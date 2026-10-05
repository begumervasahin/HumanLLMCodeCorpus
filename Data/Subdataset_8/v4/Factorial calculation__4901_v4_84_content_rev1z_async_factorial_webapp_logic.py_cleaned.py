import asyncio
import math
import sys
async def calculate_factorial(n):
    return math.factorial(n)
async def produce_factorial(queue: asyncio.Queue, start: int = 0, finish: int = None):
    loop = asyncio.get_event_loop()
    async def __factorial(n):
        item = await loop.run_in_executor(None, calculate_factorial, n)
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
        sys.stdout.write(f"Current value: {item}\n")
        await asyncio.sleep(0.2)
async def main():
    queue = asyncio.Queue(maxsize=1)
    producer_coroutine = produce_factorial(queue)
    consumer_coroutine = consume_factorial(queue)
    await asyncio.gather(producer_coroutine, consumer_coroutine)
if __name__ == "__main__":
    asyncio.run(main())