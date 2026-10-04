import sys
import wotdapp
def make_mod(username):
    with wotdapp.app.app_context():
        user = wotdapp.models.User.query.filter_by(username=username).first()
        if user is None:
            return f'{username} is not a recognized user'
        if user.isMod:
            return f'{username} is already a moderator'
        user.isMod = True
        wotdapp.db.session.add(user)
        wotdapp.db.session.commit()
        return f'{username} is now a moderator'
def remove_mod(username):
    with wotdapp.app.app_context():
        user = wotdapp.models.User.query.filter_by(username=username).first()
        if user is None:
            return f'{username} is not a recognized user'
        if not user.isMod:
            return f'{username} is not a current moderator'
        user.isMod = False
        wotdapp.db.session.add(user)
        wotdapp.db.session.commit()
        return f'{username} is no longer a moderator'
def replace_db():
    with wotdapp.app.app_context():
        wotdapp.db.drop_all()
        wotdapp.db.create_all()
        return 'Dropped all tables. Created all tables.'
def main():
    if len(sys.argv) < 2:
        print("Usage: script.py <mod|rmmod|newdb> [username]")
        return
    method = sys.argv[1]
    if method == 'mod':
        handle_mod_command()
    elif method == 'rmmod':
        handle_rmmod_command()
    elif method == 'newdb':
        handle_newdb_command()
    else:
        print("Usage: script.py <mod|rmmod|newdb> [username]")
def handle_mod_command():
    if len(sys.argv) < 3:
        print("Usage: script.py mod <username>")
    else:
        print(make_mod(sys.argv[2]))
def handle_rmmod_command():
    if len(sys.argv) < 3:
        print("Usage: script.py rmmod <username>")
    else:
        print(remove_mod(sys.argv[2]))
def handle_newdb_command():
    wipe = input('This will delete all data. Are you sure? (Y/n): ')
    if wipe.lower() == 'y':
        print(replace_db())
    else:
        print('Operation cancelled.')
if __name__ == '__main__':
    main()