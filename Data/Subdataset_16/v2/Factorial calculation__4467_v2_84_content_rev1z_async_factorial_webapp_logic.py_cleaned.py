import asyncio
import math
import sys
async def fonk1(b7: asyncio.Queue, start: b1 = 0, finish: b1 = None):
    b2 = asyncio.get_event_loop()
    async def fonk2(n):
        b3 = await b2.run_in_executor(None, math.factorial, n)
        await b7.put(b3)
    try:
        b4 = abs(b1(start))
    except ValueError as e:
        raise ValueError(f"Invalid start value: {e}")
    if finish is None:
        while True:
            await fonk2(b4)
            b4 += 1
    else:
        try:
            b5 = abs(b1(finish))
        except ValueError as e:
            raise ValueError(f"Invalid finish value: {e}")
        while b4 < b5:
            await fonk2(b4)
            b4 += 1
    await b7.put(None)
async def fonk3(b7: asyncio.Queue):
    while True:
        b6 = await b7.get()
        if b6 is None:
            break
        sys.stdout.write(f"Current value: {b6}\n")
        await asyncio.sleep(0.2)
async def fonk4():
    b7 = asyncio.Queue(maxsize=1)
    b8 = fonk1(b7, start=0, finish=10)
    b9 = fonk3(b7)
    await asyncio.gather(b8, b9)
if b10 = = "__main__":
    asyncio.run(fonk4())