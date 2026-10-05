import re
import urllib.request
from urllib import robotparser
from urllib.parse import urljoin
from urllib.error import URLError, HTTPError, ContentTooShortError
from lxml.html import fromstring
import time
class Throttle:
    def __init__(self, delay):
        self.delay = delay
        self.domains = {}
    def wait(self, url):
        domain = urllib.parse.urlparse(url).netloc
        last_accessed = self.domains.get(domain)
        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (time.time() - last_accessed)
            if sleep_secs > 0:
                time.sleep(sleep_secs)
        self.domains[domain] = time.time()
def download(url, num_retries=2, user_agent='wswp', charset='utf-8', proxy=None):
    print('Downloading:', url)
    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)
    try:
        if proxy:
            proxy_support = urllib.request.ProxyHandler({'http': proxy})
            opener = urllib.request.build_opener(proxy_support)
            urllib.request.install_opener(opener)
        response = urllib.request.urlopen(request)
        content_type = response.headers.get_content_charset()
        if not content_type:
            content_type = charset
        return response.read().decode(content_type)
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error:', e)
        if num_retries > 0 and hasattr(e, 'code') and 500 <= e.code < 600:
            return download(url, num_retries - 1, user_agent, charset, proxy)
    return None
def get_robots_parser(robots_url):
    rp = robotparser.RobotFileParser()
    rp.set_url(robots_url)
    rp.read()
    return rp
def get_links(html):
    webpage_regex = re.compile(r'<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)
def link_crawler(start_url, link_regex, user_agent='wswp', delay=3, max_depth=4, scrape_callback=None):
    crawl_queue = [start_url]
    seen = {}
    robots_url = f'{start_url}/robots.txt'
    rp = get_robots_parser(robots_url)
    throttle = Throttle(delay)
    while crawl_queue:
        url = crawl_queue.pop()
        if not rp.can_fetch(user_agent, url):
            print('Blocked by robots.txt:', url)
            continue
        depth = seen.get(url, 0)
        if depth == max_depth:
            print('Skipping {} due to depth'.format(url))
            continue
        throttle.wait(url)
        html = download(url, user_agent=user_agent)
        if not html:
            continue
        if scrape_callback:
            scrape_callback(url, html)
        for link in get_links(html):
            if re.match(link_regex, link):
                abs_link = urljoin(start_url, link)
                if abs_link not in seen:
                    seen[abs_link] = depth + 1
                    crawl_queue.append(abs_link)
def simple_scrape_callback(url, html):
    print(f'Scraped URL: {url}')
link_crawler('http: