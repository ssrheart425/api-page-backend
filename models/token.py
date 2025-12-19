from tortoise import fields
from tortoise.models import Model


class UserToken(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="tokens")
    token = fields.TextField(description="access token 原文")
    token_hash = fields.CharField(max_length=64, unique=True, description="token sha256(hex)")
    expires_at = fields.DatetimeField(description="过期时间")
    revoked = fields.BooleanField(default=False, description="是否已撤销")
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "user_token"


class FBToken(Model):
    id = fields.IntField(pk=True)
    type = fields.CharField(max_length=256, description="页面的type")
    fb_token = fields.CharField(max_length=256, description="fb_token")
    fb_pixel_id = fields.CharField(max_length=256, description="fb_token")
    created_at = fields.DatetimeField(auto_now_add=True)
    deleted = fields.BooleanField(default=False, description="是否已删除")

    class Meta:
        table = "fb_token"
