import asyncio
import math
import sys
async def calculate_factorial(n):
    return math.factorial(n)
async def produce_factorials(queue: asyncio.Queue, start: int = 0, finish: int = None):
    async def produce(n):
        item = await calculate_factorial(n)
        await queue.put(item)
    n = start if start else 0
    if finish is None:
        while True:
            await produce(n)
            n += 1
    else:
        while n != finish:
            await produce(n)
            n += 1
    await queue.put(None)
async def consume_factorials(queue: asyncio.Queue):
    while True:
        item = await queue.get()
        if not item:
            break
        sys.stdout.write(f"Current value: {item}\n")
        await asyncio.sleep(0.2)
async def main():
    queue = asyncio.Queue(maxsize=1)
    producer_coroutine = produce_factorials(queue)
    consumer_coroutine = consume_factorials(queue)
    await asyncio.gather(producer_coroutine, consumer_coroutine)
if __name__ == "__main__":
    asyncio.run(main())