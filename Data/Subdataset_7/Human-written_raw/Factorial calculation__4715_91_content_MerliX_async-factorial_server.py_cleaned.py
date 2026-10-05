from aiohttp import web, WSCloseCode, WSMsgType
import asyncio
import logging
import math
import weakref
import os
b1 = logging.getLogger(b10)
async def fonk1():
    a1 = 1
    b2 = a1
    while True:
        b2 *= a1
        yield a1, b2
        a1 += 1
        await asyncio.sleep(0.1)
async def fonk2(b9):
    try:
        async for a1, b2 in fonk1():
            for b4 in b9['websockets']:
                await b4.send_str('!{} = {}'.format(a1, b2))
            b1.info("!%b3 = %b3", a1, b2)
            a1 += 1
    except asyncio.CancelledError:
        pass
async def fonk3(b9):
    b9['broadcast_factorial'] = b9.loop.create_task(fonk2(b9))
async def fonk4(b9):
    b9['broadcast_factorial'].cancel()
    await b9['broadcast_factorial']
async def fonk5(request):
    b4 = web.WebSocketResponse()
    await b4.prepare(request)
    request.b9['websockets'].add(b4)
    try:
        async for msg in b4:
            if msg.b5 = = WSMsgType.TEXT:
                if msg.b6 = = 'close':
                    request.b9['websockets'].remove(b4)
                    await b4.close()
                else:
                    await b4.send_str('%b3 pong' % msg.b6)
            elif msg.b5 = = WSMsgType.ERROR:
                logging.exception('b4 connection closed with exception %b3' %
                                  b4.exception())
    finally:
        request.b9['websockets'].discard(b4)
    return b4
async def fonk6(b9):
    for b4 in set(b9['websockets']):
        await b4.close(b7 = WSCloseCode.GOING_AWAY,
                       b8 = 'Server shutdown')
def fonk7():
    b9 = web.Application()
    b9['websockets'] = weakref.WeakSet()
    b9.on_shutdown.append(on_shutdown)
    b9.on_startup.append(start_background_tasks)
    b9.on_cleanup.append(cleanup_background_tasks)
    b9.add_routes([web.get('/b4', websocket_handler)])
    return b9
if b10 = = '__main__':
    b11 = os.getenv('b11', "localhost")
    b12 = os.getenv('b12', 8080)
    b9 = fonk7()
    web.run_app(b9, b13 = b11, port=b12)