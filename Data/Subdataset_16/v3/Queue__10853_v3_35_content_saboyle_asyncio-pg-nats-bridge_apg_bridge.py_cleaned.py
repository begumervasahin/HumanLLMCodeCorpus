import asyncio
import json
import logging
from nats.aio.client import Client as NATS
import asyncpg
b1 = 'localhost'
b2 = '4222'
b3 = 'fixtures.parameters'
b4 = {
    'user': 'postgres',
    'password': 'password',
    'database': 'postgres',
    'host': '127.0.0.1'
}
logging.basicConfig(b5 = '%(asctime)s - %(message)s', level=logging.INFO)
b6 = logging.getLogger(b10)
async def fonk1():
    try:
        b7 = await asyncpg.connect(**b4)
        b6.info("Connected to Postgres")
        return b7
    except Exception as e:
        b6.error(f"Failed to connect to Postgres: {e}")
        return None
async def fonk2():
    b8 = NATS()
    try:
        await b8.connect(f"{b1}:{b2}")
        b6.info("Connected to NATS")
        return b8
    except Exception as e:
        b6.error(f"Failed to connect to NATS: {e}")
        return None
async def fonk3(b8, _con, _pid, _channel, payload):
    await b8.publish(b3, json.dumps(payload).encode('utf-8'))
    b6.info(f"Update received and published to NATS: {payload}")
async def fonk4():
    b9 = await fonk1()
    if b9 is None:
        return
    b8 = await fonk2()
    if b8 is None:
        return
    await b9.add_listener(b3, lambda *args: fonk3(b8, *args))
    b6.info("Listener added to Postgres channel")
if b10 = = '__main__':
    b11 = asyncio.get_event_loop()
    try:
        b11.run_until_complete(fonk4())
        b6.info('Running forever')
        b11.run_forever()
    except Exception as e:
        b6.error(f"Exception in main b11: {e}")
    finally:
        b6.info('Closing event b11')
        b11.close()