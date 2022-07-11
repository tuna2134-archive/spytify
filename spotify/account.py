from .types import access_token


class Account:
    def __init__(self, payload: access_token.AccessTokenType):
        self.payload = payload

    @property
    def access_token(self) -> str:
        return self.payload["access_token"]

    @property
    def token_type(self) -> str:
        return self.payload["token_type"]

    @property
    def expires_in(self) -> int:
        return self.payload["expires_in"]