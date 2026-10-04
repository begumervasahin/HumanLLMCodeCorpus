import redis
from rq import Connection, Worker
from flask import Flask
from flask.cli import FlaskGroup
def create_app():
    app = Flask(__name__)
    app.config['REDIS_URL'] = 'redis:
    app.config['QUEUES'] = ['default']
    return app
app = create_app()
cli = FlaskGroup(create_app=create_app)
@cli.command('run_worker')
def run_worker():
    redis_url = app.config['REDIS_URL']
    redis_connection = redis.from_url(redis_url)
    with Connection(redis_connection):
        worker = Worker(app.config['QUEUES'])
        worker.work()
if __name__ == '__main__':
    cli()