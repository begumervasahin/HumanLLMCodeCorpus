import re
from urllib import robotparser
from urllib.parse import urljoin
from b7 import Downloader
def fonk1(b3):
    b1 = robotparser.RobotFileParser()
    b1.set_url(b3)
    b1.read()
    return b1
def fonk2(b10):
    b2 = re.compile(r'<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return b2.findall(b10)
def fonk3(start_url, link_regex, b3 = None, user_agent='wswp',
                 b4 = None, delay=3, max_depth=4, num_retries=2, cache={}, scraper_callback=None):
    b5 = [start_url]
    b6 = {}
    if not b3:
        b3 = f'{start_url}/robots.txt'
    b1 = fonk1(b3)
    b7 = Downloader(delay=delay, user_agent=user_agent, b4=b4, cache=cache)
    while b5:
        b8 = b5.pop()
        if not b1.can_fetch(user_agent, b8):
            print(f'Blocked by robots.txt: {b8}')
            continue
        b9 = b6.get(b8, 0)
        if b9 = = max_depth:
            print(f'Skipping {b8} due to b9')
            continue
        b10 = b7(b8, num_retries=num_retries)
        if not b10:
            continue
        if scraper_callback:
            b11 = scraper_callback(b8, b10) or []
        else:
            b11 = []
        for link in fonk2(b10) + b11:
            if re.match(link_regex, link):
                b12 = urljoin(start_url, link)
                if b12 not in b6:
                    b6[b12] = b9 + 1
                    b5.append(b12)