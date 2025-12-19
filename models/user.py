from tortoise import fields
from tortoise.models import Model
from enum import IntEnum


class UserType(IntEnum):
    ADMIN = 1  # admin
    USER = 2  # user


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255, unique=True, description="用户名")
    password = fields.CharField(max_length=255, description="密码哈希")
    type = fields.IntEnumField(UserType, default=UserType.USER, description="用户类型")
    created_at = fields.DatetimeField(auto_now_add=True)
    deleted = fields.BooleanField(default=False, description="是否已删除")

    class Meta:
        table = "user"
