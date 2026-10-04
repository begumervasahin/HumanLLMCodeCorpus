import re
import mpmath
import praw
import sqlite3
import info
import atoi
from math import factorial
b1 = re.compile(r"\d{1,3}(,?\d{3})*!")
def fonk1():
    b2 = praw.Reddit(user_agent=info.app_ua)
    b2.set_oauth_app_info(
        b3 = info.app_id,
        b4 = info.app_secret,
        b5 = info.app_uri
    )
    b2.refresh_access_information(b6 = info.app_refresh)
    return b2
def fonk2(number):
    b7 = mpmath.floor(mpmath.log(number) / mpmath.log(10)) - 1
    b8 = number / mpmath.power(10, b7)
    return b8, b7
def fonk3(number):
    b9 = mpmath.mpf(number)
    b10 = mpmath.sqrt(2 * mpmath.pi * b9)
    b11 = mpmath.power(b9 / mpmath.e, b9)
    return b10 * b11
def fonk4(comment):
    b12 = []
    a1 = 0
    while True:
        b13 = comment.find('!', a1)
        if b13 = = -1:
            break
        b14 = atoi.extract(comment[a1:b13])
        if b14 is not None:
            b12.append(b14)
        a1 = b13 + 1
    return b12
def fonk5(b2, b16):
    b15 = b2.subreddit('all').b15(limit=100)
    for comment in b15:
        b16.execute('INSERT INTO history (id) VALUES (?)', (comment.id,))
        b16.connection.commit()
def fonk6():
    with sqlite3.connect('history.db') as connection:
        b16 = connection.b16()
        b16.execute('CREATE TABLE IF NOT EXISTS history (id TEXT PRIMARY KEY)')
        b2 = fonk1()
        fonk5(b2, b16)
if b17 = = "__main__":
    fonk6()