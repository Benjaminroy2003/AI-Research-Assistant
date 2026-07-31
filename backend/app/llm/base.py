from abc import ABC, abstractmethod


class BaseLLM(ABC):
    """Abstract interface for language model text generation."""

    @abstractmethod
    def generate_text(self, prompt: str, *, max_length: int = 100) -> str:
        """Generate text from the given prompt."""
        ...

