import asyncio
import time
import httpx

async def fetch(client, n):
    await client.get("https://httpbin.org/delay/2", timeout=10.0)
    return n

async def main():
    async with httpx.AsyncClient() as client:
        results = await asyncio.gather(fetch(client, 1), fetch(client, 2), fetch(client, 3))
    print(results)
    
start = time.perf_counter()
asyncio.run(main())
print(f"took {time.perf_counter() - start:.1f}s")