from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel, Field

from middleware.auth import require_admin
from models.fb_token import FBToken
from models.user import User
from services.common import APIResponse

router = APIRouter(prefix="/fb_token", tags=["FBToken"])


class FBTokenCreate(BaseModel):
    # 页面标识（例如：landing_a / landing_b / 1 / 2）
    type: str = Field(..., min_length=1, max_length=64)
    token: str = Field(..., min_length=1)
    pixel_id: str = Field(..., min_length=1, max_length=64)


class FBTokenUpdate(BaseModel):
    # 允许只修改其中某个字段
    token: str | None = Field(None, min_length=1)
    pixel_id: str | None = Field(None, min_length=1, max_length=64)


@router.get("", response_model=APIResponse)
async def list_fb_tokens(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    token_type: str | None = Query(None, alias="type", min_length=1, max_length=64),
    token: str | None = Query(None, min_length=1),
    pixel_id: str | None = Query(None, min_length=1, max_length=64),
    _admin_user: User = Depends(require_admin),
):
    """
    分页查询 FB token 配置（仅管理员）
    请求示例：
    - /api/v1/fb_token?type=share&page=1&size=10
    - /api/v1/fb_token?token=123&page=1&size=10
    - /api/v1/fb_token?token=123&pixel_id=863840896392599&page=1&size=10
    """
    qs = FBToken.filter(deleted=False)
    if token_type is not None:
        qs = qs.filter(type=token_type)
    if token is not None:
        qs = qs.filter(token__contains=token)
    if pixel_id is not None:
        qs = qs.filter(pixel_id=pixel_id)

    total = await qs.count()
    items = await qs.order_by("created_at").offset((page - 1) * size).limit(size).values()
    return APIResponse(
        code="200",
        msg="ok",
        data={"page": page, "size": size, "total": total, "items": items},
    )


@router.get("/by_type", response_model=APIResponse)
async def get_fb_token_by_type(
    token_type: str = Query(..., alias="type", min_length=1, max_length=64),
):
    """
    根据 type 查询 FB token 配置
    请求示例：/api/v1/fb_token/by_type?type=landing_a
    """
    item = await FBToken.get_or_none(type=token_type, deleted=False)
    if not item:
        return APIResponse(code="404", msg="not found", data=None)
    return APIResponse(
        code="200",
        msg="ok",
        data={
            "id": item.id,
            "type": item.type,
            "pixel_id": item.pixel_id,
            "token": item.token,
        },
    )


@router.get("/{token_id}", response_model=APIResponse)
async def get_fb_token(token_id: int, _admin_user: User = Depends(require_admin)):
    """
    查询单条 FB token 配置（仅管理员）
    """
    item = await FBToken.get_or_none(id=token_id, deleted=False)
    if not item:
        return APIResponse(code="404", msg="not found", data=None)
    return APIResponse(
        code="200",
        msg="ok",
        data={
            "id": item.id,
            "type": item.type,
            "pixel_id": item.pixel_id,
            "token": item.token,
        },
    )


@router.post("", response_model=APIResponse)
async def create_fb_token(payload: FBTokenCreate, _admin_user: User = Depends(require_admin)):
    """
    新增 FB token + pixel 配置（仅管理员）
    """
    exists = await FBToken.get_or_none(type=payload.type, deleted=False)
    if exists:
        return APIResponse(code="400", msg="type already exists", data=None)

    item = await FBToken.create(
        type=payload.type, token=payload.token, pixel_id=payload.pixel_id, deleted=False
    )
    return APIResponse(
        code="200",
        msg="ok",
        data={"id": item.id, "type": item.type, "pixel_id": item.pixel_id},
    )


@router.put("/{token_id}", response_model=APIResponse)
async def update_fb_token(
    token_id: int, payload: FBTokenUpdate, _admin_user: User = Depends(require_admin)
):
    """
    修改 FB token + pixel 配置（仅管理员）
    """
    item = await FBToken.get_or_none(id=token_id, deleted=False)
    if not item:
        return APIResponse(code="404", msg="not found", data=None)

    update_fields: list[str] = []
    if payload.token is not None:
        item.token = payload.token
        update_fields.append("token")
    if payload.pixel_id is not None:
        item.pixel_id = payload.pixel_id
        update_fields.append("pixel_id")

    if update_fields:
        await item.save(update_fields=update_fields)
    return APIResponse(
        code="200",
        msg="ok",
        data={"id": item.id, "type": item.type, "pixel_id": item.pixel_id},
    )


@router.delete("/{token_id}", response_model=APIResponse)
async def delete_fb_token(token_id: int, _admin_user: User = Depends(require_admin)):
    """
    删除 FB token 配置（软删除，仅管理员）
    """
    updated = await FBToken.filter(id=token_id, deleted=False).update(deleted=True)
    if updated == 0:
        return APIResponse(code="404", msg="not found", data=None)
    return APIResponse(code="200", msg="ok", data={"deleted": token_id})
