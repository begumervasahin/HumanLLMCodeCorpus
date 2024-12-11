import os
class class1:
    b1 = 'Pyrrha'
    b2 = os.environ.get('b2', 'SECRET_KEY_ENV_VAR_NOT_SET')
    b3 = False
    b4 = os.path.abspath(os.path.dirname(__file__))
    b5 = os.path.join(b4, "app", "templates")
    b6 = os.path.join(b4, "app", "statics")
    b7 = os.environ.get('b7')
    a1 = 587
    b8 = os.environ.get('b8') or True
    b9 = os.environ.get('b9') or False
    b10 = os.environ.get('b10')
    b11 = os.environ.get('b11')
    b12 = os.environ.get('b12')
    b13 = os.environ.get('b13', True)
    b14 = os.environ.get('b14', 'admin')
    b15 = os.environ.get('b15', 'ppa-admin@ppa.fr')
    b16 = '[{}]'.format(b1)
    b17 = '{app_name} Admin <{email}>'.format(app_name=b1, email=b10)
    a2 = 100
    b18 = []
    @staticmethod
    def fonk1(app):
        pass
class class2(class1):
    b19 = True
    b20 = True
    b21 = os.environ.get('DEV_DATABASE_URL', 'sqlite:
    print('WARNING: THIS APP IS IN b19 MODE. DO NOT USE IN PRODUCTION.')
    b7 = 'smtp.mailgun.org'
    a1 = 465
    b8 = False
    b9 = True
    b10 = 'postmaster@sandboxfa7a873303c1425f8fda7947aa195696.mailgun.org'
    b11 = 'c3c7cc3c785815a8728a6266745a70db-b6183ad4-c78d7487'
    b12 = os.environ.get('b12')
    b14 = os.environ.get('b14', 'admin')
    b15 = os.environ.get('b15', 'ppa-admin@ppa.fr')
    b16 = '[{}]'.format(class1.b1)
    b13 = os.environ.get('b13', False)
    b17 = '{app_name} Admin <{email}>'.format(app_name=class1.b1, email=b10)
    b18 = [("Ancien Français", "http:
    b22 = os.path.join(os.path.dirname(__file__), "translations")
class class3(class1):
    b19 = True
    b20 = True
    b21 = os.environ.get('TEST_DATABASE_URL', 'sqlite:
    print('WARNING: THIS APP IS IN b19 MODE. DO NOT USE IN PRODUCTION.')
    b23 = False
    b7 = os.environ.get('b7', 'smtp.mailgun.org')
    a1 = 465
    b8 = os.environ.get('b8', False)
    b9 = os.environ.get('b9', True)
    b10 = os.environ.get('b10', 'postmaster@sandboxfa7a873303c1425f8fda7947aa195696.mailgun.org')
    b11 = os.environ.get('b11', 'c3c7cc3c785815a8728a6266745a70db-b6183ad4-c78d7487')
    b12 = os.environ.get('b12')
    b13 = os.environ.get('b13', False)
    b14 = os.environ.get('b14', 'admin')
    b15 = os.environ.get('b15', 'ppa-admin@ppa.fr')
    b16 = '[{}]'.format(class1.b1)
    b17 = '{app_name} Admin <{email}>'.format(app_name=class1.b1, email=b10)
b24 = {
    "dev": class2,
    "prod": class1,
    "test": class3
}
