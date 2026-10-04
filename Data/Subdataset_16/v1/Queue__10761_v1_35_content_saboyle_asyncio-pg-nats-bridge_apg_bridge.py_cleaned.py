import asyncio
import json
from nats.aio.client import Client as NATS
import asyncpg
import logging
b1 = 'localhost'
b2 = '4222'
b3 = 'fixtures.parameters'
b4 = {
    'user': 'postgres',
    'password': 'password',
    'database': 'postgres',
    'host': '127.0.0.1'
}
logging.basicConfig(b5 = '%(asctime)s, %(message)s', level=logging.INFO)
b6 = logging.getLogger(b10)
async def fonk1(b9):
    b7 = NATS()
    async def fonk2():
        b8 = await asyncpg.connect(b9=b9, **b4)
        b6.info("Connected to Postgres")
        async def fonk3(_con, _pid, _channel, payload):
            await b7.publish(b3, json.dumps(payload).encode('utf-8'))
            b6.info(f"Update received: {payload}")
        await b8.add_listener(b3, publish_update)
        b6.info("Listener added to Postgres channel")
        await b7.connect(f"{b1}:{b2}", b9 = b9)
        b6.info("Connected to NATS")
    await fonk2()
if b10 = = '__main__':
    b11 = asyncio.get_event_loop()
    b11.run_until_complete(fonk1(b11))
    try:
        b6.info('Running forever')
        b11.run_forever()
    finally:
        b6.info('Closing')
        b11.close()