from .types.user import UserType


class User:
    def __init__(self, payload: UserType):
        self.payload = payload

    @property
    def country(self) -> str:
        return self.payload["country"]

    @property
    def display_name(self) -> str:
        return self.payload["display_name"]

    @property
    def email(self) -> str:
        return self.payload["email"]

    @property
    def explicit_content(self) -> dict:
        return self.payload["explicit_content"]

    @property
    def external_urls(self) -> dict:
        return self.payload["external_urls"]

    @property
    def followers(self) -> dict:
        return self.payload["followers"]

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
    def product(self) -> str:
        return self.payload["product"]

    @property
    def type(self) -> str:
        return self.payload["type"]