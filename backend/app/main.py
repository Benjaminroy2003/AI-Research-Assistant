from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1.router import router as api_router
from app.core.config import settings
from app.llm.factory import create_llm


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.llm = create_llm()
    yield


print(
    f"Starting {settings.APP_NAME} in {'debug' if settings.DEBUG else 'production'} mode "
    f"on {settings.HOST}:{settings.PORT}"
)

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG, lifespan=lifespan)

app.include_router(api_router)
