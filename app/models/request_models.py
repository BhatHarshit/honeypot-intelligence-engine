from pydantic import BaseModel


class HoneypotRequest(BaseModel):
    message: str
    conversation_id: str
