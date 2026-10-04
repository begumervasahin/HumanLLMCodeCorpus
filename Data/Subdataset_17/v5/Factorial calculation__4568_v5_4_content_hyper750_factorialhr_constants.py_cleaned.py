import logging.config
import os
def setup_logging():
    base_project_path = os.path.abspath(os.path.dirname(__file__))
    logging_config = {
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
                'filename': os.path.join(base_project_path, 'logs', 'factorialclient.log'),
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
    logging.config.dictConfig(logging_config)
def main():
    setup_logging()
if __name__ == "__main__":
    main()