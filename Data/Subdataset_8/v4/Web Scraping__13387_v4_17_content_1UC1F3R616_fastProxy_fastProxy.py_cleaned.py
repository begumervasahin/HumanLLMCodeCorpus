import fire
import requests
from bs4 import BeautifulSoup as soup
import threading
from queue import Queue
session = requests.session()
response = session.get('https:
parsed_page = soup(response.text, 'html.parser')
table_rows = parsed_page.find_all('tr')
test_url = 'https:
proxies = table_rows[1:]
alive_queue = Queue()
THREAD_COUNT = 100
REQUEST_TIMEOUT = 4
GENERATE_CSV = False
ALL_IPS = False
def alter_globals(thread_count=100, timeout=4, generate_csv=False, all_ips=False):
    global THREAD_COUNT, REQUEST_TIMEOUT, GENERATE_CSV, ALL_IPS
    try:
        THREAD_COUNT = int(thread_count)
        REQUEST_TIMEOUT = int(timeout)
    except ValueError as e:
        print(e)
        return
    if THREAD_COUNT < 0:
        THREAD_COUNT = 1
        print("[!] Negative values are not allowed. Thread count set to 100.")
    elif THREAD_COUNT == 0:
        THREAD_COUNT = 1
    if REQUEST_TIMEOUT < 0:
        print("[!] Negative values are not allowed. Request timeout set to 4 seconds.")
        REQUEST_TIMEOUT = 4
    print("[-] Threads: {}\tRequest Timeout:{}".format(THREAD_COUNT, REQUEST_TIMEOUT))
    GENERATE_CSV = True if generate_csv.lower() in ['true', 'yes', '1'] else False
    ALL_IPS = True if all_ips.lower() in ['true', 'yes', '1'] else False
class AliveIP(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        while True:
            proxy = self.queue.get()
            self.check_proxy(proxy)
            self.queue.task_done()
    def check_proxy(self, proxy):
        try:
            http_proxy = "http:
            https_proxy = "https:
            response = requests.get(test_url, proxies={'http': http_proxy, 'https': https_proxy}, timeout=REQUEST_TIMEOUT)
            if response.status_code == 200:
                alive_queue.put(proxy)
        except Exception:
            pass
def main(proxies=proxies):
    queue = Queue()
    for _ in range(THREAD_COUNT):
        t = AliveIP(queue)
        t.setDaemon(True)
        t.start()
    for proxy in proxies:
        try:
            content = proxy.find_all('td')
            if len(content) is not None:
                ip, port = content[0].get_text(), content[1].get_text()
                proxy_str = '{}:{}'.format(ip, port)
                queue.put(proxy_str)
        except IndexError:
            pass
    queue.join()
    return list(alive_queue.queue)
def generate_csv():
    if ALL_IPS:
        filename = 'all_proxies.csv'
        with open(filename, 'w') as f:
            for line in table_rows:
                content = str(line.getText(separator=';'))
                if 'Date' in content:
                    break
                f.write(content + '\n')
    else:
        filename = 'working_ips.csv'
        with open(filename, 'w') as f:
            for ip in list(alive_queue.queue):
                f.write(ip + '\n')
def printer(ip_list=list(alive_queue.queue)):
    for ip in list(alive_queue.queue):
        print(ip)
def fetch_proxies(thread_count=100, timeout=4, generate_csv=False, all_ips=False):
    global THREAD_COUNT, REQUEST_TIMEOUT, GENERATE_CSV, ALL_IPS
    THREAD_COUNT = thread_count
    REQUEST_TIMEOUT = timeout
    GENERATE_CSV = generate_csv
    ALL_IPS = all_ips
    working_ips = main(proxies=proxies)
    if GENERATE_CSV:
        generate_csv()
    return working_ips
if __name__ == "__main__":
    fire.Fire(alter_globals)
    main(proxies=proxies)
    printer()
    if GENERATE_CSV:
        generate_csv()