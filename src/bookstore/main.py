from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging
from fastapi.exceptions import RequestValidationError

from bookstore.api.v1.books import router as books_router
from bookstore.api.v1.auth import router as auth_router
from bookstore.core.config import settings
from bookstore.core.exceptions import AppException
import time

# -------------------------------------------------
# Configuracion de logging
# -------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger("bookstore")

# -------------------------------------------------
# Crear aplicacion
# -------------------------------------------------
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
)

# -------------------------------------------------
# Registrar routers
# -------------------------------------------------
app.include_router(books_router)
app.include_router(auth_router)

# -------------------------------------------------
# Manejador global AppException (errores controlados)
# -------------------------------------------------
@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    logger.error(f"Application error: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.detail,
    )

# -------------------------------------------------
# Manejador global errores inesperados (500)
# -------------------------------------------------
@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    logger.exception("Unexpected error occurred")
    return JSONResponse(
        status_code=500,
        content={
            "errorCode": "SYS_500",
            "errorMessage": "Internal server error",
            "userError": "Ocurrio un error inesperado. Intente nuevamente.",
        },
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.warning(f"Validation error: {exc.errors()}")

    return JSONResponse(
        status_code=422,
        content={
            "errorCode": "REQ_422",
            "errorMessage": "Validation error",
            "userError": "Los datos enviados no son validos",
        },
    )

# -------------------------------------------------
# Root endpoint
# -------------------------------------------------
@app.get("/", tags=["Root"])
def root():
    return {"message": "BookStore API running"}


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    logger.info(f"Incoming request: {request.method} {request.url}")

    response = await call_next(request)

    process_time = round((time.time() - start_time) * 1000, 2)

    logger.info(
        f"Completed {request.method} {request.url} "
        f"Status={response.status_code} "
        f"Duration={process_time}ms"
    )

    return response