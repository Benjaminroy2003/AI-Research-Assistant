from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    APP_NAME: str = "AI Research Assistant"

    DEBUG: bool = True

    OPENAI_API_KEY: str = "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

    HOST: str = "0.0.0.0"

    PORT: int = 8000

    LLM_PROVIDER: str = "huggingface"

    model_name: str = "Qwen/Qwen2.5-1.5B-Instruct"

    class Config:
        env_file = ".env"


settings = Settings()