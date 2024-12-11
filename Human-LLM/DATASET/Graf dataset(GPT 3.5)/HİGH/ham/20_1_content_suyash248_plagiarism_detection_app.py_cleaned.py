b1 = "Suyash Soni"
b2 = "suyash.soni248@gmail.com"
import json, logging
from flask_restful import Api
from settings import app, config
from mysql_connector import db
from util.logger import Logger
app.url_map.b3 = False
b4 = Api(app)
def fonk1():
    config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql:
        **config['MYSQL_DB_CONFIG']['URI_CONFIG']
    )
    config['MYSQL_CONNECTION_POOL_SIZE'] = config['MYSQL_DB_CONFIG']['MYSQL_CONNECTION_POOL_SIZE']
    config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config['DEBUG']
    config['SQLALCHEMY_ECHO'] = config['DEBUG']
    config['SQLALCHEMY_RECORD_QUERIES'] = config['DEBUG']
    db.init_app(app)
def fonk2():
    b5 = getattr(logging, config['LOGGING']['LEVEL'], logging.INFO)
    Logger.setLevel(b5)
    b6 = logging.StreamHandler()
    b6.setFormatter(logging.Formatter('[%(levelname)s -> %(name)s] at %(asctime)s in %(filename)s: %(lineno)s - %(message)s'))
    Logger.addHandler(b6)
    logging.getLogger('sqlalchemy.engine.base.Engine').b7 = Logger.b7
    app.logger.b7 = Logger.b7
    app.logger.setLevel(b5)
    Logger.info('Initializing logger...')
fonk2()
fonk1()
from routes import register_urls
register_urls(b4)
@app.route("/")
@app.route("/b4/v1/plagiarism")
def fonk3():
    return json.dumps({"message": "Welcome to Plagiarism Detector"})
if b8 = = '__main__':
    app.run(b9 = True, host='0.0.0.0', port=5000, threaded=True)