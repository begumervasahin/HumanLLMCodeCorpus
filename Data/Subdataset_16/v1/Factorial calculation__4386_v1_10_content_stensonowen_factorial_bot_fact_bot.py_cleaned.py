import re
import mpmath
import praw
import sqlite3
import info
import atoi
from math import factorial
b1 = re.compile(b2"\d{1,3}(,?\d{3})*!")
def fonk1():
    b2 = praw.Reddit(user_agent=info.app_ua)
    b2.set_oauth_app_info(b3 = info.app_id, client_secret=info.app_secret, redirect_uri=info.app_uri)
    b2.refresh_access_information(b4 = info.app_refresh)
    return b2
def fonk2(x):
    b5 = mpmath.floor(mpmath.log(x) / mpmath.log(10)) - 1
    b6 = x / mpmath.power(10, b5)
    return b6, b5
def fonk3(x):
    b7 = mpmath.mpf(x)
    b8 = mpmath.sqrt(2 * mpmath.pi * b7)
    b9 = mpmath.power(b7 / mpmath.e, b7)
    return b8 * b9
def fonk4(comment):
    b10 = []
    a1 = 0
    while True:
        b11 = comment.find('!', a1)
        if b11 = = -1:
            return b10
        b12 = atoi.extract(comment[a1:b11])
        if b12 is not None:
            b10.append(b12)
        a1 = b11 + 1
    return b10
def fonk5(b2, b15):
    b13 = list(b2.subreddit('all').comments(limit=100))
    for comment in b13:
        b15.execute('INSERT INTO history (id) VALUES (?)', (comment.id,))
        b15.connection.commit()
def fonk6():
    b14 = sqlite3.connect('history.db')
    b15 = b14.cursor()
    b15.execute('CREATE TABLE IF NOT EXISTS history (id TEXT PRIMARY KEY)')
    b2 = fonk1()
    fonk5(b2, b15)
if b16 = = "__main__":
    fonk6()