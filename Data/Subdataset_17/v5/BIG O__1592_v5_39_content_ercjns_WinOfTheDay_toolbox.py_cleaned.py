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
def print_usage():
    print("Usage: python script.py <method> [username]")
    print("Methods:")
    print("  mod <username>      Promote user to moderator")
    print("  rmmod <username>    Demote user from moderator")
    print("  newdb               Drop and recreate all tables")
def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    method = sys.argv[1]
    if method == 'mod':
        if len(sys.argv) != 3:
            print_usage()
            sys.exit(1)
        print(make_mod(sys.argv[2]))
    elif method == 'rmmod':
        if len(sys.argv) != 3:
            print_usage()
            sys.exit(1)
        print(remove_mod(sys.argv[2]))
    elif method == 'newdb':
        wipe = input('This will delete all data. Are you sure? (Y/n): ')
        if wipe.lower() == 'y':
            print(replace_db())
        else:
            print("Operation cancelled.")
    else:
        print(f"Unknown method: {method}")
        print_usage()
        sys.exit(1)
if __name__ == '__main__':
    main()