import praw
import sqlite3
import re
import mpmath
import atoi
fact_ptn = re.compile("\d{1,3}(,?\d{3})*!")
def login():
    import info
    r = praw.Reddit(user_agent=info.app_ua)
    r.set_oauth_app_info(client_id=info.app_id, client_secret=info.app_secret, redirect_uri=info.app_uri)
    r.refresh_access_information(refresh_token=info.app_refresh)
    return r
def shorten(x):
    b = mpmath.floor(mpmath.log(x) / mpmath.log(10)) - 1
    return (x / mpmath.power(10, b), b)
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
def get_comments(r, cur):
    all_comments = r.subreddit('all').comments()
    for comment in all_comments:
        created_utc = comment.created_utc
        numbers = findall(comment.body)
        if numbers:
            for number in numbers:
                cur.execute('INSERT INTO history (id) VALUES (?)', (number,))
    cur.connection.commit()
def main():
    sql = sqlite3.connect('history.db')
    cur = sql.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS history(id TEXT)')
    r = login()
    get_comments(r, cur)
    cur.close()
    sql.close()
if __name__ == "__main__":
    main()