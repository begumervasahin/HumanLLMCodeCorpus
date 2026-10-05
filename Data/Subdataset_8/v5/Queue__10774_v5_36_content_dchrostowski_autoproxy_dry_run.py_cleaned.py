import random
import time
import threading
from scrapy_autoproxy.config import configuration
from scrapy_autoproxy.storage_manager import StorageManager, Redis
from scrapy_autoproxy.proxy_manager import ProxyManager
redis = Redis(**configuration.redis_config)
redis.flushall()
test_sites = ['https:
'http:
crawl_statuses = [True, False]
successful = {site: 0 for site in test_sites}
failures = {site: 0 for site in test_sites}
def print_scoreboard():
    print("--------------------------------------")
    print("Successes:")
    print(successful)
    print("--------------------------------------")
    print("Failures:")
    print(failures)
    print("--------------------------------------")
def count_running_threads():
    running_count = sum(1 for t in threading.enumerate() if t.is_alive())
    return running_count
def worker():
    thread_name = threading.currentThread().getName()
    print(thread_name, "starting")
    time.sleep(random.randint(1, 10))
    proxy_manager = ProxyManager()
    for _ in range(5):
        url = random.choice(test_sites)
        print(thread_name, "crawling %s" % url)
        proxy = proxy_manager.get_proxy(url)
        time.sleep(random.randint(1, 12))
        success = random.choice(crawl_statuses)
        print(thread_name, "crawl success=%s" % success)
        if success:
            successful[url] += 1
        else:
            failures[url] += 1
        proxy.callback(success=success)
        time.sleep(random.randint(1, 6))
    print(thread_name, "stopping")
def create_workers():
    workers = []
    for i in range(5):
        worker_name = "worker_%s" % i
        worker_thread = threading.Thread(name=worker_name, target=worker)
        workers.append(worker_thread)
    return workers
workers = create_workers()
def daemon():
    daemon_thread_name = threading.currentThread().getName()
    print(daemon_thread_name, 'Starting daemon.')
    for worker_thread in workers:
        worker_thread.start()
    time.sleep(15)
    while True:
        print_scoreboard()
        if count_running_threads() == 1:
            break
        time.sleep(5)
    storage_manager = StorageManager()
    storage_manager.sync_to_db()
    return print_scoreboard()
daemon_thread = threading.Thread(name='daemon', target=daemon)
daemon_thread.setDaemon = True
daemon_thread.start()