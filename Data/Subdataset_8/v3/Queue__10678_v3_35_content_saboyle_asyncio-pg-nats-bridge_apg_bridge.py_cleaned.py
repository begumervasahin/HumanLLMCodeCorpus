import asyncio
import json
import asyncpg
from nats.aio.client import Client as NATS
NATS_HOST = 'localhost'
NATS_PORT = '4222'
CHANNEL = 'fixtures.parameters'
async def connect_to_postgres_and_nats():
    async def connect_to_postgres():
        pgconn = await asyncpg.connect(user='postgres', password='password', database='postgres', host='127.0.0.1')
        await pgconn.add_listener(CHANNEL, publish_update)
        print("Connected to PostgreSQL and added listener for channel:", CHANNEL)
        return pgconn
    async def connect_to_nats():
        nc = NATS()
        await nc.connect(f"{NATS_HOST}:{NATS_PORT}")
        print("Connected to NATS server")
        return nc
    async def publish_update(_con, _pid, _channel, payload):
        await nc.publish(CHANNEL, json.dumps(payload).encode('utf-8'))
        print(f"Update received: {payload}")
    pgconn = await connect_to_postgres()
    nc = await connect_to_nats()
async def run_bridge():
    await connect_to_postgres_and_nats()
if __name__ == '__main__':
    import logging
    logging.basicConfig(format='%(asctime)s, %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)
    try:
        event_loop = asyncio.get_event_loop()
        event_loop.run_until_complete(run_bridge())
        print('Running forever')
        event_loop.run_forever()
    finally:
        print('Closing')