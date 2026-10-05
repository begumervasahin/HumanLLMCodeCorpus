import praw
import sqlite3
import re
import mpmath
import atoi
import info
b1 = re.compile("\d{1,3}(,?\d{3})*!")
def fonk1():
    b2 = praw.Reddit(
        b3 = info.app_ua,
        b4 = info.app_id,
        b5 = info.app_secret,
        b6 = info.app_uri
    )
    b2.refresh_access_information(info.app_refresh)
    return b2
def fonk2(x):
    b7 = mpmath.floor(mpmath.log(x) / mpmath.log(10)) - 1
    return x / mpmath.power(10, b7), b7
def fonk3(x):
    b8 = mpmath.mpf(x)
    b9 = mpmath.sqrt(2 * mpmath.pi * b8)
    b10 = mpmath.power(b8 / mpmath.e, b8)
    return b9 * b10
def fonk4(comment):
    b11 = []
    b12 = b1.findall(comment)
    for match in b12:
        b13 = atoi.extract(match)
        if b13 is not None:
            b11.append(b13)
    return b11
def fonk5(b2, b16):
    b14 = b2.subreddit('all').comments()
    for comment in b14:
        b11 = fonk4(comment.body)
        if b11:
            for number in b11:
                b16.execute('INSERT INTO history (id) VALUES (?)', (number,))
    b16.connection.commit()
def fonk6():
    b15 = sqlite3.connect('history.db')
    b16 = b15.b16()
    b16.execute('CREATE TABLE IF NOT EXISTS history(id TEXT)')
    b2 = fonk1()
    fonk5(b2, b16)
    b16.close()
    b15.close()
if b17 = = "__main__":
    fonk6()