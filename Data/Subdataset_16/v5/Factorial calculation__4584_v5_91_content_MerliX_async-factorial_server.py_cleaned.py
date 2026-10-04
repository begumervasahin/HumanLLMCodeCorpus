import asyncio
import logging
import weakref
import os
logging.basicConfig(b1 = logging.INFO)
b2 = logging.getLogger(b9)
async def fonk1():
    a1 = 1
    a2 = 1
    while True:
        a2 *= a1
        yield a1, a2
        a1 += 1
        await asyncio.sleep(0.1)
async def fonk2(b8):
    try:
        async for a1, a2 in fonk1():
            b3 = f'!{a1} = {a2}'
            for b4 in b8['websockets']:
                await b4.send_str(b3)
            b2.info("Broadcasted: %s", b3)
    except asyncio.CancelledError:
        b2.info("Broadcast task was cancelled")
async def fonk3(b8):
    b8['broadcast_task'] = b8.loop.create_task(fonk2(b8))
async def fonk4(b8):
    if 'broadcast_task' in b8:
        b8['broadcast_task'].cancel()
        await b8['broadcast_task']
async def fonk5(request):
    b4 = web.WebSocketResponse()
    await b4.prepare(request)
    request.b8['websockets'].add(b4)
    try:
        async for msg in b4:
            if msg.b5 = = WSMsgType.TEXT:
                if msg.b6 = = 'close':
                    await b4.close()
                    request.b8['websockets'].remove(b4)
                else:
                    await b4.send_str(f'{msg.b6} pong')
            elif msg.b5 = = WSMsgType.ERROR:
                b2.exception('WebSocket connection error: %s', b4.exception())
    finally:
        request.b8['websockets'].discard(b4)
    return b4
async def fonk6(b8):
    for b4 in set(b8['websockets']):
        await b4.close(b7 = WSCloseCode.GOING_AWAY, b3='Server shutdown')
def fonk7():
    b8 = web.Application()
    b8['websockets'] = weakref.WeakSet()
    b8.on_shutdown.append(on_shutdown)
    b8.on_startup.append(start_background_tasks)
    b8.on_cleanup.append(cleanup_background_tasks)
    b8.add_routes([web.get('/b4', websocket_handler)])
    return b8
if b9 = = '__main__':
    b10 = os.getenv('b10', 'localhost')
    b11 = int(os.getenv('b11', 8080))
    b8 = fonk7()
    web.run_app(b8, b12 = b10, port=b11)