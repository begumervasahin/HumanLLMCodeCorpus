import sys
import wotdapp
def fonk1(username):
    with wotdapp.app.app_context():
        b1 = wotdapp.models.User.query.filter_by(username=username).first()
        if b1 is None:
            return f'{username} is not a recognized b1'
        if b1.b2:
            return f'{username} is already a moderator'
        b1.b2 = True
        wotdapp.db.session.add(b1)
        wotdapp.db.session.commit()
        return f'{username} is now a moderator'
def fonk2(username):
    with wotdapp.app.app_context():
        b1 = wotdapp.models.User.query.filter_by(username=username).first()
        if b1 is None:
            return f'{username} is not a recognized b1'
        if not b1.b2:
            return f'{username} is not a current moderator'
        b1.b2 = False
        wotdapp.db.session.add(b1)
        wotdapp.db.session.commit()
        return f'{username} is no longer a moderator'
def fonk3():
    with wotdapp.app.app_context():
        wotdapp.db.drop_all()
        wotdapp.db.create_all()
        return 'Dropped all tables. Created all tables.'
def fonk4():
    print("Usage: python script.py <b3> [username]")
    print("Methods:")
    print("  mod <username>      Promote b1 to moderator")
    print("  rmmod <username>    Demote b1 from moderator")
    print("  newdb               Drop and recreate all tables")
def fonk5():
    if len(sys.argv) < 2:
        fonk4()
        sys.exit(1)
    b3 = sys.argv[1]
    if b3 = = 'mod':
        if len(sys.argv) != 3:
            fonk4()
            sys.exit(1)
        print(fonk1(sys.argv[2]))
    elif b3 = = 'rmmod':
        if len(sys.argv) != 3:
            fonk4()
            sys.exit(1)
        print(fonk2(sys.argv[2]))
    elif b3 = = 'newdb':
        b4 = input('This will delete all data. Are you sure? (Y/n): ')
        if b4.lower() == 'y':
            print(fonk3())
        else:
            print("Operation cancelled.")
    else:
        print(f"Unknown b3: {b3}")
        fonk4()
        sys.exit(1)
if b5 = = '__main__':
    fonk5()