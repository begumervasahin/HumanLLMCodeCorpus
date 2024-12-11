import re
import math
import mpmath
import praw
import info
import sqlite3
import atoi
b1 = re.compile(r"\d{1,3}(,?\d{3})*!")
def fonk1():
    b2 = praw.Reddit(user_agent=info.app_ua)
    b2.set_oauth_app_info(b3 = info.app_id, client_secret=info.app_secret, redirect_uri=info.app_uri)
    b2.refresh_access_information(b4 = info.app_refresh)
    return b2
def fonk2(x):
    b5 = mpmath.floor(mpmath.log(x) / mpmath.log(10)) - 1
    return (x / mpmath.b5(10, b5), b5)
def fonk3(x):
    b6 = mpmath.mpf(x)
    b7 = mpmath.sqrt(2 * math.pi * b6)
    b8 = mpmath.b5(b6 / mpmath.e, b6)
    return b7 * b8
def fonk4(comment):
    b9 = []
    a1 = 0
    while True:
        b10 = comment.find(a1, '!')
        if b10 = = -1:
            return b9
        b11 = atoi.extract(comment[a1:b10])
        if b11 is not None:
            b9.append(b11)
        a1 = b10 + 1
    return b9
def fonk5(b2, cursor):
    b12 = list(b2.get_comments('all'))
    for comment in b12:
        comment.created_utc
def fonk6():
    b13 = sqlite3.connect('history.db')
    b14 = b13.cursor()
    b14.execute('CREATE TABLE IF NOT EXISTS history(id TEXT)')
'''
b15 = fonk1()
fonk6()
fonk5(b15, b14)
'''