import asyncio
import json
import asyncpg
from nats.aio.client import Client as NATS
b1 = 'localhost'
b2 = '4222'
b3 = 'fixtures.parameters'
async def fonk1():
    async def fonk2():
        b4 = await asyncpg.connect(user='postgres', password='password', database='postgres', host='127.0.0.1')
        await b4.add_listener(b3, publish_update)
        print("Connected to PostgreSQL and added listener for channel:", b3)
        return b4
    async def fonk3():
        b5 = NATS()
        await b5.connect(f"{b1}:{b2}")
        print("Connected to NATS server")
        return b5
    async def fonk4(_con, _pid, _channel, payload):
        await b5.publish(b3, json.dumps(payload).encode('utf-8'))
        print(f"Update received: {payload}")
    b4 = await fonk2()
    b5 = await fonk3()
async def fonk5():
    await fonk1()
if b6 = = '__main__':
    import logging
    logging.basicConfig(b7 = '%(asctime)s, %(message)s', level=logging.INFO)
    b8 = logging.getLogger(b6)
    try:
        b9 = asyncio.get_event_loop()
        b9.run_until_complete(fonk5())
        print('Running forever')
        b9.run_forever()
    finally:
        print('Closing')