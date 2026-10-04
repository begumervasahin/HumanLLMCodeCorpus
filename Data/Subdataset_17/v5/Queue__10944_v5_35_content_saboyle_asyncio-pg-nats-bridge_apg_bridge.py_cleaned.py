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
async def connect_to_postgres():
    connection = await asyncpg.connect(user='postgres', password='password', database='postgres', host='127.0.0.1')
    logger.info("Connected to Postgres")
    return connection
async def connect_to_nats(loop):
    nc = NATS()
    await nc.connect(f"nats:
    logger.info("Connected to NATS")
    return nc
def publish_update(nc, loop, _conn, _pid, _channel, payload):
    asyncio.run_coroutine_threadsafe(
        nc.publish(CHANNEL, json.dumps(payload).encode('utf-8')), loop
    )
    logger.info("Update received: %s", payload)
async def setup_listener(loop, nc, pgconn):
    await pgconn.add_listener(CHANNEL, lambda conn, pid, channel, payload: publish_update(nc, loop, conn, pid, channel, payload))
    logger.info("Listener added to channel: %s", CHANNEL)
async def bridge(loop):
    pgconn = await connect_to_postgres()
    nc = await connect_to_nats(loop)
    await setup_listener(loop, nc, pgconn)
if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(bridge(event_loop))
    try:
        logger.info('Running forever...')
        event_loop.run_forever()
    finally:
        logger.info('Closing event loop')
        event_loop.close()