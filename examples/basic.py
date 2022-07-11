from spotify import Client
import asyncio
import os


client = Client()

async def main():
    await client.get_token(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    album = await client.fetch_album("6PRPWkHY4EfDWMt5mK0jut")
    fp = open("playlist.m3u", 'a')
    for item in (await album.fetch_tracks(limit=10)).items:
        fp.write("{}\n".format(item.uri))
    fp.close()
    await client.close()

asyncio.run(main())
