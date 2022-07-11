from typing import TypedDict


class AccessTokenType(TypedDict):
    access_token: str
    token_type: str
    expires_in: int