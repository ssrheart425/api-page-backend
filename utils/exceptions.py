import traceback

from fastapi import HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from services.common import APIResponse


class BaseAppException(Exception):
    def __init__(self, code: int = 400, msg: str = "Business Exception", data=None):
        self.code = code
        self.msg = msg
        self.data = data
        super().__init__(msg)


async def global_exception_handler(request: Request, exc: Exception):
    _ = traceback.format_exc()
    response_data = APIResponse(
        code="500",
        msg="Internal server error.",
        data=None,
    )
    return JSONResponse(
        status_code=500, content=response_data.model_dump(exclude_none=True)
    )


async def base_app_exception_handler(request: Request, exc: BaseAppException):
    response_data = APIResponse(
        code=str(exc.code),
        msg=exc.msg or "Business error.",
        data=exc.data,
    )
    return JSONResponse(
        status_code=exc.code, content=response_data.model_dump(exclude_none=True)
    )


async def http_exception_handler(request: Request, exc: HTTPException):
    response_data = APIResponse(
        code=str(exc.status_code),
        msg=str(exc.detail) if exc.detail else "HTTP error.",
        data=None,
    )
    return JSONResponse(
        status_code=exc.status_code, content=response_data.model_dump(exclude_none=True)
    )


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    response_data = APIResponse(
        code="422",
        msg="Validation failed.",
        data=exc.errors(),
    )
    return JSONResponse(
        status_code=422, content=response_data.model_dump(exclude_none=True)
    )


def register_exception_handlers(app):
    app.add_exception_handler(BaseAppException, base_app_exception_handler)
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(Exception, global_exception_handler)

