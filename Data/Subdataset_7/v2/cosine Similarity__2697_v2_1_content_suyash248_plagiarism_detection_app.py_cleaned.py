import json
import logging
from flask import Flask
from flask_restful import Api
from mysql_connector import db
from routes import register_urls
from settings import config
from util.logger import Logger
b1 = Flask(b9)
b1.url_map.b2 = False
b3 = Api(b1)
def fonk1():
    b4 = fonk2()
    fonk3(b4)
def fonk2():
    b5 = config['MYSQL_DB_CONFIG']['URI_CONFIG']
    return 'mysql+pymysql:
def fonk3(b4):
    b1.config['SQLALCHEMY_DATABASE_URI'] = b4
    b1.config['MYSQL_CONNECTION_POOL_SIZE'] = config['MYSQL_DB_CONFIG']['MYSQL_CONNECTION_POOL_SIZE']
    b1.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config['DEBUG']
    b1.config['SQLALCHEMY_ECHO'] = config['DEBUG']
    b1.config['SQLALCHEMY_RECORD_QUERIES'] = config['DEBUG']
    db.init_app(b1)
def fonk4():
    b6 = fonk5()
    fonk6(b6)
    Logger.info('Initializing logger...')
def fonk5():
    return getattr(logging, config['LOGGING']['LEVEL'], logging.INFO)
def fonk6(b6):
    Logger.setLevel(b6)
    b7 = logging.StreamHandler()
    b7.setFormatter(logging.Formatter('[%(levelname)s -> %(name)s] at %(asctime)s in %(filename)s: %(lineno)s - %(message)s'))
    Logger.addHandler(b7)
    fonk7(b6)
def fonk7(b6):
    b1.logger.b8 = Logger.b8
    b1.logger.setLevel(b6)
def fonk8():
    return json.dumps({"message": "Welcome to Plagiarism Detector"})
register_urls(b3)
if b9 = = '__main__':
    fonk4()
    fonk1()
    b1.route("/")(index)
    b1.route("/b3/v1/plagiarism")(index)
    b1.run(b10 = True, host='0.0.0.0', port=5000, threaded=True)