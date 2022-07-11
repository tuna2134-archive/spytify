from .http import SpotifyRequester
from .account import Account
from .album import Album


class Client:
    def __init__(self):
        self.requester = SpotifyRequester()

    async def get_token(self, client_id: str, client_secret: str) -> Account:
        return Account(await self.requester.get_token(client_id, client_secret))

    async def close(self) -> None:
        await self.requester.close()

    async def fetch_album(self, album_id: str) -> Album:
        return Album(await self.requester.get_album(album_id))