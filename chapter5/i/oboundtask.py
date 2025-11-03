"""I/O Bound tasks"""

import asyncio
import aiohttp


async def download_coroutine(session, url):
    async with session.get(url) as response:
        filename = url.split("/")[-1]
        with open(filename, "wb") as f:
            while True:
                chunk = await response.content.read(1024)
                if not chunk:
                    break
                f.write(chunk)
        
        print(f"Downloaded {url}")


async def download_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(download_coroutine(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks)
    

urls = [
    "https://www.python.org",
    "https://www.google.com",
    "https://www.openai.com",
    "https://www.x.com",
]

asyncio.run(download_all(urls))
