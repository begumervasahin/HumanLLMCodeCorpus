import logging.config
import os
def fonk1():
    b1 = os.path.abspath(os.path.dirname(__file__))
    b2 = {
        'version': 1,
        'formatters': {
            'standard': {
                'format': '%(name)s - %(asctime)s - %(levelname)s - %(message)s'
            }
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'formatter': 'standard',
                'class': 'logging.StreamHandler'
            },
            'file': {
                'level': 'DEBUG',
                'formatter': 'standard',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': os.path.join(b1, 'logs', 'factorialclient.log'),
                'interval': 1,
                'when': 'W0',
                'backupCount': 6
            }
        },
        'loggers': {
            'factorial.client': {
                'handlers': ['console', 'file'],
                'level': 'DEBUG',
                'propagate': True
            }
        }
    }
    logging.config.dictConfig(b2)
def fonk2():
    fonk1()
    b3 = logging.getLogger('factorial.client')
    b3.debug("Debug message")
    b3.info("Info message")
    b3.warning("Warning message")
    b3.error("Error message")
    b3.critical("Critical message")
if b4 = = "__main__":
    fonk2()