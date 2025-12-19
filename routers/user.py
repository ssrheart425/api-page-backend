from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field

from middleware.auth import require_admin
from models.user import User, UserType
from services.common import APIResponse, create_access_token, hash_password, verify_password
from utils.exceptions import BaseAppException
from services.api import RegisterRequest, LoginRequest


router = APIRouter(prefix="/user", tags=["User"])


class UpdateUserTypeRequest(BaseModel):
    # 1=admin, 2=user（也可直接传字符串枚举名）
    type: UserType


@router.post("/register", response_model=APIResponse)
async def register(payload: RegisterRequest):
    exists = await User.get_or_none(username=payload.username, deleted=False)
    if exists:
        raise BaseAppException(code=400, msg="Username already exists")

    # 初始化场景：当系统还没有任何用户时，将第一个注册用户设为管理员，便于后续配置权限
    user_type = UserType.ADMIN if await User.filter(deleted=False).count() == 0 else UserType.USER

    user = await User.create(
        username=payload.username,
        password=hash_password(payload.password),
        type=user_type,
        deleted=False,
    )
    token = await create_access_token(user)
    return APIResponse(
        code="200",
        msg="ok",
        data={
            "token": token,
            "user": {"id": user.id, "username": user.username, "type": int(user.type)},
        },
    )


@router.post("/login", response_model=APIResponse)
async def login(payload: LoginRequest):
    user = await User.get_or_none(username=payload.username, deleted=False)
    if not user or not verify_password(payload.password, user.password):
        raise BaseAppException(code=401, msg="Invalid username or password")

    token = await create_access_token(user)
    return APIResponse(
        code="200",
        msg="ok",
        data={
            "token": token,
            "user": {"id": user.id, "username": user.username, "type": int(user.type)},
        },
    )


@router.get("/all_user", response_model=APIResponse)
async def all_user():
    """查询所有用户"""
    user = await User.filter(deleted=False)
    user_list = []
    for i in user:
        user_list.append({"id": i.id, "username": i.username, "type": i.type})
    return APIResponse(code="200", msg="ok", data=user_list)


@router.put("/type/{user_id}", response_model=APIResponse)
async def update_user_type(
    user_id: int,
    payload: UpdateUserTypeRequest,
    _admin_user: User = Depends(require_admin),
):
    """
    修改用户权限（仅管理员可操作）
    """
    target = await User.get_or_none(id=user_id, deleted=False)
    if not target:
        return APIResponse(code="0", msg="user not found")

    target.type = payload.type
    await target.save(update_fields=["type"])
    return APIResponse(
        code="200",
        msg="ok",
        data={"id": target.id, "username": target.username, "type": int(target.type)},
    )
