import asyncio
import math
import sys
async def fonk1(b6: asyncio.Queue, start: b1 = 0, finish: b1 = None):
    async def fonk2(n: b1):
        b2 = await asyncio.get_event_loop().run_in_executor(None, math.factorial, n)
        await b6.put(b2)
    try:
        b3 = abs(b1(start))
    except ValueError as e:
        raise ValueError(f"Invalid start value: {e}")
    if finish is None:
        while True:
            await fonk2(b3)
            b3 += 1
    else:
        try:
            b4 = abs(b1(finish))
        except ValueError as e:
            raise ValueError(f"Invalid finish value: {e}")
        while b3 < b4:
            await fonk2(b3)
            b3 += 1
    await b6.put(None)
async def fonk3(b6: asyncio.Queue):
    while True:
        b5 = await b6.get()
        if b5 is None:
            break
        sys.stdout.write(f"Current value: {b5}\n")
        await asyncio.sleep(0.2)
async def fonk4():
    b6 = asyncio.Queue(maxsize=1)
    b7 = fonk1(b6, start=0, finish=10)
    b8 = fonk3(b6)
    await asyncio.gather(b7, b8)
if b9 = = "__main__":
    asyncio.run(fonk4())