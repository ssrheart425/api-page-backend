from tortoise import fields
from tortoise.models import Model
from enum import IntEnum

from models.user import User, UserType
from utils.exceptions import BaseAppException


class AppLinkType(IntEnum):
    WHATSAPP = 1  # whatsapp
    TELEGRAM = 2  # telegram


class AppLink(Model):
    id = fields.IntField(pk=True)
    type = fields.IntEnumField(AppLinkType, default=AppLinkType.WHATSAPP, description="link类型")
    link = fields.TextField(description="app链接")
    created_at = fields.DatetimeField(auto_now_add=True)
    deleted = fields.BooleanField(default=False, description="是否已删除")

    class Meta:
        table = "app_link"

    @staticmethod
    def _assert_admin(user: User) -> None:
        # 只有管理员允许操作（新增/修改/删除）
        if user.type != UserType.ADMIN:
            raise BaseAppException(code=403, msg="Permission denied")

    @classmethod
    async def admin_create_whatsapp(cls, user: User, link: str) -> "AppLink":
        cls._assert_admin(user)
        return await cls.create(type=AppLinkType.WHATSAPP, link=link, deleted=False)

    @classmethod
    async def admin_update_whatsapp(cls, user: User, link_id: int, link: str) -> "AppLink":
        cls._assert_admin(user)
        item = await cls.get_or_none(id=link_id, type=AppLinkType.WHATSAPP, deleted=False)
        if item is None:
            raise BaseAppException(code=404, msg="not found")
        item.link = link
        await item.save(update_fields=["link"])
        return item

    @classmethod
    async def admin_delete_whatsapp(cls, user: User, link_id: int) -> None:
        cls._assert_admin(user)
        updated = await cls.filter(id=link_id, type=AppLinkType.WHATSAPP, deleted=False).update(
            deleted=True
        )
        if updated == 0:
            raise BaseAppException(code=404, msg="not found")
