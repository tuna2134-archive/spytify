from httpx import AsyncClient

from base64 import b64encode

from .types.access_token import AccessTokenType
from .types.user import UserType
from .types.album import AlbumType
from .errors import TokenError


class SpotifyRequester:
    BASEURL: str = "https://api.spotify.com/v1"
    TOKEN: str | None = None
    TOKEN_TYPE: str | None = None

    def __init__(self):
        self.client = AsyncClient()

    async def request(self, method: str, endpoint: str, **kwargs) -> dict | None:
        if self.TOKEN is None:
            raise TokenError("No token set")
        else:
            headers = {
                "Authorization": f"{self.TOKEN_TYPE} {self.TOKEN}"
            }
            headers.update(kwargs.pop("headers", {}))
            kwargs["headers"] = headers
        response = await self.client.request(method, self.BASEURL + endpoint, **kwargs)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 204:
            return None
        elif response.status_code == 401:
            raise TokenError("Token expired")
        elif response.status_code == 404:
            raise TokenError(response.json()["error"]["message"])
        else:
            raise Exception(response.json()["error"]["message"])

    async def get_user(self) -> UserType:
        return await self.request("GET", "/me")

    async def get_token(self, client_id: str, client_secret: str) -> AccessTokenType:
        basic_auth = b64encode(f"{client_id}:{client_secret}".encode()).decode()
        res = await self.client.request("POST", "https://accounts.spotify.com/api/token", headers={
            "Authorization": f'Basic {basic_auth}',
            "Content-Type": "application/x-www-form-urlencoded"
        }, data={
            "grant_type": "client_credentials"
        })
        self.TOKEN = res.json()["access_token"]
        self.TOKEN_TYPE = res.json()["token_type"]
        return res.json()

    async def get_album(self, album_id: str) -> AlbumType:
        return await self.request("GET", f"/albums/{album_id}")

    async def get_album_tracks(
        self, album_id: str, payload: dict
    ) -> list:
        return await self.request("GET", f"/albums/{album_id}/tracks", params=payload)

    async def close(self) -> None:
        await self.client.aclose()