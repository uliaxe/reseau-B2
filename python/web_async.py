import asyncio
import aiohttp
import aiofiles

url = 'https://www.ynov.com'

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def write_to_file():
    async with aiofiles.open('meo.txt', "w") as out:
        await out.write("meoooow")
        await out.flush()

async def main():
    await write_to_file()
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        print(html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
