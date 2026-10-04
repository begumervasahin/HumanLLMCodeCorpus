import asyncio
import json
from nats.aio.client import Client as NATS
import asyncpg
import logging
NATS_HOST = 'localhost'
NATS_PORT = '4222'
CHANNEL = 'fixtures.parameters'
DB_CONFIG = {
    'user': 'postgres',
    'password': 'password',
    'database': 'postgres',
    'host': '127.0.0.1'
}
logging.basicConfig(format='%(asctime)s, %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
async def bridge(loop):
    nc = NATS()
    async def connect_listener():
        pgconn = await asyncpg.connect(loop=loop, **DB_CONFIG)
        logger.info("Connected to Postgres")
        async def publish_update(_con, _pid, _channel, payload):
            await nc.publish(CHANNEL, json.dumps(payload).encode('utf-8'))
            logger.info(f"Update received: {payload}")
        await pgconn.add_listener(CHANNEL, publish_update)
        logger.info("Listener added to Postgres channel")
        await nc.connect(f"{NATS_HOST}:{NATS_PORT}", loop=loop)
        logger.info("Connected to NATS")
    await connect_listener()
if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(bridge(event_loop))
    try:
        logger.info('Running forever')
        event_loop.run_forever()
    finally:
        logger.info('Closing')
        event_loop.close()