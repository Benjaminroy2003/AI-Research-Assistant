from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForCausalLM
from app.core.config import settings

class LLM:
    def __init__(self):
        self.pipe = pipeline("text-generation", model=settings.model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(settings.model_name)
        self.model =  AutoModelForCausalLM.from_pretrained(settings.model_name, device_map="auto")

    def generate_text(self, prompt: str, max_length: int = 100):
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_length=max_length)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
