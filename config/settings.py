import os
from dotenv import load_dotenv
from dataclasses import dataclass

#Reads app settings from .env
#Gives the rest of the app one clean function: get_settings()

load_dotenv()

@dataclass(frozen=True)
class Settings:
    app_name: str
    app_version: str
    environment: str

def get_settings() -> Settings:
    return Settings(
        app_name=os.getenv("APP_NAME", "FinRAG Agent"),
        app_version=os.getenv("APP_VERSION", "0.1.0"),
        environment=os.getenv("ENVIRONMENT", "development")
    )

