from math import factorial
import mpmath
import praw, info, sqlite3
import atoi
fact_ptn = re.compile("\d{1,3}(,?\d{3})*!")
def login():
    r = praw.Reddit(info.app_ua)
    r.set_oauth_app_info(info.app_id, info.app_secret, info.app_uri)
    r.refresh_access_information(info.app_refresh)
    return r
def shorten(x):
    b = mpmath.floor(mpmath.log(x)/mpmath.log(10)) - 1
    return (x/mpmath.power(10,b), b)
def stirling(x):
    n = mpmath.mpf(x)
    coeff = mpmath.sqrt(2 * mpmath.pi * n)
    expon = mpmath.power(n/mpmath.e, n)
    return coeff * expon
def findall(comment):
    numbers = []
    start = 0
    while True:
        end = comment.find(start, '!')
        if i == -1:
            return numbers
        result = atoi.extract(comment[start:end])
        if result is not None:
            numbers.append(result)
        start = end + 1
    return numbers
def get_comments(r, cur):
    all_comments = list(r.get_comments('all'))
    for comment in all_comments:
        comment.created_utc
def main():
    sql = sqlite3.connect('history.db')
    cur = sql.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS history(id TEXT)')
'''r = login()
s = r.get_subreddit('all')
p = list(s.get_comments(limit=100))
p.reverse()
print p[0].replies'''