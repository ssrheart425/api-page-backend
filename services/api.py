from pydantic import BaseModel, Field


class WhatsAppLinkCreate(BaseModel):
    # 新增 WhatsApp 链接的入参
    link: str = Field(..., min_length=1)


class WhatsAppLinkUpdate(BaseModel):
    # 修改 WhatsApp 链接的入参
    link: str = Field(..., min_length=1)


class RegisterRequest(BaseModel):
    username: str = Field(..., min_length=1, max_length=255)
    password: str = Field(..., min_length=6, max_length=255)


class LoginRequest(BaseModel):
    username: str = Field(..., min_length=1, max_length=255)
    password: str = Field(..., min_length=1, max_length=255)
