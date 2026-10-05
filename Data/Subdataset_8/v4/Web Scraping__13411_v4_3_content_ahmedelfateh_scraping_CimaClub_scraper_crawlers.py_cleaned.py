import threading
from queue import Queue
from workfiles.createdir import create_project_directory, get_domain_name
from workfiles.linkgetter import file_to_set
from workfiles.crawler import Crawler
proj_name = 'CimaClub'
base_url = 'http:
domain_name = get_domain_name(base_url)
queue_file = proj_name + '/getURL.txt'
scraped_file = proj_name + '/setURL.tex'
thread_num = 8
queue = Queue()
create_project_directory(proj_name)
Crawler(proj_name, base_url, domain_name)
def crawl():
    queued_links = file_to_set(queue_file)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + " links in the queue")
        create_jobs()
def create_jobs():
    for link in file_to_set(queue_file):
        queue.put(link)
        queue.join()
        crawl()
def create_crawlers():
    for _ in range(thread_num):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()
def work():
    while True:
        url = queue.get()
        Crawler.crawl_page(threading.current_thread().name, url)
        queue.task_done()
create_crawlers()
crawl()