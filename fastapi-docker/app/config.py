import os
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    ENV: str

    class Config:
        env_file = os.getenv(
            "ENV", ".env.development"
        )


config = Config()