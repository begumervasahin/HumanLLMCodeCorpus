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
    if len(sys.argv) < 2:
        print("Usage: script.py <mod|rmmod|newdb> [username]")
        return
    b3 = sys.argv[1]
    if b3 = = 'mod':
        fonk5()
    elif b3 = = 'rmmod':
        fonk6()
    elif b3 = = 'newdb':
        fonk7()
    else:
        print("Usage: script.py <mod|rmmod|newdb> [username]")
def fonk5():
    if len(sys.argv) < 3:
        print("Usage: script.py mod <username>")
    else:
        print(fonk1(sys.argv[2]))
def fonk6():
    if len(sys.argv) < 3:
        print("Usage: script.py rmmod <username>")
    else:
        print(fonk2(sys.argv[2]))
def fonk7():
    b4 = input('This will delete all data. Are you sure? (Y/n): ')
    if b4.lower() == 'y':
        print(fonk3())
    else:
        print('Operation cancelled.')
if b5 = = '__main__':
    fonk4()