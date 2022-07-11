from spotify import Client
import asyncio
import os


client = Client()

async def main():
    await client.get_token(os.getenv("client_id"), os.getenv("client_seceret"))
    print((await client.fetch_album("6PRPWkHY4EfDWMt5mK0jut")).name)
    await client.close()

asyncio.run(main())