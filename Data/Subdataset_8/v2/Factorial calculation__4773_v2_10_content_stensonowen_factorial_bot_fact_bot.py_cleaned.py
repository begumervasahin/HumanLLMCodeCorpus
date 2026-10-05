import praw
import sqlite3
import re
import mpmath
import atoi
fact_ptn = re.compile("\d{1,3}(,?\d{3})*!")
def login():
    import info
    reddit = praw.Reddit(user_agent=info.app_ua)
    reddit.set_oauth_app_info(client_id=info.app_id, client_secret=info.app_secret, redirect_uri=info.app_uri)
    reddit.refresh_access_information(refresh_token=info.app_refresh)
    return reddit
def shorten(x):
    order_of_magnitude = mpmath.floor(mpmath.log(x) / mpmath.log(10)) - 1
    return (x / mpmath.power(10, order_of_magnitude), order_of_magnitude)
def stirling(x):
    n = mpmath.mpf(x)
    coeff = mpmath.sqrt(2 * mpmath.pi * n)
    expon = mpmath.power(n / mpmath.e, n)
    return coeff * expon
def findall(comment):
    numbers = []
    matches = fact_ptn.findall(comment)
    for match in matches:
        result = atoi.extract(match)
        if result is not None:
            numbers.append(result)
    return numbers
def get_comments(reddit, cursor):
    all_comments = reddit.subreddit('all').comments()
    for comment in all_comments:
        created_utc = comment.created_utc
        numbers = findall(comment.body)
        if numbers:
            for number in numbers:
                cursor.execute('INSERT INTO history (id) VALUES (?)', (number,))
    cursor.connection.commit()
def main():
    db_connection = sqlite3.connect('history.db')
    cursor = db_connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS history(id TEXT)')
    reddit_instance = login()
    get_comments(reddit_instance, cursor)
    cursor.close()
    db_connection.close()
if __name__ == "__main__":
    main()