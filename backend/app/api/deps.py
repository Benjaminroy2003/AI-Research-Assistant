from fastapi import Depends, Request

from app.llm.base import BaseLLM
from app.services.chat import ChatService


def get_llm(request: Request) -> BaseLLM:
    return request.app.state.llm


def get_chat_service(llm: BaseLLM = Depends(get_llm)) -> ChatService:
    return ChatService(llm=llm)
