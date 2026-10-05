import re
import socket
from urllib import robotparser
from urllib.parse import urljoin, urlparse
from time import time
from downloader import Downloader
socket.setdefaulttimeout(60)
def get_robots_parser(robots_url):
    try:
        rp = robotparser.RobotFileParser()
        rp.set_url(robots_url)
        rp.read()
        return rp
    except Exception as e:
        print('Error finding robots_url:', robots_url, e)
def extract_links(html):
    link_pattern = re.compile("""<a[^>]+href=["'](.*?)["']
    Crawl from the given start URL following links matched by link_regex. This function does not scrape any information.
    Args:
        start_url (str or list of strs): Website(s) to start crawling
        link_regex (str): Regex pattern to match for links
    Kwargs:
        robots_url (str): URL of the site's robots.txt (default: start_url + /robots.txt)
        user_agent (str): User agent string (default: 'wswp')
        proxies (list of dicts): A list of dictionaries for HTTP/HTTPS proxies
        delay (int): Seconds to throttle between requests to one domain (default: 3)
        max_depth (int): Maximum crawl depth to avoid traps (default: 4)
        num_retries (int): Number of retries if a download fails
        cache (dict): Cache dictionary with URLs as keys and dictionaries for responses (default: {})
        scraper_callback: Function to be called on URL and HTML content
    """
    crawl_queue = start_url if isinstance(start_url, list) else [start_url]
    seen, robots = {}, {}
    downloader = Downloader(delay=delay, user_agent=user_agent, proxies=proxies, cache=cache)
    while crawl_queue:
        url = crawl_queue.pop()
        no_robots = False
        if 'http' not in url:
            continue
        domain = '{}:
        rp = robots.get(domain)
        if not rp and domain not in robots:
            robots_url = '{}/robots.txt'.format(domain)
            rp = get_robots_parser(robots_url)
            if not rp:
                no_robots = True
            robots[domain] = rp
        elif domain in robots:
            no_robots = True
        if no_robots or rp.can_fetch(user_agent, url):
            depth = seen.get(url, 0)
            if depth == max_depth:
                print('Skipping %s due to depth' % url)
                continue
            html = downloader(url, num_retries=num_retries)
            if not html:
                continue
            links = scraper_callback(url, html) if scraper_callback else []
            for link in extract_links(html) + links:
                if re.match(link_regex, link):
                    if 'http' not in link:
                        link = urljoin(domain, link)
                    if link not in seen:
                        seen[link] = depth + 1
                        crawl_queue.append(link)
        else:
            print('Blocked by robots.txt:', url)
if __name__ == '__main__':
    from alexa_callback import AlexaCallback
    from rediscache import RedisCache
    AC = AlexaCallback()
    AC()
    start_time = time()
    link_crawler(AC.urls, '$^', cache=RedisCache())
    print('Total time: %ss' % (time() - start_time))