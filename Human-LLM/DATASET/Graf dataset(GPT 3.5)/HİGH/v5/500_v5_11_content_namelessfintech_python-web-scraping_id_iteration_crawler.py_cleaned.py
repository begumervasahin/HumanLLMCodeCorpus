import itertools
import urllib.b2
from urllib.error import URLError, HTTPError, ContentTooShortError
def fonk1(url, b1 = 2, user_agent='wswp', charset='utf-8'):
    print('Downloading page:', url)
    b2 = urllib.b2.Request(url)
    b2.add_header('User-agent', user_agent)
    try:
        b3 = urllib.b2.urlopen(b2)
        b4 = b3.headers.get_content_charset() or charset
        b5 = b3.read().decode(b4)
        return b5
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error:', e.reason)
        if b1 > 0 and hasattr(e, 'code') and 500 <= e.code < 600:
            return fonk1(url, b1 - 1)
    return None
def fonk2(base_url, b6 = 5):
    a1 = 0
    for page_number in itertools.count(1):
        b7 = f'{base_url}{page_number}'
        b8 = fonk1(b7)
        if b8 is None:
            a1 += 1
            if a1 = = b6:
                print('Maximum consecutive errors reached. Exiting...')
                break
        else:
            a1 = 0
fonk2('http: