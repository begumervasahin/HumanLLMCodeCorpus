import asyncio
import json
import logging
from nats.aio.client import Client as NATS
import asyncpg
NATS_HOST = 'localhost'
NATS_PORT = '4222'
CHANNEL = 'fixtures.parameters'
DB_CONFIG = {
    'user': 'postgres',
    'password': 'password',
    'database': 'postgres',
    'host': '127.0.0.1'
}
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
async def connect_to_postgres():
    try:
        connection = await asyncpg.connect(**DB_CONFIG)
        logger.info("Connected to Postgres")
        return connection
    except Exception as e:
        logger.error(f"Failed to connect to Postgres: {e}")
        return None
async def connect_to_nats():
    nc = NATS()
    try:
        await nc.connect(f"{NATS_HOST}:{NATS_PORT}")
        logger.info("Connected to NATS")
        return nc
    except Exception as e:
        logger.error(f"Failed to connect to NATS: {e}")
        return None
async def publish_update(nc, _con, _pid, _channel, payload):
    await nc.publish(CHANNEL, json.dumps(payload).encode('utf-8'))
    logger.info(f"Update received and published to NATS: {payload}")
async def bridge():
    pgconn = await connect_to_postgres()
    if pgconn is None:
        return
    nc = await connect_to_nats()
    if nc is None:
        return
    await pgconn.add_listener(CHANNEL, lambda *args: publish_update(nc, *args))
    logger.info("Listener added to Postgres channel")
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(bridge())
        logger.info('Running forever')
        loop.run_forever()
    except Exception as e:
        logger.error(f"Exception in main loop: {e}")
    finally:
        logger.info('Closing event loop')
        loop.close()