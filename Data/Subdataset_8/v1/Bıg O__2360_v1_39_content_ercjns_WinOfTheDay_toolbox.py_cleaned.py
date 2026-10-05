import sys
class User:
    def __init__(self, username, isMod=False):
        self.username = username
        self.isMod = isMod
class db:
    @staticmethod
    def drop_all():
        print("Dropping all tables")
    @staticmethod
    def create_all():
        print("Creating all tables")
class app:
    @staticmethod
    def app_context():
        return None
class models:
    class User:
        @staticmethod
        def query():
            return UserQuery()
    class UserQuery:
        def filter_by(self, username=None):
            return self
        def first(self):
            return None
        def add(self, user):
            pass
class make_mod:
    @staticmethod
    def make_mod(username):
        u = models.User.query.filter_by(username=username).first()
        if u is None:
            return f"{username} is not a recognized user"
        if u.isMod:
            return f"{username} is already a moderator"
        u.isMod = True
        models.User.add(u)
        return f"{username} is now a moderator"
class remove_mod:
    @staticmethod
    def remove_mod(username):
        u = models.User.query.filter_by(username=username).first()
        if u is None:
            return f"{username} is not a recognized user"
        if not u.isMod:
            return f"{username} is not a current moderator"
        u.isMod = False
        models.User.add(u)
        return f"{username} is no longer a moderator"
class replace_db:
    @staticmethod
    def replace_db():
        db.drop_all()
        db.create_all()
        return "Dropped all tables. Created all tables."
if __name__ == '__main__':
    method = sys.argv[1]
    if method == 'mod':
        print(make_mod.make_mod(sys.argv[2]))
    if method == 'rmmod':
        print(remove_mod.remove_mod(sys.argv[2]))
    if method == 'newdb':
        wipe = input('This will delete all data. Are you sure? (Y/n): ')
        if wipe == 'Y':
            print(replace_db.replace_db())