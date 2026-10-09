from fastapi import FastAPI

from .handler import router


def create_app() -> FastAPI:
    app = FastAPI(title="FastAPI Exercise Solution", version="0.1.0")
    app.include_router(router)
    return app


app = create_app()
