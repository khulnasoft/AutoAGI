from fastapi import FastAPI

from .routes.v1 import v1_router

external_app = FastAPI(
    title="AutoAGI External API",
    description="External API for AutoAGI integrations",
    docs_url="/docs",
    version="1.0",
)
external_app.include_router(v1_router, prefix="/v1")
