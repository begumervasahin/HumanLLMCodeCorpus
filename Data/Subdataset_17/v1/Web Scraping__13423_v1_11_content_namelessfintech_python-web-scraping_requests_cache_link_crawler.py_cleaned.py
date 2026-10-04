import re
from urllib import robotparser
from urllib.parse import urljoin
from datetime import timedelta
import requests
import requests_cache
import time
class Downloader:
    def __init__(self, delay=3, user_agent='wswp', proxies=None):
        self.throttle = Throttle(delay)
        self.user_agent = user_agent
        self.proxies = proxies
    def __call__(self, url, num_retries=2):
        result = None
        try:
            self.throttle.wait(url)
            headers = {'User-Agent': self.user_agent}
            response = requests.get(url, headers=headers, proxies=self.proxies)
            if response.status_code == 200:
                result = response.text
            elif num_retries > 0 and 500 <= response.status_code < 600:
                return self.__call__(url, num_retries-1)
        except requests.exceptions.RequestException as e:
            print(f"Download error: {e}")
        return result
class Throttle:
    def __init__(self, delay):
        self.delay = delay
        self.domains = {}
    def wait(self, url):
        domain = re.findall(r':
        last_accessed = self.domains.get(domain)
        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (time.time() - last_accessed)
            if sleep_secs > 0:
                time.sleep(sleep_secs)
        self.domains[domain] = time.time()
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
    D = Downloader(delay=delay, user_agent=user_agent, proxies=proxies)
    while crawl_queue:
        url = crawl_queue.pop()
        if rp.can_fetch(user_agent, url):
            depth = seen.get(url, 0)
            if depth == max_depth:
                print('Skipping %s due to depth' % url)
                continue
            html = D(url, num_retries=num_retries)
            if not html:
                continue
            for link in get_links(html):
                if re.match(link_regex, link):
                    abs_link = urljoin(start_url, link)
                    if abs_link not in seen:
                        seen[abs_link] = depth + 1
                        crawl_queue.append(abs_link)
        else:
            print('Blocked by robots.txt:', url)
if __name__ == '__main__':
    link_crawler('http: