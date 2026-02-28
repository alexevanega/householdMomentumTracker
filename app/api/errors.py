from __future__ import annotations
from typing import Any, Dict, Optional
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

def error_payload(code: str, message: str, details: Optional[Any] = None) -> Dict[str, Any]:
    """
    Cannonical error payload shape for the entire API.
    
    - 'code': machine-readable (snake_case)
    - 'messsage': human-readable
    - 'details': optional extra info (only when useful)
    """
    payload: Dict[str,Any] = {
        "error": {
            "code": code,
            "message": message
        }
    }

    if details is not None:
        payload["error"]["details"] = details
    
    return payload

def build_error_response(code: str, message: str, status_code: int, details: Optional[Any] = None) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content= error_payload(code=code, message=message, details=details)
    )

class APIError(Exception):
    def __init__(self, code: str, message: str, status_code: int, details: Optional[Any] = None):
        self.code = code
        self.message = message
        self.status_code = status_code
        self.details = details

class ValidationError(APIError):
    def __init__(self, message: str, details: Optional[Any] = None):
        super().__init__(
            code="validation_error",
            message=message,
            status_code=400,
            details=details
        )

class NotFoundError(APIError):
    def __init__(self, message: str, details: Optional[Any] = None):
        super().__init__(
            code="validation_error",
            message=message,
            status_code=404,
            details=details
        )

class ConflictError(APIError):
    """
    For invariant violations / state machine violations.
    Provide a specific machine code per conflict type (e.g. 'daily_win_conflict, 'invalid_transition').
    """
    def __init__(self, code:str, message:str, details: Optional[Any] = None):
        super().__init__(
            code=code,
            message=message,
            status_code=409,
            details=details
        )

# --------------------------
# Exeption Handler Functions
# --------------------------
async def api_error_handler(request: Request, exc: APIError) -> JSONResponse:
    return build_error_response(
        code=exc.code,
        message=exc.message,
        status_code=exc.status_code,
        details=getattr(exc, "details", None)
    )

async def request_validation_error_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    """
    Normalizes FastAPI/Pydantic validation into cannonical error shape.
    - loc: where it failed (e.g ["body","title"])
    - msg: human message
    - type: pydantic error type
    """
    normalized_details = [
        {
            "loc": list(err.get("loc", [])),
            "msg": err.get("msg", "Invalid Value"),
            "type": err.get("type", "validation_error")
        }
        for err in exc.errors()
    ]
    return build_error_response(
        code="request_validation_error",
        message="Request Validation Failed",
        status_code=400,
        details=normalized_details
    )

async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    """
    Normalizes any accidental HTTPException usage (or internal FastAPI raises)
    into cannonical shape
    - If detail is a string, use it as message
    - If detail is a dict and already matches our shape, pass through.
    - Otherwise, convert it safely
    """
    detail = exc.detail
    # If someone raised HTTPException with our already-cannonical shape, honor it.
    if isinstance(detail, dict) and "error" in detail and isinstance(detail["error"], dict):
        return JSONResponse(status_code=exc.status_code, content=detail)
    
    message = detail if isinstance(detail, str) else "Request Failed."
    return build_error_response(
        code="http_exception",
        message=message,
        status_code=exc.status_code
    )