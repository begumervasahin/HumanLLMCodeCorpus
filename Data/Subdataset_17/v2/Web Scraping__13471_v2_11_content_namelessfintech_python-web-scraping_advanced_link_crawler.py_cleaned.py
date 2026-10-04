import re
import time
from urllib import robotparser
from urllib.parse import urljoin
import requests
class Downloader:
    def __init__(self, delay=3, user_agent='wswp', proxies=None, cache=None):
        self.delay = delay
        self.user_agent = user_agent
        self.proxies = proxies
        self.cache = cache if cache is not None else {}
        self.last_accessed = {}
    def __call__(self, url, num_retries=2):
        if url in self.cache:
            return self.cache[url]['html']
        headers = {'User-Agent': self.user_agent}
        for _ in range(num_retries):
            try:
                response = requests.get(url, headers=headers, proxies=self.proxies)
                response.raise_for_status()
                html = response.text
                self.cache[url] = {'html': html}
                return html
            except requests.RequestException as e:
                print(f'Download error: {e}')
                time.sleep(self.delay)
        return None
def get_robots_parser(robots_url):
    rp = robotparser.RobotFileParser()
    rp.set_url(robots_url)
    rp.read()
    return rp
def get_links(html):
    webpage_regex = re.compile(r'<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)
def link_crawler(start_url, link_regex, robots_url=None, user_agent='wswp',
                 proxies=None, delay=3, max_depth=4, num_retries=2, cache=None, scraper_callback=None):
    crawl_queue = [start_url]
    seen = {}
    if not robots_url:
        robots_url = urljoin(start_url, '/robots.txt')
    rp = get_robots_parser(robots_url)
    downloader = Downloader(delay=delay, user_agent=user_agent, proxies=proxies, cache=cache)
    while crawl_queue:
        url = crawl_queue.pop()
        if not rp.can_fetch(user_agent, url):
            print(f'Blocked by robots.txt: {url}')
            continue
        depth = seen.get(url, 0)
        if depth == max_depth:
            print(f'Skipping {url} due to depth')
            continue
        html = downloader(url, num_retries=num_retries)
        if not html:
            continue
        if scraper_callback:
            links = scraper_callback(url, html) or []
        else:
            links = []
        for link in get_links(html) + links:
            if re.match(link_regex, link):
                abs_link = urljoin(start_url, link)
                if abs_link not in seen:
                    seen[abs_link] = depth + 1
                    crawl_queue.append(abs_link)
if __name__ == "__main__":
    start_url = 'http:
    link_regex = r'example.com/.*'
    link_crawler(start_url, link_regex)