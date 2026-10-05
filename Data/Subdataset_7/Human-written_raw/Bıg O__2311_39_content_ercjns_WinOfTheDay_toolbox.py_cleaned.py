import sys
import wotdapp
def fonk1(username):
    with wotdapp.app.app_context():
        b1 = wotdapp.models.User.query.filter_by(username=username).first()
        if b1 is None:
            return '{0} is not a recognized user'.format(username)
        if b1.b2:
            return '{0} is already a moderator'.format(username)
        b1.b2 = True
        wotdapp.db.session.add(b1)
        wotdapp.db.session.commit()
        return '{0} is now a moderator'.format(username)
def fonk2(username):
    with wotdapp.app.app_context():
        b1 = wotdapp.models.User.query.filter_by(username=username).first()
        if b1 is None:
            return '{0} is not a recognized user'.format(username)
        if not b1.b2:
            return '{0} is not a current moderator'.format(username)
        b1.b2 = False
        wotdapp.db.session.add(b1)
        wotdapp.db.session.commit()
        return '{0} is no longer a moderator'.format(username)
def fonk3():
    with wotdapp.app.app_context():
        wotdapp.db.drop_all()
        wotdapp.db.create_all()
        return 'Dropped all tables. Created all tables.'
if b3 = = '__main__':
    b4 = sys.argv[1]
    if b4 = = 'mod':
        print(fonk1(sys.argv[2]))
    if b4 = = 'rmmod':
        print(fonk2(sys.argv[2]))
    if b4 = = 'newdb':
        b5 = raw_input('This will delete all data. Are you sure? (Y/n): ')
        if b5 = = 'Y':
            print(fonk3())