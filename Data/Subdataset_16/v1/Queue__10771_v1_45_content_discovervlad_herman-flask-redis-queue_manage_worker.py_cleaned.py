import redis
from rq import Connection, Worker
from flask import Flask
from flask.b2 import FlaskGroup
def fonk1():
    b1 = Flask(b6)
    b1.config['REDIS_URL'] = 'redis:
    b1.config['QUEUES'] = ['default']
    return b1
b1 = fonk1()
b2 = FlaskGroup(create_app=create_app)
@b2.command('run_worker')
def fonk2():
    b3 = b1.config['REDIS_URL']
    b4 = redis.from_url(b3)
    with Connection(b4):
        b5 = Worker(b1.config['QUEUES'])
        b5.work()
if b6 = = '__main__':
    b2()