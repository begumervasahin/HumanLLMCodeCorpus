import asyncio
import asyncpg
import json
import logging
from nats.aio.client import Client as NATS
NATS_HOST = 'localhost'
NATS_PORT = 4222
CHANNEL = 'fixtures.parameters'
async def connect_to_postgres(loop):
    pgconn = await asyncpg.connect(
        user='postgres', password='password', database='postgres', host='127.0.0.1', loop=loop
    )
    print("Connected to PostgreSQL")
    await pgconn.add_listener(CHANNEL, publish_update)
    print("Listener added to PostgreSQL")
async def publish_update(_con, _pid, _channel, payload):
    await nc.publish(CHANNEL, json.dumps(payload).encode('utf-8'))
    logger.info(f"Update received: {payload}")
async def bridge(loop):
    await nc.connect(f"{NATS_HOST}:{NATS_PORT}", loop=loop)
    print("Connected to NATS")
    await connect_to_postgres(loop)
logging.basicConfig(format='%(asctime)s, %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
if __name__ == '__main__':
    try:
        nc = NATS()
        event_loop = asyncio.get_event_loop()
        event_loop.run_until_complete(bridge(event_loop))
        print('Run forever')
        event_loop.run_forever()
    except KeyboardInterrupt:
        print('KeyboardInterrupt received. Closing...')
    finally:
        print('Closing NATS connection...')
        event_loop.run_until_complete(nc.close())
        event_loop.close()