from spotify import Client
import asyncio
import os


client = Client()

async def main():
    await client.get_token(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    album = await client.fetch_album("6PRPWkHY4EfDWMt5mK0jut")
    m3u = []
    for item in (await album.fetch_tracks(limit=1)).items:
        m3u.append(item.uri)
    with open("music.m3u", "a") as f:
        f.write("\n".join(m for m in m3u))
    await client.close()

asyncio.run(main())
