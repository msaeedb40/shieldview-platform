import uvicorn
import httpx
import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from performance.middleware import PerformanceMiddleware
from error_handling.handlers import global_exception_handler, validation_exception_handler
from telemetry.service import setup_telemetry, logger
from streaming.service import security_event_generator
from sse_starlette.sse import EventSourceResponse
from fastapi.exceptions import RequestValidationError

# Setup Telemetry
setup_telemetry()

mymiddleware = FastAPI(title="ShieldView Middleware")

# Register Middlewares
mymiddleware.add_middleware(PerformanceMiddleware)
mymiddleware.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, restrict to dashboard URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration
BACKEND_URL = os.environ.get("BACKEND_URL", "http://backend:8000")

# Proxy Helper
async def proxy_auth(path: str, request: Request):
    async with httpx.AsyncClient() as client:
        try:
            body = await request.json()
            response = await client.post(f"{BACKEND_URL}/api/auth/{path}", json=body)
            return response.json()
        except Exception as e:
            logger.error(f"auth_proxy_error", path=path, error=str(e))
            raise HTTPException(status_code=500, detail="Authentication service unavailable")

# Register Exception Handlers
mymiddleware.add_exception_handler(Exception, global_exception_handler)
mymiddleware.add_exception_handler(RequestValidationError, validation_exception_handler)

@mymiddleware.get("/health")
async def health_check():
    logger.info("health_check_triggered")
    return {"status": "active", "service": "middleware"}

# Auth Proxy Routes
@mymiddleware.post("/auth/register")
async def register(request: Request):
    return await proxy_auth("register/", request)

@mymiddleware.post("/auth/login")
async def login(request: Request):
    return await proxy_auth("token/", request)

@mymiddleware.post("/auth/refresh")
async def refresh(request: Request):
    return await proxy_auth("token/refresh/", request)

@mymiddleware.post("/auth/password-reset")
async def password_reset(request: Request):
    return await proxy_auth("password-reset/", request)

@mymiddleware.post("/auth/password-reset/confirm")
async def password_reset_confirm(request: Request):
    return await proxy_auth("password-reset/confirm/", request)

@mymiddleware.get("/stream")
async def stream_events(request: Request):
    return EventSourceResponse(security_event_generator(request))

if __name__ == '__main__':
    uvicorn.run(
        host='0.0.0.0',
        port=8400,
        app="main:mymiddleware",
        reload=True
    )