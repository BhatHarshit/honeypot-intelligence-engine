from fastapi import APIRouter, Depends
from app.core.auth import verify_api_key
from app.models.request_models import HoneypotRequest
from app.models.response_models import HoneypotResponse

router = APIRouter(prefix="/honeypot", tags=["Honeypot"])


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.post("/analyze", response_model=HoneypotResponse)
def analyze_message(
    request: HoneypotRequest,
    _: str = Depends(verify_api_key)
):
    return {
        "scam_detected": False,
        "confidence": 0.0,
        "risk_level": "LOW",
        "extracted_intelligence": {
            "upi_ids": [],
            "bank_accounts": [],
            "links": []
        },
        "agent_response": "Can you explain more?",
        "turn_count": 1,
        "simulation_mode": True
    }
