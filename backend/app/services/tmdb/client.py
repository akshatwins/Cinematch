import httpx
from app.core.config import get_settings


class TMDBClient:
    def __init__(self):
        self.settings = get_settings()

    @property
    def configured(self) -> bool:
        return bool(self.settings.tmdb_access_token)

    async def get(self, path: str, params: dict | None = None):
        if not self.configured:
            raise RuntimeError("TMDB_ACCESS_TOKEN is not configured.")
        headers = {
            "Authorization": f"Bearer {self.settings.tmdb_access_token}",
            "accept": "application/json",
        }
        async with httpx.AsyncClient(
            base_url=self.settings.tmdb_base_url,
            timeout=self.settings.request_timeout_seconds,
            headers=headers,
        ) as client:
            response = await client.get(path, params=params or {})
            response.raise_for_status()
            return response.json()

    def image_url(self, path: str | None, size: str = "w500") -> str | None:
        if not path:
            return None
        return f"{self.settings.tmdb_image_base_url}/{size}{path}"


tmdb = TMDBClient()
