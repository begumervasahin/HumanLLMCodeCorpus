import sys
import wotdapp
def make_mod(username):
    with wotdapp.app.app_context():
        u = wotdapp.models.User.query.filter_by(username=username).first()
        if u is None:
            return f'{username} is not a recognized user'
        if u.isMod:
            return f'{username} is already a moderator'
        u.isMod = True
        wotdapp.db.session.add(u)
        wotdapp.db.session.commit()
        return f'{username} is now a moderator'
def remove_mod(username):
    with wotdapp.app.app_context():
        u = wotdapp.models.User.query.filter_by(username=username).first()
        if u is None:
            return f'{username} is not a recognized user'
        if not u.isMod:
            return f'{username} is not a current moderator'
        u.isMod = False
        wotdapp.db.session.add(u)
        wotdapp.db.session.commit()
        return f'{username} is no longer a moderator'
def replace_db():
    with wotdapp.app.app_context():
        wotdapp.db.drop_all()
        wotdapp.db.create_all()
        return 'Dropped all tables. Created all tables.'
if __name__ == '__main__':
    method = sys.argv[1]
    if method == 'mod':
        if len(sys.argv) < 3:
            print("Usage: script.py mod <username>")
        else:
            print(make_mod(sys.argv[2]))
    elif method == 'rmmod':
        if len(sys.argv) < 3:
            print("Usage: script.py rmmod <username>")
        else:
            print(remove_mod(sys.argv[2]))
    elif method == 'newdb':
        wipe = input('This will delete all data. Are you sure? (Y/n): ')
        if wipe == 'Y':
            print(replace_db())
        else:
            print('Operation cancelled.')
    else:
        print("Usage: script.py <mod|rmmod|newdb> [username]")