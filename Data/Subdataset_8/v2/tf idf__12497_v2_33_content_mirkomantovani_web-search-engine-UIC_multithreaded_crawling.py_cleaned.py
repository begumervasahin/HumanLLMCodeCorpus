import threading
from queue import Queue
from crawler import Crawler
from domain_utils import get_domain_name
from crawling_utils import get_set_from_file
FOLDER = 'uic'
HOMEPAGE = 'https:
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_PATH = FOLDER + '/queue.txt'
CRAWLED_PATH = FOLDER + '/crawled.txt'
THREAD_NUMBER = 20
queue = Queue()
def start_crawling():
    create_workers()
    crawl()
def create_workers():
    for _ in range(THREAD_NUMBER):
        thread = threading.Thread(target=work)
        thread.daemon = True
        thread.start()
def work():
    while True:
        url = queue.get()
        Crawler.crawl_page(threading.current_thread().name, url)
        queue.task_done()
def create_jobs():
    for link in get_set_from_file(QUEUE_PATH):
        queue.put(link)
    queue.join()
    crawl()
def crawl():
    queued_links = get_set_from_file(QUEUE_PATH)
    if len(queued_links) > 0:
        print(f"{len(queued_links)} links in the queue")
        create_jobs()
if __name__ == "__main__":
    start_crawling()