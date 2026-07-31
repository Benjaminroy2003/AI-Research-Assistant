from app.core.config import settings
from app.llm.base import BaseLLM


def create_llm() -> BaseLLM:
    match settings.LLM_PROVIDER:
        case "huggingface":
            from app.llm.hugging_face import HuggingFaceLLM

            return HuggingFaceLLM()
        case _:
            raise ValueError(f"Unknown LLM provider: {settings.LLM_PROVIDER!r}")
