import multiprocessing
import re
import socket
import threading
import time
from urllib import robotparser
from urllib.parse import urljoin, urlparse
from chp3.downloader import Downloader
from chp4.redis_queue import RedisQueue
SLEEP_TIME = 1
socket.setdefaulttimeout(60)
def get_robots_parser(robots_url):
    " Return the robots parser object using the robots_url "
    try:
        rp = robotparser.RobotFileParser()
        rp.set_url(robots_url)
        rp.read()
        return rp
    except Exception as e:
        print('Error finding robots_url:', robots_url, e)
def clean_link(url, domain, link):
    if link.startswith('
        link = '{}:{}'.format(urlparse(url).scheme, link)
    elif link.startswith(':
        link = '{}{}'.format(urlparse(url).scheme, link)
    else:
        link = urljoin(domain, link)
    return link
def get_links(html, link_regex):
    " Return a list of links (using simple regex matching) from the html content "
    webpage_regex = re.compile("""<a[^>]+href=["'](.*?)["'] Crawl from the given start URLs following links matched by link_regex. In this
        implementation, we do not actually scrape any information.
        args:
            start_url (str or list of strs): web site(s) to start crawl
            link_regex (str): regex to match for links
        kwargs:
            user_agent (str): user agent (default: wswp)
            proxies (list of dicts): a list of possible dicts
                for http / https proxies
                For formatting, see the requests library
            delay (int): seconds to throttle between requests to one domain
                        (default: 3)
            max_depth (int): maximum crawl depth (to avoid traps) (default: 4)
            num_retries (int):
            cache (dict): cache dict with urls as keys
                          and dicts for responses (default: {})
            scraper_callback: function to be called on url and html content
     create a multiprocessing threaded crawler """
    processes = []
    num_procs = kwargs.pop('num_procs')
    if not num_procs:
        num_procs = multiprocessing.cpu_count()
    for _ in range(num_procs):
        proc = multiprocessing.Process(target=threaded_crawler_rq,
                                       args=args, kwargs=kwargs)
        proc.start()
        processes.append(proc)
    for proc in processes:
        proc.join()
if __name__ == '__main__':
    from chp4.alexa_callback import AlexaCallback
    from chp3.rediscache import RedisCache
    import argparse
    parser = argparse.ArgumentParser(description='Multiprocessing threaded link crawler')
    parser.add_argument('max_threads', type=int, help='maximum number of threads',
                        nargs='?', default=5)
    parser.add_argument('num_procs', type=int, help='number of processes',
                        nargs='?', default=None)
    parser.add_argument('url_pattern', type=str, help='regex pattern for url matching',
                        nargs='?', default='$^')
    par_args = parser.parse_args()
    AC = AlexaCallback()
    AC()
    start_time = time.time()
    mp_threaded_crawler(AC.urls, par_args.url_pattern, cache=RedisCache(),
                        num_procs=par_args.num_procs, max_threads=par_args.max_threads)
    print('Total time: %ss' % (time.time() - start_time))