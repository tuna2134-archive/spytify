from .payloadattr import PayloadAttr


class AlbumTracks(PayloadAttr):
    pass

class Album(PayloadAttr):

    async def fetch_tracks(
        self, *, limit: int | None = 20, store: str | None = None,
        offset: int | None = None
    ) -> AlbumTracks:
        payload = {}
        if limit is not None:
            payload["limit"] = limit
        if store is not None:
            payload["store"] = store
        if offset is not None:
            payload["offset"] = offset
        return AlbumTracks(await self.requester.get_album_tracks(self.id, payload), self.requester)