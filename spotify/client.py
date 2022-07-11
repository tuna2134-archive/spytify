from .http import SpotifyRequester
from .account import Account
from .albums import Album


class Client:
    def __init__(self):
        self.requester = SpotifyRequester()

    async def get_token(self, client_id: str, client_secret: str) -> Account:
        return Account(await self.requester.get_token(client_id, client_secret))

    async def close(self) -> None:
        await self.requester.close()

    async def fetch_album(
        self, album_id: str, *, limit: int | None = 20, store: str | None = None,
        offset: int | None = None
    ) -> Album:
        payload = {}
        if limit is not None:
            payload["limit"] = limit
        if store is not None:
            payload["store"] = store
        if offset is not None:
            payload["offset"] = offset
        return Album(await self.requester.get_album(album_id), self.requester)