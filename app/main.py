from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(
        title="URL Shortener",
        version="0.1.0",
        description="Public URL shortener API without authentication in v1.0.",
    )

    @app.get("/health", tags=["health"])
    def health_check() -> dict[str, str]:
        return {"status": "ok"}

    return app


app = create_app()
