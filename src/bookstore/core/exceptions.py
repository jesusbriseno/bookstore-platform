from fastapi import HTTPException


class AppException(HTTPException):
    def __init__(
        self,
        status_code: int,
        error_code: str,
        error_message: str,
        user_error: str,
        info: str | None = None,
    ):
        detail = {
            "errorCode": error_code,
            "errorMessage": error_message,
            "userError": user_error,
        }

        if info:
            detail["info"] = info

        super().__init__(status_code=status_code, detail=detail)