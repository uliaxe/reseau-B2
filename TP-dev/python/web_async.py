import asyncio
from aiohttp import ClientSession

url = 'https://www.ynov.com'
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        print(html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
