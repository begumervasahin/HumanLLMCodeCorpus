import threading
from queue import Queue
from crawler import Crawler
from domain_utils import get_domain_name
from crawling_utils import get_set_from_file
FOLDER = 'uic'
HOMEPAGE = 'https:
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_PATH = f'{FOLDER}/queue.txt'
CRAWLED_PATH = f'{FOLDER}/crawled.txt'
THREAD_NUMBER = 20
queue = Queue()
counter = 100
crawler = Crawler(FOLDER, HOMEPAGE, DOMAIN_NAME)
def start_crawling():
    create_and_start_workers()
    crawl()
def create_and_start_workers():
    for _ in range(THREAD_NUMBER):
        worker_thread = threading.Thread(target=worker)
        worker_thread.daemon = True
        worker_thread.start()
def worker():
    while True:
        url = queue.get()
        crawler.crawl_page(threading.current_thread().name, url)
        queue.task_done()
def create_jobs():
    for link in get_set_from_file(QUEUE_PATH):
        queue.put(link)
    queue.join()
    crawl()
def crawl():
    queued_links = get_set_from_file(QUEUE_PATH)
    if queued_links:
        print(f'{len(queued_links)} links in the queue')
        create_jobs()
start_crawling()