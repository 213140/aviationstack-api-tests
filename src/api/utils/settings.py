import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv("API_BASE_URL", "https://api.aviationstack.com/v1")
    access_key: str | None = os.getenv("AVIATIONSTACK_ACCESS_KEY")
    timeout_seconds: int = int(os.getenv("TIMEOUT_SECONDS", "10"))
