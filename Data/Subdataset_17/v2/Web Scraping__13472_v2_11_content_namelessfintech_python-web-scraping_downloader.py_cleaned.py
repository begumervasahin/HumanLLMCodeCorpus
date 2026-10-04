from random import choice
import requests
from throttle import Throttle
class Downloader:
    def __init__(self, delay=5, user_agent='wswp', proxies=None, cache=None, timeout=60):
        self.throttle = Throttle(delay)
        self.user_agent = user_agent
        self.proxies = proxies if proxies else []
        self.cache = cache if cache is not None else {}
        self.timeout = timeout
        self.num_retries = None
    def __call__(self, url, num_retries=2):
        self.num_retries = num_retries
        result = self.cache.get(url)
        if result:
            print('Loaded from cache:', url)
            if self.num_retries and 500 <= result['code'] < 600:
                result = None
        if not result:
            self.throttle.wait(url)
            proxies = choice(self.proxies) if self.proxies else None
            headers = {'User-Agent': self.user_agent}
            result = self.download(url, headers, proxies)
            self.cache[url] = result
        return result.get('html')
    def download(self, url, headers, proxies):
        print('Downloading:', url)
        try:
            response = requests.get(url, headers=headers, proxies=proxies, timeout=self.timeout)
            html = response.text
            if response.status_code >= 400:
                print('Download error:', response.text)
                html = None
                if self.num_retries and 500 <= response.status_code < 600:
                    self.num_retries -= 1
                    return self.download(url, headers, proxies)
        except requests.exceptions.RequestException as e:
            print('Download error:', e)
            return {'html': None, 'code': 500}
        return {'html': html, 'code': response.status_code}
if __name__ == "__main__":
    cache = {}
    downloader = Downloader(delay=1, user_agent='test_agent', cache=cache)
    html = downloader('http:
    print(html)