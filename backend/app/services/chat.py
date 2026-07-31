from app.llm.base import BaseLLM


class ChatService:
    def __init__(self, llm: BaseLLM):
        self.llm = llm

    def generate_text(self, prompt: str, *, max_length: int = 100) -> str:
        return self.llm.generate_text(prompt, max_length=max_length)
