import itertools
import urllib.b2
from urllib.error import URLError, HTTPError, ContentTooShortError
def fonk1(url, b1 = 2, user_agent='wswp', charset='utf-8'):
    print('Downloading:', url)
    b2 = urllib.b2.Request(url)
    b2.add_header('User-agent', user_agent)
    try:
        b3 = urllib.b2.urlopen(b2)
        b4 = b3.headers.get_content_charset()
        if not b4:
            b4 = charset
        b5 = b3.read().decode(b4)
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error:', e.reason)
        b5 = None
        if b1 > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return fonk1(url, b1 - 1)
    return b5
def fonk2(url, b6 = 5):
    a1 = 0
    for page in itertools.count(1):
        b7 = '{}{}'.format(url, page)
        b5 = fonk1(b7)
        if b5 is None:
            a1 += 1
            if a1 = = b6:
                break
        else:
            a1 = 0
print(fonk2('http: