import asyncio
import json
import asyncpg
from nats.aio.client import Client as NATS
b1 = 'localhost'
b2 = '4222'
b3 = 'fixtures.parameters'
async def fonk1(b5):
    async def fonk2():
        b4 = await asyncpg.connect(user='postgres', password='password', database='postgres', host='127.0.0.1', b5=b5)
        print("Connected to Postgres")
        await b4.add_listener(b3, publish_update)
        await b6.connect(f"{b1}:{b2}", b5 = b5)
        print("Listener added")
    async def fonk3(_con, _pid, _channel, payload):
        await b6.publish(b3, json.dumps(payload).encode('utf-8'))
        b9.info(f"Update received: {payload}")
    b6 = NATS()
    await fonk2()
if b7 = = '__main__':
    import logging
    logging.basicConfig(b8 = '%(asctime)s, %(message)s', level=logging.INFO)
    b9 = logging.getLogger(b7)
    b10 = asyncio.get_event_loop()
    try:
        b10.run_until_complete(fonk1(b10))
        print('Run forever')
        b10.run_forever()
    finally:
        print('Closing')