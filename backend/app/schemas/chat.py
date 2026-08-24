from pydantic import BaseModel,Field
from typing import Optional
import uuid

class ChatRequest(BaseModel):
    message : str
    conversation_id : Optional[str] = Field(default_factory=lambda:str(uuid.uuid4()), description="Unique identifier for the conversation")

class ChatResponse(BaseModel):
    message : str
    conversation_id : str