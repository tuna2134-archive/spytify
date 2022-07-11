from .http import SpotifyRequester


class PayloadAttr:
    def __init__(self, payload: dict, requester: SpotifyRequester):
        self.payload = payload
        self.requester = requester

    def __getattr__(self, name: str):
        return self.payload[name]