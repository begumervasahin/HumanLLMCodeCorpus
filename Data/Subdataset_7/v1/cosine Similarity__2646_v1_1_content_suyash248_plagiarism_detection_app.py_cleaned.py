import json
import logging
from flask import Flask
from flask_restful import Api
from mysql_connector import db
from routes import register_urls
from settings import config
from util.logger import Logger
b1 = Flask(b8)
b1.url_map.b2 = False
b3 = Api(b1)
def fonk1():
    b4 = 'mysql+pymysql:
        **config['MYSQL_DB_CONFIG']['URI_CONFIG']
    )
    b1.config['SQLALCHEMY_DATABASE_URI'] = b4
    b1.config['MYSQL_CONNECTION_POOL_SIZE'] = config['MYSQL_DB_CONFIG']['MYSQL_CONNECTION_POOL_SIZE']
    b1.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config['DEBUG']
    b1.config['SQLALCHEMY_ECHO'] = config['DEBUG']
    b1.config['SQLALCHEMY_RECORD_QUERIES'] = config['DEBUG']
    db.init_app(b1)
def fonk2():
    b5 = getattr(logging, config['LOGGING']['LEVEL'], logging.INFO)
    Logger.setLevel(b5)
    b6 = logging.StreamHandler()
    b6.setFormatter(logging.Formatter('[%(levelname)s -> %(name)s] at %(asctime)s in %(filename)s: %(lineno)s - %(message)s'))
    Logger.addHandler(b6)
    logging.getLogger('sqlalchemy.engine.base.Engine').b7 = Logger.b7
    b1.logger.b7 = Logger.b7
    b1.logger.setLevel(b5)
    Logger.info('Initializing logger...')
def fonk3():
    return json.dumps({"message": "Welcome to Plagiarism Detector"})
register_urls(b3)
if b8 = = '__main__':
    fonk2()
    fonk1()
    b1.route("/")(index)
    b1.route("/b3/v1/plagiarism")(index)
    b1.run(b9 = True, host='0.0.0.0', port=5000, threaded=True)