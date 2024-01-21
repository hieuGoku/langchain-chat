"""Start Application."""

import uvicorn
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from app.api.routes import api_route
from app.configs import config_server
from app.logger.logger import custom_logger


class LoggingMiddleware(BaseHTTPMiddleware):
    """Logging All API Requests"""

    async def dispatch(self, request, call_next: RequestResponseEndpoint) -> Response:
        custom_logger.info(
            f"Request: {request.method} {request.url} {request.client.host}"
        )
        response = await call_next(request)
        custom_logger.info("Response status code: %s", response.status_code)
        return response


def create_app() -> FastAPI:
    """
    The function creates a FastAPI application with CORS middleware and logging middleware, and includes
    a router for API routes.
    :return: The function `create_app()` returns an instance of the `FastAPI` class.
    """

    app = FastAPI(title="Langchain Chat API", version="0.1.0")

    custom_logger.debug("Setting up CORS middleware")
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    custom_logger.debug("Setting up logging middleware")
    app.add_middleware(LoggingMiddleware)

    app.include_router(api_route)

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, host=config_server.HOST, port=config_server.PORT, log_config=None)
