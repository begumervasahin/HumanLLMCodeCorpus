import asyncio
import math
import sys
async def produce_factorial(queue: asyncio.Queue, start: int = 0, finish: int = None):
    loop = asyncio.get_event_loop()
    async def calculate_factorial(n):
        factorial_result = await loop.run_in_executor(None, math.factorial, n)
        await queue.put(factorial_result)
    try:
        current = abs(int(start))
    except ValueError as e:
        raise ValueError(f"Invalid start value: {e}")
    if finish is None:
        while True:
            await calculate_factorial(current)
            current += 1
    else:
        try:
            end = abs(int(finish))
        except ValueError as e:
            raise ValueError(f"Invalid finish value: {e}")
        while current < end:
            await calculate_factorial(current)
            current += 1
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