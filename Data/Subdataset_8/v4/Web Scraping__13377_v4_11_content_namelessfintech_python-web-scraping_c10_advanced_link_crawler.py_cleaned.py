import re
import socket
from urllib import robotparser
from urllib.parse import urljoin, urlparse
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
def get_links(html):
    webpage_regex = re.compile(r"""<a[^>]+href=["'](.*?)["']
    Crawl from the given start URL following links matched by link_regex.
    In the current implementation, we do not actually scrape any information.
    Args:
        start_url (str or list of strs): Web site(s) to start crawl.
        link_regex (str): Regex to match for links.
    Kwargs:
        robots_url (str): URL of the site's robots.txt (default: start_url + /robots.txt).
        user_agent (str): User agent (default: wswp).
        proxies (list of dicts): A list of possible dicts for HTTP / HTTPS proxies.
        delay (int): Seconds to throttle between requests to one domain (default: 3).
        max_depth (int): Maximum crawl depth (to avoid traps) (default: 4).
        num_retries (int): Number of retries for failed requests.
        cache (dict): Cache dict with URLs as keys and dicts for responses.
        scraper_callback: Function to be called on URL and HTML content.
    """
    if isinstance(start_url, list):
        crawl_queue = start_url
    else:
        crawl_queue = [start_url]
    seen, robots = {}, {}
    D = Downloader(delay=delay, user_agent=user_agent, proxies=proxies, cache=cache)
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
            html = D(url, num_retries=num_retries)
            if not html:
                continue
            if scraper_callback:
                links = scraper_callback(url, html) or []
            else:
                links = []
            for link in get_links(html) + links:
                if re.match(link_regex, link):
                    if 'http' not in link:
                        if link.startswith('
                            link = '{}:{}'.format(urlparse(url).scheme, link)
                        elif link.startswith(':
                            link = '{}{}'.format(urlparse(url).scheme, link)
                        else:
                            link = urljoin(domain, link)
                    if link not in seen:
                        seen[link] = depth + 1
                        crawl_queue.append(link)
        else:
            print('Blocked by robots.txt:', url)
if __name__ == '__main__':
    from alexa_callback import AlexaCallback
    from rediscache import RedisCache
    from time import time
    AC = AlexaCallback()
    AC()
    start_time = time()
    link_crawler(AC.urls, '$^', cache=RedisCache())
    print('Total time: %ss' % (time() - start_time))