import praw
import sqlite3
import re
import mpmath
import atoi
b1 = re.compile("\d{1,3}(,?\d{3})*!")
def fonk1():
    import info
    b2 = praw.Reddit(user_agent=info.app_ua)
    b2.set_oauth_app_info(b3 = info.app_id, client_secret=info.app_secret, redirect_uri=info.app_uri)
    b2.refresh_access_information(b4 = info.app_refresh)
    return b2
def fonk2(x):
    b5 = mpmath.floor(mpmath.log(x) / mpmath.log(10)) - 1
    return (x / mpmath.power(10, b5), b5)
def fonk3(x):
    b6 = mpmath.mpf(x)
    b7 = mpmath.sqrt(2 * mpmath.pi * b6)
    b8 = mpmath.power(b6 / mpmath.e, b6)
    return b7 * b8
def fonk4(comment):
    b9 = []
    b10 = b1.fonk4(comment)
    for match in b10:
        b11 = atoi.extract(match)
        if b11 is not None:
            b9.append(b11)
    return b9
def fonk5(b2, b15):
    b12 = b2.subreddit('all').comments()
    for comment in b12:
        b13 = comment.b13
        b9 = fonk4(comment.body)
        if b9:
            for number in b9:
                b15.execute('INSERT INTO history (id) VALUES (?)', (number,))
    b15.connection.commit()
def fonk6():
    b14 = sqlite3.connect('history.db')
    b15 = b14.cursor()
    b15.execute('CREATE TABLE IF NOT EXISTS history(id TEXT)')
    b2 = fonk1()
    fonk5(b2, b15)
    b15.close()
    b14.close()
if b16 = = "__main__":
    fonk6()