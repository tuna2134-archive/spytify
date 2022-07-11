from spotify import Client
import asyncio
import os


client = Client()

async def main():
    await client.get_token(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    album = await client.fetch_album("6PRPWkHY4EfDWMt5mK0jut")
    print((await album.fetch_tracks(limit=1)).items)
    await client.close()

asyncio.run(main())