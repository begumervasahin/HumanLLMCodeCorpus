from aiohttp import web, WSCloseCode, WSMsgType
import asyncio
import logging
import weakref
import os
logging.basicConfig(b1 = logging.INFO)
b2 = logging.getLogger(b10)
async def fonk1():
    a1 = 1
    b3 = a1
    while True:
        b3 *= a1
        yield a1, b3
        a1 += 1
        await asyncio.sleep(0.1)
async def fonk2(b9):
    try:
        async for a1, b3 in fonk1():
            b4 = f'!{a1} = {b3}'
            for b5 in b9['websockets']:
                await b5.send_str(b4)
            b2.info("Broadcasted: %s", b4)
    except asyncio.CancelledError:
        b2.info("Broadcast task was cancelled")
async def fonk3(b9):
    b9['broadcast_task'] = b9.loop.create_task(fonk2(b9))
async def fonk4(b9):
    if 'broadcast_task' in b9:
        b9['broadcast_task'].cancel()
        await b9['broadcast_task']
async def fonk5(request):
    b5 = web.WebSocketResponse()
    await b5.prepare(request)
    request.b9['websockets'].add(b5)
    try:
        async for msg in b5:
            if msg.b6 = = WSMsgType.TEXT:
                if msg.b7 = = 'close':
                    await b5.close()
                    request.b9['websockets'].remove(b5)
                else:
                    await b5.send_str(f'{msg.b7} pong')
            elif msg.b6 = = WSMsgType.ERROR:
                b2.exception('WebSocket connection error: %s', b5.exception())
    finally:
        request.b9['websockets'].discard(b5)
    return b5
async def fonk6(b9):
    for b5 in set(b9['websockets']):
        await b5.close(b8 = WSCloseCode.GOING_AWAY, b4='Server shutdown')
def fonk7():
    b9 = web.Application()
    b9['websockets'] = weakref.WeakSet()
    b9.on_shutdown.append(on_shutdown)
    b9.on_startup.append(start_background_tasks)
    b9.on_cleanup.append(cleanup_background_tasks)
    b9.add_routes([web.get('/b5', websocket_handler)])
    return b9
if b10 = = '__main__':
    b11 = os.getenv('b11', 'localhost')
    b12 = int(os.getenv('b12', 8080))
    b9 = fonk7()
    web.run_app(b9, b13 = b11, port=b12)