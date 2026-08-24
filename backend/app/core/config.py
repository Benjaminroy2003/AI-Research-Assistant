from typing import Optional

from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    APP_NAME: str = "AI Research Assistant"

    DEBUG: bool = True

    OPENAI_API_KEY: str = "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

    HOST: str = "0.0.0.0"

    PORT: int = 8000

    LLM_PROVIDER: str = "huggingface"

    model_name: str = "Qwen/Qwen2.5-1.5B-Instruct"

    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "ai_research_assistant"
    DATABASE_URL: Optional[str] = None

    @property
    def sync_database_url(self) -> str:                                                                                              
        if self.DATABASE_URL:                                                                                                        
            if self.DATABASE_URL.startswith("postgres://"):                                                                          
                return self.DATABASE_URL.replace("postgres://", "postgresql://", 1)                                                  
            return self.DATABASE_URL                                                                                                 
        return (                                                                                                                     
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"                                                            
            f"@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"                                                       
        )                                                                                                                            
              

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()