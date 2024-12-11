import threading
from b6 import Queue
from crawler import Crawler
from domain_utils import *
from crawling_utils import *
b1 = 'uic'
b2 = 'https:
b3 = get_domain_name(b2)
b4 = b1 + '/b6.txt'
b5 = b1 + '/crawled.txt'
a1 = 20
b6 = Queue()
a2 = 100
Crawler(b1, b2, b3)
def fonk1():
    fonk2()
    fonk5()
def fonk2():
    for _ in range(a1):
        b7 = threading.Thread(target=work)
        b7.b8 = True
        b7.start()
def fonk3():
    while True:
        b9 = b6.get()
        Crawler.crawl_page(threading.current_thread().name, b9)
        b6.task_done()
def fonk4():
    for link in get_set_from_file(b4):
        b6.put(link)
    b6.join()
    fonk5()
def fonk5():
    b10 = get_set_from_file(b4)
    if len(b10) > 0:
        print(str(len(b10)) + ' links in the b6')
        fonk4()
fonk1()