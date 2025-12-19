import base64
import hashlib
import hmac
import json
import os
import time
from datetime import datetime, timedelta
from typing import Any, Optional

from fastapi.responses import JSONResponse
from pydantic import BaseModel

from models.token import UserToken
from models.user import User


class APIResponse(BaseModel):
    code: str
    msg: str
    data: Optional[Any] = None
    extra: Optional[dict] = None

    def to_response(self) -> JSONResponse:
        return JSONResponse(status_code=200, content=self.model_dump(exclude_none=True))


_PWD_ALG = "pbkdf2_sha256"
_PWD_ITERATIONS = 200_000


def hash_password(password: str) -> str:
    salt = os.urandom(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, _PWD_ITERATIONS)
    salt_b64 = base64.urlsafe_b64encode(salt).decode("ascii").rstrip("=")
    digest_b64 = base64.urlsafe_b64encode(digest).decode("ascii").rstrip("=")
    return f"{_PWD_ALG}${_PWD_ITERATIONS}${salt_b64}${digest_b64}"


def verify_password(password: str, password_hash: str) -> bool:
    try:
        alg, iterations_str, salt_b64, digest_b64 = password_hash.split("$", 3)
        if alg != _PWD_ALG:
            return False
        iterations = int(iterations_str)

        salt = base64.urlsafe_b64decode(salt_b64 + "==")
        expected = base64.urlsafe_b64decode(digest_b64 + "==")
        actual = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)
        return hmac.compare_digest(actual, expected)
    except Exception:
        return False


def _jwt_secret() -> str:
    return os.getenv("JWT_SECRET_KEY", "")


def _jwt_algorithm() -> str:
    return os.getenv("JWT_ALGORITHM", "HS256")


def _access_token_ttl_seconds() -> int:
    # 默认 7 天
    return int(os.getenv("ACCESS_TOKEN_TTL_SECONDS", str(60 * 60 * 24 * 7)))


def token_sha256(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()


def _b64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode("ascii").rstrip("=")


def _b64url_decode(data: str) -> bytes:
    padding = "=" * (-len(data) % 4)
    return base64.urlsafe_b64decode(data + padding)


def _jwt_encode(payload: dict) -> str:
    header = {"typ": "JWT", "alg": "HS256"}
    header_b64 = _b64url_encode(json.dumps(header, separators=(",", ":")).encode("utf-8"))
    payload_b64 = _b64url_encode(json.dumps(payload, separators=(",", ":")).encode("utf-8"))
    signing_input = f"{header_b64}.{payload_b64}".encode("ascii")
    signature = hmac.new(
        _jwt_secret().encode("utf-8"), signing_input, digestmod=hashlib.sha256
    ).digest()
    return f"{header_b64}.{payload_b64}.{_b64url_encode(signature)}"


def _jwt_decode(token: str) -> dict:
    try:
        header_b64, payload_b64, signature_b64 = token.split(".", 2)
    except ValueError as e:
        raise ValueError("Invalid token format") from e

    try:
        header = json.loads(_b64url_decode(header_b64).decode("utf-8"))
        payload = json.loads(_b64url_decode(payload_b64).decode("utf-8"))
    except Exception as e:
        raise ValueError("Invalid token payload") from e

    if header.get("alg") != "HS256":
        raise ValueError("Unsupported algorithm")

    signing_input = f"{header_b64}.{payload_b64}".encode("ascii")
    expected_sig = hmac.new(
        _jwt_secret().encode("utf-8"), signing_input, digestmod=hashlib.sha256
    ).digest()
    actual_sig = _b64url_decode(signature_b64)
    if not hmac.compare_digest(actual_sig, expected_sig):
        raise ValueError("Invalid signature")

    exp = payload.get("exp")
    if exp is not None:
        try:
            exp_int = int(exp)
        except Exception as e:
            raise ValueError("Invalid exp") from e
        if time.time() >= exp_int:
            raise ValueError("Token expired")

    return payload


async def create_access_token(user: User) -> str:
    now = datetime.now()
    expires_at = now + timedelta(seconds=_access_token_ttl_seconds())
    payload = {
        "user_id": user.id,
        "iat": int(now.timestamp()),
        "exp": int(expires_at.timestamp()),
    }
    token = _jwt_encode(payload)
    await UserToken.create(
        user=user,
        token=token,
        token_hash=token_sha256(token),
        expires_at=expires_at,
        revoked=False,
    )
    return token


async def validate_token(token: str) -> Optional[User]:
    """
    校验 token（JWT 签名+过期）并从 MySQL 校验 token 是否存在且未撤销。
    返回用户对象（不存在/无效则返回 None）。
    """
    try:
        payload = _jwt_decode(token)
    except Exception:
        return None

    user_id = payload.get("user_id")
    if not user_id:
        return None

    token_row = await UserToken.get_or_none(token_hash=token_sha256(token), revoked=False)
    if token_row is None:
        return None
    # 避免 offset-aware / offset-naive datetime 比较报错：统一用 timestamp 进行比较
    if token_row.expires_at.timestamp() <= time.time():
        return None

    user = await User.get_or_none(id=token_row.user_id, deleted=False)
    if user is None:
        return None
    if user.id != int(user_id):
        return None

    return user
