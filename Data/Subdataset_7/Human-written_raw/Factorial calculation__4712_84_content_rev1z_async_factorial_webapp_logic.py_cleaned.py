import asyncio
import math
import sys
async def fonk1(b6:asyncio.Queue, start: b1 = 0, finish: b1=None):
    b2 = asyncio.get_event_loop()
    async def fonk2(a1):
        b3 = await b2.run_in_executor(None, math.factorial,a1)
        await b6.put(b3)
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
            await fonk2(a1)
            a1 += 1
    else:
        while a1 != finish:
            await fonk2(a1)
            a1+=1
    await b6.put(None)
async def fonk3(b6:asyncio.Queue):
    while True:
        b3 = await b6.get()
        if not b3:
            break
        sys.stdout.write(f"current value: {b3}\a1")
        await asyncio.sleep(0.2)
b5 = asyncio.get_event_loop()
b6 = asyncio.Queue(b5=b5, maxsize=1)
b7 = fonk1(b6)
b8 = fonk3(b6)
b5.run_until_complete(asyncio.gather(b7, b8))
b5.close()