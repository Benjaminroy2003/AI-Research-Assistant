# app/services/chat.py

from app.llm.hugging_face import LLM


class ChatService:
    def __init__(self):
        self.llm = LLM()

    def generate_text(self, prompt: str, max_length: int = 100):
        return self.llm.generate_text(prompt, max_length)