from fastapi import FastAPI
from routers import links
from routers import user
from routers import fb_token
from tortoise.contrib.fastapi import register_tortoise
from app.db import TORTOISE_ORM
from fastapi.middleware.cors import CORSMiddleware
from utils.exceptions import register_exception_handlers

app = FastAPI()

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 全局异常
register_exception_handlers(app)

app.include_router(links.router, prefix="/api/v1")
app.include_router(user.router, prefix="/api/v1")
app.include_router(fb_token.router, prefix="/api/v1")
