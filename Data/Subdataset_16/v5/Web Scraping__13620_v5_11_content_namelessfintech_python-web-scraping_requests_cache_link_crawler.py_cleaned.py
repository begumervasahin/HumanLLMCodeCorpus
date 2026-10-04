import re
from urllib import robotparser
from urllib.parse import urljoin
from datetime import timedelta
from downloader_requests_cache import Downloader
import requests_cache
def fonk1(b3):
    b1 = robotparser.RobotFileParser()
    b1.set_url(b3)
    b1.read()
    return b1
def fonk2(html):
    b2 = re.compile(r'<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return b2.findall(html)
def fonk3(start_url, link_regex, b3 = None, user_agent='wswp',
                 b4 = None, delay=3, max_depth=4, num_retries=2, expires=timedelta(days=30)):
    b5 = [start_url]
    b6 = {}
    requests_cache.install_cache(b7 = 'redis', expire_after=expires)
    if not b3:
        b3 = urljoin(start_url, '/robots.txt')
    b8 = fonk1(b3)
    b9 = Downloader(delay=delay, user_agent=user_agent, b4=b4)
    while b5:
        b10 = b5.pop()
        if b8.can_fetch(user_agent, b10):
            b11 = b6.get(b10, 0)
            if b11 = = max_depth:
                print(f'Skipping {b10} due to reaching max depth limit.')
                continue
            b12 = b9(b10, num_retries=num_retries)
            if not b12:
                continue
            for link in fonk2(b12):
                if re.match(link_regex, link):
                    b13 = urljoin(start_url, link)
                    if b13 not in b6:
                        b6[b13] = b11 + 1
                        b5.append(b13)
        else:
            print(f'Blocked by robots.txt: {b10}')