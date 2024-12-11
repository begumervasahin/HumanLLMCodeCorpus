import threading
from b5 import Queue
from workfiles.createdir import create_directory
from workfiles.linkgetter import get_domain_name, file_to_set
from workfiles.crawler import Crawler
b1 = 'CimaClub'
b2 = 'http:
b3 = f'{b1}/getURL.txt'
b4 = f'{b1}/setURL.tex'
a1 = 8
b5 = Queue()
def fonk1():
    b6 = file_to_set(b3)
    if len(b6) > 0:
        print(f'{len(b6)} links in the b5.')
        fonk2()
def fonk2():
    for link in file_to_set(b3):
        b5.put(link)
    b5.join()
    fonk1()
def fonk3():
    for _ in range(a1):
        b7 = threading.Thread(target=crawl)
        b7.b8 = True
        b7.start()
def fonk4():
    while True:
        b9 = b5.get()
        Crawler.crawl_page(threading.current_thread().name, b9)
        b5.task_done()
if b10 = = "__main__":
    Crawler(b1, b2, get_domain_name(b2))
    fonk3()
    fonk1()