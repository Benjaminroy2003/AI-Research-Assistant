from fastapi import APIRouter, Depends

from app.api.deps import get_chat_service
from app.schemas.chat import ChatResponse
from app.services.chat import ChatService

router = APIRouter()


@router.post("/chat")
def chat_endpoint(
    message: ChatResponse,
    chat_service: ChatService = Depends(get_chat_service),
):
    response = chat_service.generate_text(message.message)

    return ChatResponse(message=response)
