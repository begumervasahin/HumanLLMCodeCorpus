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
    link_pattern = re.compile(r'<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return link_pattern.findall(html)
def link_crawler(start_url, link_regex, robots_url=None, user_agent='wswp',
                 proxies=None, delay=3, max_depth=4, num_retries=2, expires=timedelta(days=30)):
    crawl_queue = [start_url]
    seen_urls = {}
    requests_cache.install_cache(backend='redis', expire_after=expires)
    if not robots_url:
        robots_url = urljoin(start_url, '/robots.txt')
    robots_parser = get_robots_parser(robots_url)
    downloader = Downloader(delay=delay, user_agent=user_agent, proxies=proxies)
    while crawl_queue:
        url = crawl_queue.pop()
        if robots_parser.can_fetch(user_agent, url):
            current_depth = seen_urls.get(url, 0)
            if current_depth == max_depth:
                print(f'Skipping {url} due to reaching max depth limit.')
                continue
            html_content = downloader(url, num_retries=num_retries)
            if not html_content:
                continue
            for link in get_links(html_content):
                if re.match(link_regex, link):
                    absolute_link = urljoin(start_url, link)
                    if absolute_link not in seen_urls:
                        seen_urls[absolute_link] = current_depth + 1
                        crawl_queue.append(absolute_link)
        else:
            print(f'Blocked by robots.txt: {url}')