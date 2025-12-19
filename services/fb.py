import asyncio
import json
import os
import urllib.request
from typing import Any

from fastapi import Request


def _fb_events_url(pixel_id: str, token: str) -> str:
    # Facebook Conversions API endpoint
    return f"https://graph.facebook.com/v20.0/{pixel_id}/events?access_token={token}"


def _post_json(
    url: str, payload: dict[str, Any], timeout_seconds: float = 3.0
) -> tuple[int, str]:
    # 使用标准库 urllib 发起 HTTP 请求，避免引入 httpx/aiohttp 依赖
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout_seconds) as resp:
        body = resp.read().decode("utf-8", errors="replace")
        status = getattr(resp, "status", 200)
        return status, body


async def send_fb_click_event(
    request: Request, *, event_source_url: str, fb_token: str, fb_pixel_id: str
) -> bool:
    """
    在随机接口命中时，上报一次 Facebook Conversions API 点击事件。
    - FB token / pixel id 从数据库读取并传入
    - 可选：FB_EVENT_NAME(默认 Click)、FB_TEST_EVENT_CODE(测试用)
    - 失败不会抛异常（返回 False）
    """
    event_name = os.getenv("FB_EVENT_NAME", "Click")
    test_event_code = os.getenv("FB_TEST_EVENT_CODE")

    user_data: dict[str, Any] = {
        # FB CAPI 推荐字段：客户端 IP / UA
        "client_ip_address": request.client.host if request.client else None,
        "client_user_agent": request.headers.get("user-agent"),
    }
    fbp = request.cookies.get("_fbp")
    fbc = request.cookies.get("_fbc")
    if fbp:
        # 浏览器 _fbp cookie（可选）
        user_data["fbp"] = fbp
    if fbc:
        # 浏览器 _fbc cookie（可选）
        user_data["fbc"] = fbc
    user_data = {k: v for k, v in user_data.items() if v}

    payload: dict[str, Any] = {
        "data": [
            {
                "event_name": event_name,
                "event_time": int(__import__("time").time()),
                "action_source": "website",
                "event_source_url": event_source_url,
                "user_data": user_data,
            }
        ]
    }
    if test_event_code:
        payload["test_event_code"] = test_event_code

    url = _fb_events_url(fb_pixel_id, fb_token)
    try:
        status, body = await asyncio.to_thread(_post_json, url, payload)
        # 打印 FB 返回结果（注意：不要打印 token）
        print(f"[FB] POST /events status={status} resp={body}")
        return True
    except Exception:
        # 请求失败也不影响主接口返回
        return False
