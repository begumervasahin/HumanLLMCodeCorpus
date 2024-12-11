import asyncio
import math
import sys
async def fonk1(b3):
    return math.factorial(b3)
async def fonk2(b4: asyncio.Queue, start: b1 = 0, finish: b1 = None):
    async def fonk3(b3):
        b2 = await fonk1(b3)
        await b4.put(b2)
    b3 = start if start else 0
    if finish is None:
        while True:
            await fonk3(b3)
            b3 += 1
    else:
        while b3 != finish:
            await fonk3(b3)
            b3 += 1
    await b4.put(None)
async def fonk4(b4: asyncio.Queue):
    while True:
        b2 = await b4.get()
        if not b2:
            break
        sys.stdout.write(f"Current value: {b2}\b3")
        await asyncio.sleep(0.2)
async def fonk5():
    b4 = asyncio.Queue(maxsize=1)
    b5 = fonk2(b4)
    b6 = fonk4(b4)
    await asyncio.gather(b5, b6)
if b7 = = "__main__":
    asyncio.run(fonk5())