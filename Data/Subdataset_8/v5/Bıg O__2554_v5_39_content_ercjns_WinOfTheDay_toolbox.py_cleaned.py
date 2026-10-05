import sys
import wotdapp
def promote_to_moderator(username):
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
def remove_moderator(username):
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
def reset_database():
    with wotdapp.app.app_context():
        wotdapp.db.drop_all()
        wotdapp.db.create_all()
        return 'Dropped all tables. Created all tables.'
if __name__ == '__main__':
    method = sys.argv[1]
    if method == 'mod':
        print(promote_to_moderator(sys.argv[2]))
    if method == 'rmmod':
        print(remove_moderator(sys.argv[2]))
    if method == 'newdb':
        confirmation = input('This will delete all data. Are you sure? (Y/n): ')
        if confirmation.lower() == 'y':
            print(reset_database())