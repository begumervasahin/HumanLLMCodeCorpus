import asyncio
import math
import sys
async def produce_factorial(queue: asyncio.Queue, start: int = 0, finish: int = None):
    _loop = asyncio.get_event_loop()
    async def __factorio(n):
        item = await _loop.run_in_executor(None, math.factorial, n)
        await queue.put(item)
    try:
        n = abs(int(start))
    except ValueError as e:
        raise RuntimeError(f"Invalid start value: {e}")
    if finish is None:
        while True:
            await __factorio(n)
            n += 1
    else:
        finish = abs(int(finish))
        while n < finish:
            await __factorio(n)
            n += 1
    await queue.put(None)
async def consume_factorial(queue: asyncio.Queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        sys.stdout.write(f"Current value: {item}\n")
        await asyncio.sleep(0.2)
async def main():
    queue = asyncio.Queue(maxsize=1)
    producer = produce_factorial(queue, start=0, finish=10)
    consumer = consume_factorial(queue)
    await asyncio.gather(producer, consumer)
if __name__ == "__main__":
    asyncio.run(main())