import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    APP_NAME = 'Pyrrha'
    SECRET_KEY = os.environ.get('SECRET_KEY', 'SECRET_KEY_ENV_VAR_NOT_SET')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    template_folder = os.path.join(basedir, "app", "templates")
    static_folder = os.path.join(basedir, "app", "statics")
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = 587
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or True
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL') or False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
    SEND_MAIL_STATUS = os.environ.get('SEND_MAIL_STATUS', True)
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'admin')
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', 'ppa-admin@ppa.fr')
    EMAIL_SUBJECT_PREFIX = '[{}]'.format(APP_NAME)
    EMAIL_SENDER = '{app_name} Admin <{email}>'.format(app_name=APP_NAME, email=MAIL_USERNAME)
    PAGINATION_DEFAULT_TOKENS = 100
    LEMMATIZERS = []
    @staticmethod
    def init_app(app):
        pass
class DevelopmentConfig(Config):
    DEBUG = True
    ASSETS_DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:
    MAIL_SERVER = 'smtp.mailgun.org'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'postmaster@sandboxfa7a873303c1425f8fda7947aa195696.mailgun.org'
    MAIL_PASSWORD = 'c3c7cc3c785815a8728a6266745a70db-b6183ad4-c78d7487'
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
    SEND_MAIL_STATUS = os.environ.get('SEND_MAIL_STATUS', False)
    EMAIL_SENDER = '{app_name} Admin <{email}>'.format(app_name=Config.APP_NAME, email=MAIL_USERNAME)
    LEMMATIZERS = [
        ("Ancien Français", "http:
    ]
    BABEL_TRANSLATION_DIRECTORIES = os.path.join(os.path.dirname(__file__), "translations")
class TestConfig(Config):
    DEBUG = True
    ASSETS_DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:
    WTF_CSRF_ENABLED = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.mailgun.org'
    MAIL_PORT = 465
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or False
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL') or True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'postmaster@sandboxfa7a873303c1425f8fda7947aa195696.mailgun.org'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'c3c7cc3c785815a8728a6266745a70db-b6183ad4-c78d7487'
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
    SEND_MAIL_STATUS = os.environ.get('SEND_MAIL_STATUS', False)
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'admin')
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', 'ppa-admin@ppa.fr')
    EMAIL_SENDER = '{app_name} Admin <{email}>'.format(app_name=Config.APP_NAME, email=MAIL_USERNAME)
config = {
    "dev": DevelopmentConfig,
    "prod": Config,
    "test": TestConfig
}