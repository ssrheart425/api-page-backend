from fastapi import APIRouter, Depends, Query, Request
from services.common import APIResponse
from models.page_link import AppLink, AppLinkType
from services.api import WhatsAppLinkCreate, WhatsAppLinkUpdate
from middleware.auth import require_admin
from models.user import User
from services.fb import send_fb_click_event
from models.fb_token import FBToken
import random

router = APIRouter(tags=["Links"])


@router.get("/links")
async def get_links(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    type: AppLinkType | None = Query(None),
    link: str | None = Query(None, min_length=1),
):
    """
    分页查询链接
    请求示例：/api/v1/links?page=1&size=10
    筛选示例：/api/v1/links?page=1&size=10&type=1&link=whatsapp
    """
    qs = AppLink.filter(deleted=False)
    if type is not None:
        qs = qs.filter(type=type)
    if link is not None:
        qs = qs.filter(link__contains=link)

    total = await qs.count()
    items = await qs.order_by("created_at").offset((page - 1) * size).limit(size).values()
    return APIResponse(
        code="200",
        msg="ok",
        data={"page": page, "size": size, "total": total, "items": items},
    )


@router.get("/links/random")
async def get_random_link(
    request: Request,
    page_type: str = Query(..., alias="type", min_length=1),
    link_type: AppLinkType = AppLinkType.WHATSAPP,
):
    # 随机返回 1 条未删除的链接
    page_links = await AppLink.filter(type=link_type, deleted=False).all().values()
    if not page_links:
        return APIResponse(code="200", msg="no data", data=None)
    page_link = random.choice(page_links)
    # 额外上报一次 FB 点击事件（失败不影响正常返回）
    # - FB token/pixel 从数据库表 FBToken 中按 type(page_type) 读取
    # - 上报结果会在控制台打印：[FB] POST /events status=... resp=...
    link_url = page_link.get("link") if isinstance(page_link, dict) else None
    if link_url:
        fb_cfg = await FBToken.get_or_none(type=page_type, deleted=False)
        if fb_cfg:
            await send_fb_click_event(
                request,
                event_source_url=link_url,
                fb_token=fb_cfg.token,
                fb_pixel_id=fb_cfg.pixel_id,
            )
    return APIResponse(code="200", msg="ok", data=page_link)


@router.post("/links")
async def create_links(payload: WhatsAppLinkCreate, admin_user: User = Depends(require_admin)):
    # 新增 WhatsApp 链接（仅管理员）
    item = await AppLink.admin_create_whatsapp(admin_user, payload.link)
    return APIResponse(code="200", msg="ok", data={"id": item.id, "link": item.link})


@router.put("/links/{link_id}")
async def update_links(
    link_id: int, payload: WhatsAppLinkUpdate, admin_user: User = Depends(require_admin)
):
    # 修改指定 id 的 WhatsApp 链接（仅管理员）
    item = await AppLink.admin_update_whatsapp(admin_user, link_id, payload.link)
    return APIResponse(code="200", msg="ok", data={"id": item.id, "link": item.link})


@router.delete("/links/{link_id}")
async def delete_links(link_id: int, admin_user: User = Depends(require_admin)):
    # 删除指定 id 的 WhatsApp 链接（仅管理员，软删除）
    await AppLink.admin_delete_whatsapp(admin_user, link_id)
    return APIResponse(code="200", msg="ok", data={"deleted": link_id})
