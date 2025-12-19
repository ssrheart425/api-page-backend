from fastapi import Depends, Request

from models.user import User, UserType
from services.common import validate_token
from utils.exceptions import BaseAppException


async def get_current_user(request: Request) -> User:
    """
    校验用户 token 并返回用户对象
    - 从 MySQL 校验 token 是否存在且未撤销
    - 校验通过后挂载到 request.state.user / request.state.user_id
    """
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise BaseAppException(code=401, msg="Not logged in or token missing")
    token = auth_header[7:].strip()
    if not token:
        raise BaseAppException(code=401, msg="Token is empty")
    user = await validate_token(token)
    if not user:
        raise BaseAppException(code=401, msg="Invalid token or user not found")

    request.state.user = user
    request.state.user_id = user.id
    return user


async def require_admin(user: User = Depends(get_current_user)) -> User:
    """
    管理员权限校验：必须是 type=admin 的用户才允许通过。
    """
    if user.type != UserType.ADMIN:
        raise BaseAppException(code=403, msg="Permission denied")
    return user
