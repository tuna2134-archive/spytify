from .types.album import AlbumType


class Album:
    def __init__(self, payload: AlbumType):
        self.payload = payload

    @property
    def album_type(self) -> str:
        return self.payload["album_type"]

    @property
    def total_tracks(self) -> int:
        return self.payload["total_tracks"]

    @property
    def available_markets(self) -> list:
        return self.payload["available_markets"]

    @property
    def external_urls(self) -> dict:
        return self.payload["external_urls"]

    @property
    def href(self) -> str:
        return self.payload["href"]

    @property
    def id(self) -> str:
        return self.payload["id"]

    @property
    def images(self) -> list:
        return self.payload["images"]

    @property
    def name(self) -> str:
        return self.payload["name"]

    @property
    def release_date(self) -> str:
        return self.payload["release_date"]

    @property
    def release_date_precision(self) -> str:
        return self.payload["release_date_precision"]

    @property
    def restrictions(self) -> dict:
        return self.payload["restrictions"]

    @property
    def type(self) -> str:
        return self.payload["type"]

    @property
    def uri(self) -> str:
        return self.payload["uri"]

    @property
    def artists(self) -> list:
        return self.payload["artists"]

    @property
    def tracks(self) -> dict:
        return self.payload["tracks"]