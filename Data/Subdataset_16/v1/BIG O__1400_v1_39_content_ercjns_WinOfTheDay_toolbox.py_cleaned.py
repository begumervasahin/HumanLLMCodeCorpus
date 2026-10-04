import sys
import wotdapp
def fonk1(username):
    with wotdapp.app.app_context():
        b1 = wotdapp.models.User.query.filter_by(username=username).first()
        if b1 is None:
            return f'{username} is not a recognized user'
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
            return f'{username} is not a recognized user'
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
if b3 = = '__main__':
    b4 = sys.argv[1]
    if b4 = = 'mod':
        if len(sys.argv) < 3:
            print("Usage: script.py mod <username>")
        else:
            print(fonk1(sys.argv[2]))
    elif b4 = = 'rmmod':
        if len(sys.argv) < 3:
            print("Usage: script.py rmmod <username>")
        else:
            print(fonk2(sys.argv[2]))
    elif b4 = = 'newdb':
        b5 = input('This will delete all data. Are you sure? (Y/n): ')
        if b5 = = 'Y':
            print(fonk3())
        else:
            print('Operation cancelled.')
    else:
        print("Usage: script.py <mod|rmmod|newdb> [username]")