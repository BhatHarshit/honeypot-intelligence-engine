from fastapi import FastAPI
from app.routes.honeypot import router as honeypot_router

app = FastAPI(
    title="Honeypot Intelligence Engine",
    version="1.0.0"
)

app.include_router(honeypot_router)
