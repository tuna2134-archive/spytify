from .http import SpotifyRequester
from .account import Account
from .albums import Album
from .user import User


class Client:
    """
    Client class for Spotify api

    Attributes:
        requester (SpotifyRequester): http requester
    """

    def __init__(self):
        self.requester = SpotifyRequester()

    async def get_token(self, client_id: str, client_secret: str) -> Account:
        """
        Get a token. This can take access_token
        
        Args:
            cleint_id (str): cleint id
            client_secret (str): client secret

        Returns:
            Account: account object"""
        return Account(await self.requester.get_token(client_id, client_secret))
    
    async def get_user(self) -> User:
        return User(await self.requester.get_user())

    async def close(self) -> None:
        "Close the client."
        await self.requester.close()

    async def fetch_album(
        self, album_id: str, *, limit: int | None = 20, store: str | None = None,
        offset: int | None = None
    ) -> Album:
        """
        Fetch an album.

        Args:
            album_id (str): album id
            limit (int | None): limit
            store (str | None): store
            offset (int | None): offset
        """
        payload = {}
        if limit is not None:
            payload["limit"] = limit
        if store is not None:
            payload["store"] = store
        if offset is not None:
            payload["offset"] = offset
        return Album(await self.requester.get_album(album_id), self.requester)
