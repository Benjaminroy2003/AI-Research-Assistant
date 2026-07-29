from abc import ABC, abstractmethod

class BaseLLM(ABC):
    @abstractmethod
    async def generate_text(self,prompt: str,max_length: int = 100) -> str:
        pass