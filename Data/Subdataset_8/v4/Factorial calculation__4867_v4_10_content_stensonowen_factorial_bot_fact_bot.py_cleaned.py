import re
import math
import mpmath
import praw
import info
import sqlite3
import atoi
fact_ptn = re.compile("\d{1,3}(,?\d{3})*!")
def login():
    reddit = praw.Reddit(user_agent=info.app_ua)
    reddit.set_oauth_app_info(client_id=info.app_id, client_secret=info.app_secret, redirect_uri=info.app_uri)
    reddit.refresh_access_information(refresh_token=info.app_refresh)
    return reddit
def shorten(x):
    power = mpmath.floor(mpmath.log(x) / mpmath.log(10)) - 1
    return (x / mpmath.power(10, power), power)
def stirling(x):
    n = mpmath.mpf(x)
    coeff = mpmath.sqrt(2 * math.pi * n)
    expon = mpmath.power(n / mpmath.e, n)
    return coeff * expon
def findall(comment):
    numbers = []
    start = 0
    while True:
        end = comment.find(start, '!')
        if end == -1:
            return numbers
        result = atoi.extract(comment[start:end])
        if result is not None:
            numbers.append(result)
        start = end + 1
    return numbers
def get_comments(reddit, cursor):
    all_comments = list(reddit.get_comments('all'))
    for comment in all_comments:
        comment.created_utc
def main():
    sql = sqlite3.connect('history.db')
    cursor = sql.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS history(id TEXT)')
'''
reddit = login()
main()
get_comments(reddit, cursor)
'''