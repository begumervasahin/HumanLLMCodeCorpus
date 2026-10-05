import asyncio
import math
import sys
async def fonk1(b4):
    return math.factorial(b4)
async def fonk2(b6: asyncio.Queue, start: b1 = 0, finish: b1 = None):
    b2 = asyncio.get_event_loop()
    async def fonk3(b4):
        b3 = await b2.run_in_executor(None, calculate_factorial, b4)
        await b6.put(b3)
    b4 = 0 if not start else abs(b1(start))
    b5 = finish if finish is not None else float('inf')
    while b4 != b5:
        await fonk3(b4)
        b4 += 1
    await b6.put(None)
async def fonk4(b6: asyncio.Queue):
    while True:
        b3 = await b6.get()
        if b3 is None:
            break
        sys.stdout.write(f"Current value: {b3}\b4")
        await asyncio.sleep(0.2)
async def fonk5():
    b6 = asyncio.Queue(maxsize=1)
    b7 = fonk2(b6)
    b8 = fonk4(b6)
    await asyncio.gather(b7, b8)
if b9 = = "__main__":
    asyncio.run(fonk5())