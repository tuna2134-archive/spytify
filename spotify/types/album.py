from typing import TypedDict, List


class AlbumType(TypedDict):
    album_type: str
    total_tracks: int
    available_markets: List[str]
    external_urls: dict
    href: str
    id: str
    images: List[dict]
    name: str
    release_date: str
    release_date_precision: str
    restrictions: dict
    type: str
    uri: str
    artists: list
    tracks: dict