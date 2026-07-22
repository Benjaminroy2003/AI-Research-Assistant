from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.router import router as api_router


print(f"Starting {settings.APP_NAME} in {'debug' if settings.DEBUG else 'production'} mode on {settings.HOST}:{settings.PORT}")

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)

app.include_router(api_router)