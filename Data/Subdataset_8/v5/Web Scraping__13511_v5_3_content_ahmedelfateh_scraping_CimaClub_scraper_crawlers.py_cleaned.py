import threading
from queue import Queue
from workfiles.createdir import create_project_directory, get_domain_name
from workfiles.linkgetter import file_to_set
from workfiles.crawler import Crawler
proj_name = 'CimaClub'
base_url = 'http:
domain_name = get_domain_name(base_url)
queue_file = f'{proj_name}/getURL.txt'
scraped_file = f'{proj_name}/setURL.tex'
num_threads = 8
url_queue = Queue()
create_project_directory(proj_name)
crawler = Crawler(proj_name, base_url, domain_name)
def crawl():
    queued_links = file_to_set(queue_file)
    if queued_links:
        print(f"{len(queued_links)} links in the queue")
        create_jobs()
def create_jobs():
    for link in file_to_set(queue_file):
        url_queue.put(link)
        url_queue.join()
        crawl()
def create_crawlers():
    for _ in range(num_threads):
        thread = threading.Thread(target=work)
        thread.daemon = True
        thread.start()
def work():
    while True:
        url = url_queue.get()
        Crawler.crawl_page(threading.current_thread().name, url)
        url_queue.task_done()
create_crawlers()
crawl()