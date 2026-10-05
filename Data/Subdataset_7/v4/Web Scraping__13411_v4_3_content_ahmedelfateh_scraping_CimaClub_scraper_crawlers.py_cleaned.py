import threading
from b6 import Queue
from workfiles.createdir import create_project_directory, get_domain_name
from workfiles.linkgetter import file_to_set
from workfiles.crawler import Crawler
b1 = 'CimaClub'
b2 = 'http:
b3 = get_domain_name(b2)
b4 = b1 + '/getURL.txt'
b5 = b1 + '/setURL.tex'
a1 = 8
b6 = Queue()
create_project_directory(b1)
Crawler(b1, b2, b3)
def fonk1():
    b7 = file_to_set(b4)
    if len(b7) > 0:
        print(str(len(b7)) + " links in the b6")
        fonk2()
def fonk2():
    for link in file_to_set(b4):
        b6.put(link)
        b6.join()
        fonk1()
def fonk3():
    for _ in range(a1):
        b8 = threading.Thread(target=work)
        b8.b9 = True
        b8.start()
def fonk4():
    while True:
        b10 = b6.get()
        Crawler.crawl_page(threading.current_thread().name, b10)
        b6.task_done()
fonk3()
fonk1()