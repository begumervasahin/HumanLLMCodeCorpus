import fire
import requests
from bs4 import BeautifulSoup as soup
import threading
from queue import Queue
PROXY_URL = 'https:
TEST_URL = 'https:
THREAD_COUNT = 100
REQUEST_TIMEOUT = 4
proxies = []
alive_queue = Queue()
generate_csv = False
include_all_ips = False
def alter_globals(thread_count=THREAD_COUNT, timeout=REQUEST_TIMEOUT, csv=False, all_ips=False):
    global THREAD_COUNT, REQUEST_TIMEOUT, generate_csv, include_all_ips
    try:
        THREAD_COUNT = int(thread_count)
        REQUEST_TIMEOUT = int(timeout)
    except ValueError as e:
        print(e)
        return
    if THREAD_COUNT < 1:
        THREAD_COUNT = 1
        print("[!] Thread count cannot be less than 1. Defaulting to 1.")
    if REQUEST_TIMEOUT < 0:
        print("[!] Request timeout cannot be negative. Defaulting to 4 seconds.")
        REQUEST_TIMEOUT = 4
    print("[-] Threads: {}\tRequest Timeout: {}".format(THREAD_COUNT, REQUEST_TIMEOUT))
    generate_csv = csv.lower() in ['true', 'yes', '1']
    include_all_ips = all_ips.lower() in ['true', 'yes', '1']
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
            response = requests.get(TEST_URL, proxies={'http': http_proxy, 'https': https_proxy}, timeout=REQUEST_TIMEOUT)
            if response.status_code == 200:
                alive_queue.put(proxy)
        except Exception:
            pass
def fetch_proxies():
    global proxies
    session = requests.session()
    response = session.get(PROXY_URL)
    parsed_page = soup(response.text, 'html.parser')
    table_rows = parsed_page.find_all('tr')
    proxies = table_rows[1:]
def test_proxies():
    queue = Queue()
    for _ in range(THREAD_COUNT):
        t = AliveIP(queue)
        t.setDaemon(True)
        t.start()
    for proxy_row in proxies:
        try:
            ip, port = [data.text for data in proxy_row.find_all('td')[:2]]
            proxy_str = '{}:{}'.format(ip, port)
            queue.put(proxy_str)
        except Exception:
            pass
    queue.join()
def generate_csv_files():
    filename = 'all_proxies.csv' if include_all_ips else 'working_ips.csv'
    with open(filename, 'w') as f:
        for proxy_row in proxies:
            content = str(proxy_row.getText(separator=';'))
            if 'Date' in content:
                break
            f.write(content + '\n')
def print_working_ips():
    for ip in list(alive_queue.queue):
        print(ip)
def main():
    fetch_proxies()
    test_proxies()
    print_working_ips()
    if generate_csv:
        generate_csv_files()
if __name__ == "__main__":
    fire.Fire(alter_globals)
    main()