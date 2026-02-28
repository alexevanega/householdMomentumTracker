from fastapi import HTTPException
from fastapi.responses import JSONResponse

def build_error_response(code: str, message: str, status_code: int) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={
            "error": {
                "code": code,
                "message": message
            }
        }
    )

class APIError(Exception):
    def __init__(self, code: str, message: str, status_code: int):
        self.code = code
        self.message = message
        self.status_code = status_code

class ValidationError(APIError):
    def __init__(self, message: str):
        super().__init__(
            code="validation_error",
            message=message,
            status_code=400
        )

class NotFoundError(APIError):
    def __init__(self, message: str):
        super().__init__(
            code="validation_error",
            message=message,
            status_code=404
        )

class ConflictError(APIError):
    def __init__(self, code:str, message:str):
        super().__init__(
            code=code,
            message=message,
            status_code=409
        )