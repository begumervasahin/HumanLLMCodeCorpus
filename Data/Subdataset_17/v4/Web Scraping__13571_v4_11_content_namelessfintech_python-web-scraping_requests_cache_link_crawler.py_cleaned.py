import re
from urllib import robotparser
from urllib.parse import urljoin
from datetime import timedelta
from downloader_requests_cache import Downloader
import requests_cache
def get_robots_parser(robots_url):
    rp = robotparser.RobotFileParser()
    rp.set_url(robots_url)
    rp.read()
    return rp
def get_links(html):
    webpage_regex = re.compile(r'<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)
def link_crawler(start_url, link_regex, robots_url=None, user_agent='wswp',
                 proxies=None, delay=3, max_depth=4, num_retries=2, expires=timedelta(days=30)):
    crawl_queue = [start_url]
    seen = {}
    requests_cache.install_cache(backend='redis', expire_after=expires)
    if not robots_url:
        robots_url = urljoin(start_url, '/robots.txt')
    rp = get_robots_parser(robots_url)
    downloader = Downloader(delay=delay, user_agent=user_agent, proxies=proxies)
    while crawl_queue:
        url = crawl_queue.pop()
        if rp.can_fetch(user_agent, url):
            depth = seen.get(url, 0)
            if depth == max_depth:
                print(f'Skipping {url} due to depth limit')
                continue
            html = downloader(url, num_retries=num_retries)
            if not html:
                continue
            for link in get_links(html):
                if re.match(link_regex, link):
                    abs_link = urljoin(start_url, link)
                    if abs_link not in seen:
                        seen[abs_link] = depth + 1
                        crawl_queue.append(abs_link)
        else:
            print(f'Blocked by robots.txt: {url}')