import asyncio
import json
import logging
from nats.aio.client import Client as NATS
import asyncpg
b1 = 'localhost'
b2 = '4222'
b3 = 'fixtures.parameters'
logging.basicConfig(b4 = '%(asctime)s, %(message)s', level=logging.INFO)
b5 = logging.getLogger(b9)
async def fonk1():
    b6 = await asyncpg.connect(user='postgres', password='password', database='postgres', host='127.0.0.1')
    b5.info("Connected to Postgres")
    return b6
async def fonk2(loop):
    b7 = NATS()
    await b7.connect(f"nats:
    b5.info("Connected to NATS")
    return b7
def fonk3(b7, loop, _conn, _pid, _channel, payload):
    asyncio.run_coroutine_threadsafe(
        b7.publish(b3, json.dumps(payload).encode('utf-8')), loop
    )
    b5.info("Update received: %s", payload)
async def fonk4(loop, b7, b8):
    await b8.add_listener(b3, lambda conn, pid, channel, payload: fonk3(b7, loop, conn, pid, channel, payload))
    b5.info("Listener added to channel: %s", b3)
async def fonk5(loop):
    b8 = await fonk1()
    b7 = await fonk2(loop)
    await fonk4(loop, b7, b8)
if b9 = = '__main__':
    b10 = asyncio.get_event_loop()
    b10.run_until_complete(fonk5(b10))
    try:
        b5.info('Running forever...')
        b10.run_forever()
    finally:
        b5.info('Closing event loop')
        b10.close()