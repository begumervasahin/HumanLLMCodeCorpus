import logging.config
import os
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
b3 = logging.getLogger('factorial.client')
b3.debug('This is a debug message')
b3.info('This is an info message')
b3.warning('This is a warning message')
b3.error('This is an error message')
b3.critical('This is a critical message')