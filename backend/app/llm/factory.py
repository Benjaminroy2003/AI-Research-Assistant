from app.core.config import settings
from app.llm.base import BaseLLM

_llm: BaseLLM | None = None


def get_llm() -> BaseLLM:
    global _llm
    if _llm is None:
        _llm = _create_llm()
    return _llm


def _create_llm() -> BaseLLM:
    match settings.LLM_PROVIDER:
        case "huggingface":
            from app.llm.hugging_face import HuggingFaceLLM

            return HuggingFaceLLM()
        case _:
            raise ValueError(f"Unknown LLM provider: {settings.LLM_PROVIDER!r}")
