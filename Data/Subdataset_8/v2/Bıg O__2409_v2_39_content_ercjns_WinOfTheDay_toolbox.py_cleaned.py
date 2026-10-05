import sys
class User:
    def __init__(self, username, is_mod=False):
        self.username = username
        self.is_mod = is_mod
class Database:
    @staticmethod
    def drop_all_tables():
        print("Dropping all tables")
    @staticmethod
    def create_all_tables():
        print("Creating all tables")
class ApplicationContext:
    @staticmethod
    def get_app_context():
        return None
class UserModel:
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
class MakeModerator:
    @staticmethod
    def make_mod(username):
        user = UserModel.query().filter_by(username=username).first()
        if user is None:
            return f"{username} is not a recognized user"
        if user.is_mod:
            return f"{username} is already a moderator"
        user.is_mod = True
        UserModel.query().add(user)
        return f"{username} is now a moderator"
class RemoveModerator:
    @staticmethod
    def remove_mod(username):
        user = UserModel.query().filter_by(username=username).first()
        if user is None:
            return f"{username} is not a recognized user"
        if not user.is_mod:
            return f"{username} is not a current moderator"
        user.is_mod = False
        UserModel.query().add(user)
        return f"{username} is no longer a moderator"
class ReplaceDatabase:
    @staticmethod
    def replace_db():
        Database.drop_all_tables()
        Database.create_all_tables()
        return "Dropped all tables. Created all tables."
if __name__ == '__main__':
    method = sys.argv[1]
    if method == 'mod':
        print(MakeModerator.make_mod(sys.argv[2]))
    elif method == 'rmmod':
        print(RemoveModerator.remove_mod(sys.argv[2]))
    elif method == 'newdb':
        wipe = input('This will delete all data. Are you sure? (Y/n): ')
        if wipe == 'Y':
            print(ReplaceDatabase.replace_db())