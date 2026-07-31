from fastapi import APIRouter

from app.llm.factory import get_llm
from app.schemas.chat import ChatResponse
from app.services.chat import ChatService

router = APIRouter()


@router.post("/chat")
def chat_endpoint(message: ChatResponse):
    chat_service = ChatService(llm=get_llm())

    response = chat_service.generate_text(message.message)

    return ChatResponse(message=response)