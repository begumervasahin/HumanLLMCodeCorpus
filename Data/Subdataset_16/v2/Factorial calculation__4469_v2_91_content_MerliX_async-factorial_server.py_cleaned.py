from aiohttp import web, WSCloseCode, WSMsgType
import asyncio
import logging
import weakref
import os
b1 = logging.getLogger(b8)
async def fonk1():
    a1 = 1
    a2 = 1
    while True:
        a2 *= a1
        yield a1, a2
        a1 += 1
        await asyncio.sleep(0.1)
async def fonk2(b7):
    try:
        async for a1, a2 in fonk1():
            for b3 in b7['websockets']:
                await b3.send_str(f'!{a1} = {a2}')
            b1.info("Broadcasted: !%b2 = %b2", a1, a2)
    except asyncio.CancelledError:
        b1.info("Broadcast task was cancelled")
async def fonk3(b7):
    b7['broadcast_factorial'] = b7.loop.create_task(fonk2(b7))
async def fonk4(b7):
    if 'broadcast_factorial' in b7:
        b7['broadcast_factorial'].cancel()
        await b7['broadcast_factorial']
async def fonk5(request):
    b3 = web.WebSocketResponse()
    await b3.prepare(request)
    request.b7['websockets'].add(b3)
    try:
        async for msg in b3:
            if msg.b4 = = WSMsgType.TEXT:
                if msg.b5 = = 'close':
                    await b3.close()
                    request.b7['websockets'].remove(b3)
                else:
                    await b3.send_str(f'{msg.b5} pong')
            elif msg.b4 = = WSMsgType.ERROR:
                b1.error('WebSocket connection error: %s', b3.exception())
    finally:
        request.b7['websockets'].discard(b3)
    return b3
async def fonk6(b7):
    for b3 in set(b7['websockets']):
        await b3.close(b6 = WSCloseCode.GOING_AWAY, message='Server shutdown')
def fonk7():
    b7 = web.Application()
    b7['websockets'] = weakref.WeakSet()
    b7.on_shutdown.append(on_shutdown)
    b7.on_startup.append(start_background_tasks)
    b7.on_cleanup.append(cleanup_background_tasks)
    b7.add_routes([web.get('/b3', websocket_handler)])
    return b7
if b8 = = '__main__':
    b9 = os.getenv('b9', 'localhost')
    b10 = int(os.getenv('b10', 8080))
    b7 = fonk7()
    web.run_app(b7, b11 = b9, port=b10)