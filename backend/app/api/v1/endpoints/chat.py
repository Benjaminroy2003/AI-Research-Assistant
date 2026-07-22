# Accept a user message (POST /chat)
# Validate it with Pydantic
# Call a service layer
# Return an AI response

from fastapi import APIRouter
from app.services.chat import ChatResponse

router = APIRouter()

@router.post("/chat")
def chat_endpoint(message: ChatResponse):
    response = f"Received message: {message.message}"
    return ChatResponse(message=response)