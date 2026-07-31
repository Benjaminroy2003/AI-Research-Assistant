from transformers import AutoModelForCausalLM, AutoTokenizer

from app.core.config import settings
from app.llm.base import BaseLLM


class HuggingFaceLLM(BaseLLM):
    def __init__(self, model_name: str | None = None):
        model_name = model_name or settings.model_name
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

    def generate_text(self, prompt: str, *, max_length: int = 100) -> str:
        device = next(self.model.parameters()).device
        inputs = self.tokenizer(prompt, return_tensors="pt").to(device)
        outputs = self.model.generate(**inputs, max_length=max_length)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
