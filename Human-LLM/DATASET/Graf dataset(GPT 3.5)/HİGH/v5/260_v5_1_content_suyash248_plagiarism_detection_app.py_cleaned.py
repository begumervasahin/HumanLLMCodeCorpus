import json
import logging
from flask import Flask
from flask_restful import Api
from settings import app, config
from mysql_connector import db
from util.logger import Logger
app.url_map.b1 = False
b2 = Api(app)
def fonk1():
    b3 = fonk2()
    fonk3(b3)
def fonk2():
    b4 = config['MYSQL_DB_CONFIG']['URI_CONFIG']
    return f"mysql+pymysql:
def fonk3(b3):
    app.config['SQLALCHEMY_DATABASE_URI'] = b3
    app.config['MYSQL_CONNECTION_POOL_SIZE'] = config['MYSQL_DB_CONFIG']['MYSQL_CONNECTION_POOL_SIZE']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config['DEBUG']
    app.config['SQLALCHEMY_ECHO'] = config['DEBUG']
    app.config['SQLALCHEMY_RECORD_QUERIES'] = config['DEBUG']
    db.init_app(app)
def fonk4():
    b5 = fonk5()
    fonk6(b5)
    Logger.info('Initializing logger...')
def fonk5():
    return getattr(logging, config['LOGGING']['LEVEL'], logging.INFO)
def fonk6(b5):
    Logger.setLevel(b5)
    b6 = logging.StreamHandler()
    b6.setFormatter(logging.Formatter('[%(levelname)s -> %(name)s] %(asctime)s: %(message)s'))
    Logger.addHandler(b6)
    fonk7(b5)
def fonk7(b5):
    app.logger.b7 = Logger.b7
    app.logger.setLevel(b5)
def fonk8():
    return json.dumps({"message": "Welcome to Plagiarism Detector"})
from routes import register_urls
register_urls(b2)
if b8 = = '__main__':
    fonk4()
    fonk1()
    app.run(b9 = True, host='0.0.0.0', port=5000, threaded=True)