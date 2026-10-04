from aiohttp import web, WSCloseCode, WSMsgType
import asyncio
import logging
import weakref
import os
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
async def factorial_producer():
    number = 1
    factorial = 1
    while True:
        factorial *= number
        yield number, factorial
        number += 1
        await asyncio.sleep(0.1)
async def broadcast_factorials(app):
    try:
        async for number, factorial in factorial_producer():
            for ws in app['websockets']:
                await ws.send_str(f'!{number} = {factorial}')
            logger.info("Broadcasted: !%d = %d", number, factorial)
    except asyncio.CancelledError:
        logger.info("Broadcast task was cancelled")
async def start_background_tasks(app):
    app['broadcast_task'] = app.loop.create_task(broadcast_factorials(app))
async def cleanup_background_tasks(app):
    if 'broadcast_task' in app:
        app['broadcast_task'].cancel()
        await app['broadcast_task']
async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    request.app['websockets'].add(ws)
    try:
        async for msg in ws:
            if msg.type == WSMsgType.TEXT:
                if msg.data == 'close':
                    await ws.close()
                else:
                    await ws.send_str(f'{msg.data} pong')
            elif msg.type == WSMsgType.ERROR:
                logger.error('WebSocket connection error: %s', ws.exception())
    finally:
        request.app['websockets'].discard(ws)
    return ws
async def on_shutdown(app):
    for ws in set(app['websockets']):
        await ws.close(code=WSCloseCode.GOING_AWAY, message='Server shutdown')
def create_app():
    app = web.Application()
    app['websockets'] = weakref.WeakSet()
    app.on_shutdown.append(on_shutdown)
    app.on_startup.append(start_background_tasks)
    app.on_cleanup.append(cleanup_background_tasks)
    app.add_routes([web.get('/ws', websocket_handler)])
    return app
if __name__ == '__main__':
    HOST = os.getenv('HOST', 'localhost')
    PORT = int(os.getenv('PORT', 8080))
    app = create_app()
    web.run_app(app, host=HOST, port=PORT)