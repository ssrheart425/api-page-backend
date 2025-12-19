from tortoise import fields
from tortoise.models import Model


class FBToken(Model):
    id = fields.IntField(pk=True)
    # 页面标识（例如：landing_a / landing_b / 1 / 2）
    type = fields.CharField(max_length=64, description="页面标识")
    token = fields.TextField(description="Facebook access token")
    pixel_id = fields.CharField(max_length=64, description="Facebook pixel id")
    deleted = fields.BooleanField(default=False, description="是否已删除")
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "fb_token"
