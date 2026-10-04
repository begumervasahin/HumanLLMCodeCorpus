from math import factorial
import mpmath
import praw, info, sqlite3
import atoi
b1 = re.compile("\d{1,3}(,?\d{3})*!")
def fonk1():
    b2 = praw.Reddit(info.app_ua)
    b2.set_oauth_app_info(info.app_id, info.app_secret, info.app_uri)
    b2.refresh_access_information(info.app_refresh)
    return b2
def fonk2(x):
    b3 = mpmath.floor(mpmath.log(x)/mpmath.log(10)) - 1
    return (x/mpmath.power(10,b3), b3)
def fonk3(x):
    b4 = mpmath.mpf(x)
    b5 = mpmath.sqrt(2 * mpmath.pi * b4)
    b6 = mpmath.power(b4/mpmath.e, b4)
    return b5 * b6
def fonk4(comment):
    b7 = []
    a1 = 0
    while True:
        b8 = comment.find(a1, '!')
        if b9 = = -1:
            return b7
        b10 = atoi.extract(comment[a1:b8])
        if b10 is not None:
            b7.append(b10)
        a1 = b8 + 1
    return b7
def fonk5(b2, b13):
    b11 = list(b2.fonk5('all'))
    for comment in b11:
        comment.created_utc
def fonk6():
    b12 = sqlite3.connect('history.db')
    b13 = b12.cursor()
    b13.execute('CREATE TABLE IF NOT EXISTS history(id TEXT)')
'''b2 = fonk1()
b14 = b2.get_subreddit('all')
b15 = list(b14.fonk5(limit=100))
b15.reverse()
print b15[0].replies'''