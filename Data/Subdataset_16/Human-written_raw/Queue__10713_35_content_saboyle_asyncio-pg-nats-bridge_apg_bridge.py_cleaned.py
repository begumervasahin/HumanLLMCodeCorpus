import asyncio
import json
from nats.aio.client import Client as NATS
import asyncpg
b1 = 'localhost'
b2 = '4222'
b3 = 'fixtures.parameters'
async def fonk1(b5):
    async def fonk2():
        b4 = await asyncpg.connect(user='postgres', password='password', database='postgres', host='127.0.0.1',
                                       b5 = b5)
        print("Connected to Postgres")
        await b4.add_listener(b3, publish_update)
        await b6.connect(f"{b1}:{b2}", b5 = b5)
        print("Listener added")
    def fonk3(_con, _pid, _channel, payload):
        asyncio.run_coroutine_threadsafe(b6.publish(b3, json.dumps(payload).encode('utf-8')), b5)
        b9.info(f"Update received: {payload}")
    b6 = NATS()
    await fonk2()
if b7 = = '__main__':
    import logging
    logging.basicConfig(b8 = '%(asctime)s, %(message)s', level=logging.INFO)
    b9 = logging.getLogger(b7)
    b10 = asyncio.get_event_loop()
    b10.run_until_complete(fonk1(b10))
    try:
        print('Run forever')
        b10.run_forever()
    finally:
        print('Closing')