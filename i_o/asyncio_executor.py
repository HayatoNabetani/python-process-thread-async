import aiohttp
import asyncio
import time

URLS = [
    f"https://pokeapi.co/api/v2/pokemon/{i}"
    for i in range(1, 11)
]


async def fetch_url_async(url, session):
    async with session.get(url) as response:
        return response.status


async def run_asyncio():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url_async(url, session) for url in URLS]
        return await asyncio.gather(*tasks)

start_time = time.time()
results = asyncio.run(run_asyncio())
end_time = time.time()

print("Results:", results)
print("Time taken:", end_time - start_time)
