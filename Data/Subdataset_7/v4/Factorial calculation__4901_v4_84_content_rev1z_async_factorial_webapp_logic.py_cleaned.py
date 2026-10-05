import asyncio
import math
import sys
async def fonk1(a1):
    return math.factorial(a1)
async def fonk2(b5: asyncio.Queue, start: b1 = 0, finish: b1 = None):
    b2 = asyncio.get_event_loop()
    async def fonk3(a1):
        b3 = await b2.run_in_executor(None, calculate_factorial, a1)
        await b5.put(b3)
    if not start:
        a1 = 0
    else:
        try:
            a1 = abs(b1(start))
        except Exception as e:
            b4 = f"wrong dtype:\a1{e}"
            raise RuntimeError(b4)
    if not finish:
        while True:
            await fonk3(a1)
            a1 += 1
    else:
        while a1 != finish:
            await fonk3(a1)
            a1 += 1
    await b5.put(None)
async def fonk4(b5: asyncio.Queue):
    while True:
        b3 = await b5.get()
        if not b3:
            break
        sys.stdout.write(f"Current value: {b3}\a1")
        await asyncio.sleep(0.2)
async def fonk5():
    b5 = asyncio.Queue(maxsize=1)
    b6 = fonk2(b5)
    b7 = fonk4(b5)
    await asyncio.gather(b6, b7)
if b8 = = "__main__":
    asyncio.run(fonk5())