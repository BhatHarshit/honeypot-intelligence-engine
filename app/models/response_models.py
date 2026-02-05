from pydantic import BaseModel
from typing import List, Dict


class ExtractedIntelligence(BaseModel):
    upi_ids: List[str]
    bank_accounts: List[str]
    links: List[str]


class HoneypotResponse(BaseModel):
    scam_detected: bool
    confidence: float
    risk_level: str
    extracted_intelligence: ExtractedIntelligence
    agent_response: str
    turn_count: int
    simulation_mode: bool
