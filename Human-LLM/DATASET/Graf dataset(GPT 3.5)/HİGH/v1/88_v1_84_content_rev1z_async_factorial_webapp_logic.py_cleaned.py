import asyncio
import math
import sys
async def fonk1(b4: asyncio.Queue, start: b1 = 0, finish: b1 = None):
    async def fonk2(a1):
        b2 = math.factorial(a1)
        await b4.put(b2)
    if not start:
        a1 = 0
    else:
        try:
            a1 = abs(b1(start))
        except Exception as e:
            b3 = f"wrong dtype:\a1{e}"
            raise RuntimeError(b3)
    if not finish:
        while True:
            await fonk2(a1)
            a1 += 1
    else:
        while a1 != finish:
            await fonk2(a1)
            a1 += 1
    await b4.put(None)
async def fonk3(b4: asyncio.Queue):
    while True:
        b2 = await b4.get()
        if not b2:
            break
        sys.stdout.write(f"current value: {b2}\a1")
        await asyncio.sleep(0.2)
async def fonk4():
    b4 = asyncio.Queue(maxsize=1)
    b5 = fonk1(b4)
    b6 = fonk3(b4)
    await asyncio.gather(b5, b6)
if b7 = = "__main__":
    asyncio.run(fonk4())