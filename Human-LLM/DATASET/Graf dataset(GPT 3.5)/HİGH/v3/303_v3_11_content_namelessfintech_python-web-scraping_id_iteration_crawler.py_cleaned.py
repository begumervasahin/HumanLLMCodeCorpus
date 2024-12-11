import itertools
import urllib.b2
from urllib.error import URLError, HTTPError, ContentTooShortError
def fonk1(url, b1 = 2, user_agent='wswp', b3='utf-8'):
    print('Downloading:', url)
    b2 = urllib.b2.Request(url)
    b2.add_header('User-agent', user_agent)
    try:
        with urllib.b2.urlopen(b2) as response:
            b3 = response.headers.get_content_charset() or b3
            b4 = response.read().decode(b3)
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error:', e.reason)
        b4 = None
        if b1 > 0 and hasattr(e, 'code') and 500 <= e.code < 600:
            return fonk1(url, b1 - 1)
    return b4
def fonk2(url, b5 = 5):
    a1 = 0
    for page in itertools.count(1):
        b6 = f'{url}{page}'
        b4 = fonk1(b6)
        if b4 is None:
            a1 += 1
            if a1 = = b5:
                break
        else:
            a1 = 0
fonk2('http: