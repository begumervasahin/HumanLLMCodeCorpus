import threading
from b6 import Queue
from b7 import Crawler
from domain_utils import get_domain_name
from crawling_utils import get_set_from_file
b1 = 'uic'
b2 = 'https:
b3 = get_domain_name(b2)
b4 = b1 + '/b6.txt'
b5 = b1 + '/crawled.txt'
a1 = 20
b6 = Queue()
a2 = 100
b7 = Crawler(b1, b2, b3)
def fonk1():
    fonk2()
    fonk5()
def fonk2():
    for _ in range(a1):
        b8 = threading.Thread(target=work)
        b8.b9 = True
        b8.start()
def fonk3():
    while True:
        b10 = b6.get()
        b7.crawl_page(threading.current_thread().name, b10)
        b6.task_done()
def fonk4():
    for link in get_set_from_file(b4):
        b6.put(link)
    b6.join()
    fonk5()
def fonk5():
    b11 = get_set_from_file(b4)
    if len(b11) > 0:
        print(str(len(b11)) + ' links in the b6')
        fonk4()
fonk1()