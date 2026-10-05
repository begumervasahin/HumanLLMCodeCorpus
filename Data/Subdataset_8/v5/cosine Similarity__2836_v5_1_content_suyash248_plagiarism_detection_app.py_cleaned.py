import json
import logging
from flask import Flask
from flask_restful import Api
from settings import app, config
from mysql_connector import db
from util.logger import Logger
app.url_map.strict_slashes = False
api = Api(app)
def initialize_sqlalchemy():
    db_uri = build_db_uri()
    configure_sqlalchemy(db_uri)
def build_db_uri():
    uri_config = config['MYSQL_DB_CONFIG']['URI_CONFIG']
    return f"mysql+pymysql:
def configure_sqlalchemy(db_uri):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['MYSQL_CONNECTION_POOL_SIZE'] = config['MYSQL_DB_CONFIG']['MYSQL_CONNECTION_POOL_SIZE']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config['DEBUG']
    app.config['SQLALCHEMY_ECHO'] = config['DEBUG']
    app.config['SQLALCHEMY_RECORD_QUERIES'] = config['DEBUG']
    db.init_app(app)
def init_logger():
    log_level = get_log_level()
    configure_logger(log_level)
    Logger.info('Initializing logger...')
def get_log_level():
    return getattr(logging, config['LOGGING']['LEVEL'], logging.INFO)
def configure_logger(log_level):
    Logger.setLevel(log_level)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter('[%(levelname)s -> %(name)s] %(asctime)s: %(message)s'))
    Logger.addHandler(stream_handler)
    configure_app_logger(log_level)
def configure_app_logger(log_level):
    app.logger.handlers = Logger.handlers
    app.logger.setLevel(log_level)
def index():
    return json.dumps({"message": "Welcome to Plagiarism Detector"})
from routes import register_urls
register_urls(api)
if __name__ == '__main__':
    init_logger()
    initialize_sqlalchemy()
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)