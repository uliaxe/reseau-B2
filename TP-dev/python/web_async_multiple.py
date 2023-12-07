import aiohttp
import aiofiles
import asyncio
import os
import sys

async def fetch_content(session, url):
    try:
        async with session.get(url) as response:
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return await response.text()
    except aiohttp.ClientError as e:
        print(f"Error fetching content from {url}: {e}")
        return None

async def save_to_file(url, content):
    # Remove 'https://' and replace '/' with '_' in the filename
    filename = f"/tmp/web_{url.replace('https://', '').replace('/', '_')}.txt"
    async with aiofiles.open(filename, 'w', encoding='utf-8') as file:
        await file.write(content)
    print(f"Content from {url} saved to {filename}")

async def process_urls_from_file(session, file_path):
    with open(file_path, 'r') as file:
        urls = file.read().splitlines()

    tasks = [fetch_and_save(session, url) for url in urls]
    await asyncio.gather(*tasks)

async def fetch_and_save(session, url):
    content = await fetch_content(session, url)
    if content:
        await save_to_file(url, content)

async def main():
    if len(sys.argv) != 2:
        print("Usage: python web_async_multiple.py <file_path>")
        sys.exit(1)

    input_file = sys.argv[1]
    
    if not os.path.isfile(input_file):
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    async with aiohttp.ClientSession() as session:
        await process_urls_from_file(session, input_file)

if __name__ == "__main__":
    asyncio.run(main())
