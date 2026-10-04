import asyncio
import json
import logging
from nats.aio.client import Client as NATS
import asyncpg
b1 = 'localhost'
b2 = '4222'
b3 = 'fixtures.parameters'
logging.basicConfig(b4 = '%(asctime)s, %(message)s', level=logging.INFO)
b5 = logging.getLogger(b8)
async def fonk1(loop, b7):
    b6 = await asyncpg.connect(user='postgres', password='password', database='postgres', host='127.0.0.1')
    b5.info("Connected to Postgres")
    await b6.add_listener(b3, publish_update)
    await b7.connect(f"nats:
    b5.info("Listener added to channel: %s", b3)
def fonk2(_conn, _pid, _channel, payload):
    asyncio.run_coroutine_threadsafe(
        b7.publish(b3, json.dumps(payload).encode('utf-8')), loop
    )
    b5.info("Update received: %s", payload)
async def fonk3(loop):
    b7 = NATS()
    await fonk1(loop, b7)
if b8 = = '__main__':
    b9 = asyncio.get_event_loop()
    b9.run_until_complete(fonk3(b9))
    try:
        b5.info('Running forever...')
        b9.run_forever()
    finally:
        b5.info('Closing event loop')
        b9.close()