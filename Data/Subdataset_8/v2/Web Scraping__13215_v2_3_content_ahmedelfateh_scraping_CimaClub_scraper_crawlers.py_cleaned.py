import threading
from queue import Queue
from workfiles.createdir import create_directory
from workfiles.linkgetter import get_domain_name, file_to_set
from workfiles.crawler import Crawler
project_name = 'CimaClub'
base_url = 'http:
queue_file = f'{project_name}/getURL.txt'
scraped_file = f'{project_name}/setURL.tex'
num_threads = 8
queue = Queue()
def start_crawling():
    queued_links = file_to_set(queue_file)
    if len(queued_links) > 0:
        print(f'{len(queued_links)} links in the queue.')
        create_jobs()
def create_jobs():
    for link in file_to_set(queue_file):
        queue.put(link)
    queue.join()
    start_crawling()
def create_crawler_threads():
    for _ in range(num_threads):
        thread = threading.Thread(target=crawl)
        thread.daemon = True
        thread.start()
def crawl():
    while True:
        url = queue.get()
        Crawler.crawl_page(threading.current_thread().name, url)
        queue.task_done()
if __name__ == "__main__":
    Crawler(project_name, base_url, get_domain_name(base_url))
    create_crawler_threads()
    start_crawling()