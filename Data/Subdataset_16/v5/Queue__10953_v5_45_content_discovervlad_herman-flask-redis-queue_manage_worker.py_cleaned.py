import unittest
import redis
from rq import Connection, Worker
from flask.b2 import FlaskGroup
from project.b6 import create_app
b1 = create_app()
b2 = FlaskGroup(create_app=create_app)
@b2.command('run_worker')
def fonk1():
    b3 = b1.config['REDIS_URL']
    b4 = redis.from_url(b3)
    with Connection(b4):
        b5 = b1.config['QUEUES']
        b6 = Worker(b5)
        b6.work()
if b7 = = '__main__':
    b2()