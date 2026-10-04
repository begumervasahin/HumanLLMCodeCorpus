import re
import mpmath
import praw
import sqlite3
import info
import atoi
from math import factorial
fact_ptn = re.compile(r"\d{1,3}(,?\d{3})*!")
def login():
    r = praw.Reddit(user_agent=info.app_ua)
    r.set_oauth_app_info(client_id=info.app_id, client_secret=info.app_secret, redirect_uri=info.app_uri)
    r.refresh_access_information(refresh_token=info.app_refresh)
    return r
def shorten(x):
    exponent = mpmath.floor(mpmath.log(x) / mpmath.log(10)) - 1
    mantissa = x / mpmath.power(10, exponent)
    return mantissa, exponent
def stirling(x):
    n = mpmath.mpf(x)
    coeff = mpmath.sqrt(2 * mpmath.pi * n)
    expon = mpmath.power(n / mpmath.e, n)
    return coeff * expon
def find_all_factorials(comment):
    numbers = []
    start = 0
    while True:
        end = comment.find('!', start)
        if end == -1:
            return numbers
        result = atoi.extract(comment[start:end])
        if result is not None:
            numbers.append(result)
        start = end + 1
    return numbers
def get_comments(r, cur):
    all_comments = list(r.subreddit('all').comments(limit=100))
    for comment in all_comments:
        cur.execute('INSERT INTO history (id) VALUES (?)', (comment.id,))
        cur.connection.commit()
def main():
    sql = sqlite3.connect('history.db')
    cur = sql.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS history (id TEXT PRIMARY KEY)')
    r = login()
    get_comments(r, cur)
if __name__ == "__main__":
    main()