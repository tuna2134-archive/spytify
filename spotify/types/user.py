from typing import TypedDict


class UserType(TypedDict):
    country: str
    display_name: str
    email: str
    explicit_content: dict
    external_urls: dict
    followers: dict
    href: str
    id: str
    images: list
    product: str
    type: str
    uri: str