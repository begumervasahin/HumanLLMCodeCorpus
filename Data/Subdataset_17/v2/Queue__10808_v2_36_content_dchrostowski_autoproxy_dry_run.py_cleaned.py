import random
import time
import threading
from scrapy_autoproxy.config import configuration
from scrapy_autoproxy.storage_manager import StorageManager, Redis
from scrapy_autoproxy.proxy_manager import ProxyManager
redis = Redis(**configuration.redis_config)
redis.flushall()
test_sites = [
    'https:
    'http:
    'http:
    'http:
    'http:
    'http:
    'http:
]
crawl_statuses = [True, False]
successful = {site: 0 for site in test_sites}
failures = {site: 0 for site in test_sites}
def print_scoreboard():
    print("--------------------------------------")
    print("Successes:")
    for site, count in successful.items():
        print(f"{site}: {count}")
    print("--------------------------------------")
    print("Failures:")
    for site, count in failures.items():
        print(f"{site}: {count}")
    print("--------------------------------------")
def count_running_threads():
    return sum(1 for t in threading.enumerate() if t.is_alive())
def worker():
    thread_name = threading.current_thread().getName()
    print(f"{thread_name} starting")
    time.sleep(random.randint(1, 10))
    pm = ProxyManager()
    for _ in range(5):
        url = random.choice(test_sites)
        print(f"{thread_name} crawling {url}")
        proxy = pm.get_proxy(url)
        time.sleep(random.randint(1, 12))
        success = random.choice(crawl_statuses)
        print(f"{thread_name} crawl success={success}")
        if success:
            successful[url] += 1
        else:
            failures[url] += 1
        proxy.callback(success=success)
        time.sleep(random.randint(1, 6))
    print(f"{thread_name} stopping")
def create_workers(num_workers=5):
    workers = []
    for i in range(num_workers):
        worker_name = f"worker_{i}"
        worker_thread = threading.Thread(name=worker_name, target=worker)
        workers.append(worker_thread)
    return workers
workers = create_workers()
def daemon():
    print(threading.current_thread().getName(), 'Starting daemon.')
    for worker_thread in workers:
        worker_thread.start()
    time.sleep(15)
    while True:
        print_scoreboard()
        if count_running_threads() == 1:
            break
        time.sleep(5)
    sm = StorageManager()
    sm.sync_to_db()
    print_scoreboard()
daemon_thread = threading.Thread(name='daemon', target=daemon)
daemon_thread.setDaemon(True)
daemon_thread.start()