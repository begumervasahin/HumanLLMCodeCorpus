import threading
from queue import Queue
from workfiles.createdir import create_directory
from workfiles.linkgetter import get_domain_name, file_to_set
from workfiles.crawler import Crawler
PROJECT_NAME = 'CimaClub'
BASE_URL = 'http:
QUEUE_FILE = f'{PROJECT_NAME}/getURL.txt'
SCRAPED_FILE = f'{PROJECT_NAME}/setURL.tex'
NUM_THREADS = 8
queue = Queue()
def start_crawling():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(f'{len(queued_links)} links in the queue.')
        create_jobs()
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    start_crawling()
def create_crawler_threads():
    for _ in range(NUM_THREADS):
        thread = threading.Thread(target=crawl)
        thread.daemon = True
        thread.start()
def crawl():
    while True:
        url = queue.get()
        Crawler.crawl_page(threading.current_thread().name, url)
        queue.task_done()
if __name__ == "__main__":
    Crawler(PROJECT_NAME, BASE_URL, get_domain_name(BASE_URL))
    create_crawler_threads()
    start_crawling()