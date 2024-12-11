import asyncio
import asyncpg
import json
import logging
from nats.aio.client import Client as NATS
b1 = 'localhost'
a1 = 4222
b2 = 'fixtures.parameters'
async def fonk1(b5):
    b3 = await asyncpg.connect(
        b4 = 'postgres', password='password', database='postgres', host='127.0.0.1', b5=b5
    )
    print("Connected to PostgreSQL")
    await b3.add_listener(b2, publish_update)
    print("Listener added to PostgreSQL")
async def fonk2(_con, _pid, _channel, payload):
    await b9.publish(b2, json.dumps(payload).encode('utf-8'))
    b7.info(f"Update received: {payload}")
async def fonk3(b5):
    await b9.connect(f"{b1}:{a1}", b5 = b5)
    print("Connected to NATS")
    await fonk1(b5)
logging.basicConfig(b6 = '%(asctime)s, %(message)s', level=logging.INFO)
b7 = logging.getLogger(b8)
if b8 = = '__main__':
    try:
        b9 = NATS()
        b10 = asyncio.get_event_loop()
        b10.run_until_complete(fonk3(b10))
        print('Run forever')
        b10.run_forever()
    except KeyboardInterrupt:
        print('KeyboardInterrupt received. Closing...')
    finally:
        print('Closing NATS connection...')
        b10.run_until_complete(b9.close())
        b10.close()