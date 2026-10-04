import re
import mpmath
import praw
import sqlite3
import info
import atoi
from math import factorial
FACT_PATTERN = re.compile(r"\d{1,3}(,?\d{3})*!")
def login():
    reddit = praw.Reddit(user_agent=info.app_ua)
    reddit.set_oauth_app_info(
        client_id=info.app_id,
        client_secret=info.app_secret,
        redirect_uri=info.app_uri
    )
    reddit.refresh_access_information(refresh_token=info.app_refresh)
    return reddit
def shorten(number):
    exponent = mpmath.floor(mpmath.log(number) / mpmath.log(10)) - 1
    mantissa = number / mpmath.power(10, exponent)
    return mantissa, exponent
def stirling(number):
    n = mpmath.mpf(number)
    coefficient = mpmath.sqrt(2 * mpmath.pi * n)
    exponentiation = mpmath.power(n / mpmath.e, n)
    return coefficient * exponentiation
def find_all_factorials(comment):
    numbers = []
    start = 0
    while True:
        end = comment.find('!', start)
        if end == -1:
            break
        result = atoi.extract(comment[start:end])
        if result is not None:
            numbers.append(result)
        start = end + 1
    return numbers
def get_comments(reddit, cursor):
    comments = reddit.subreddit('all').comments(limit=100)
    for comment in comments:
        cursor.execute('INSERT INTO history (id) VALUES (?)', (comment.id,))
        cursor.connection.commit()
def main():
    with sqlite3.connect('history.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS history (id TEXT PRIMARY KEY)')
        reddit = login()
        get_comments(reddit, cursor)
if __name__ == "__main__":
    main()