import asyncio
import math
import sys
async def produce_factorial(queue: asyncio.Queue, start: int = 0, finish: int = None):
    async def __factorial(n):
        item = math.factorial(n)
        await queue.put(item)
    if not start:
        n = 0
    else:
        try:
            n = abs(int(start))
        except Exception as e:
            msg = f"wrong dtype:\n{e}"
            raise RuntimeError(msg)
    if not finish:
        while True:
            await __factorial(n)
            n += 1
    else:
        while n != finish:
            await __factorial(n)
            n += 1
    await queue.put(None)
async def consume_factorial(queue: asyncio.Queue):
    while True:
        item = await queue.get()
        if not item:
            break
        sys.stdout.write(f"current value: {item}\n")
        await asyncio.sleep(0.2)
async def main():
    queue = asyncio.Queue(maxsize=1)
    producer_coro = produce_factorial(queue)
    consumer_coro = consume_factorial(queue)
    await asyncio.gather(producer_coro, consumer_coro)
if __name__ == "__main__":
    asyncio.run(main())