import asyncio
import json
import logging
from nats.aio.client import Client as NATS
import asyncpg
NATS_HOST = 'localhost'
NATS_PORT = '4222'
CHANNEL = 'fixtures.parameters'
logging.basicConfig(format='%(asctime)s, %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
async def connect_listener(loop, nc):
    pgconn = await asyncpg.connect(user='postgres', password='password', database='postgres', host='127.0.0.1')
    logger.info("Connected to Postgres")
    await pgconn.add_listener(CHANNEL, publish_update)
    await nc.connect(f"nats:
    logger.info("Listener added to channel: %s", CHANNEL)
def publish_update(_conn, _pid, _channel, payload):
    asyncio.run_coroutine_threadsafe(
        nc.publish(CHANNEL, json.dumps(payload).encode('utf-8')), loop
    )
    logger.info("Update received: %s", payload)
async def bridge(loop):
    nc = NATS()
    await connect_listener(loop, nc)
if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(bridge(event_loop))
    try:
        logger.info('Running forever...')
        event_loop.run_forever()
    finally:
        logger.info('Closing event loop')
        event_loop.close()