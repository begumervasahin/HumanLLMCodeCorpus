import urllib.request
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
class ProxyScraper:
    def __init__(self):
        self.ua = UserAgent()
        self.proxies = []
    def fetch_proxies(self):
        proxies_url = 'https:
        request = urllib.request.Request(proxies_url, headers={'User-Agent': self.ua.random})
        response = urllib.request.urlopen(request)
        soup = BeautifulSoup(response, 'html.parser')
        proxy_table = soup.find(id='proxylisttable')
        for row in proxy_table.tbody.find_all('tr'):
            ip = row.find_all('td')[0].string
            port = row.find_all('td')[1].string
            self.proxies.append({'ip': ip, 'port': port})
    def get_random_proxy(self):
        return random.choice(self.proxies)
def main():
    scraper = ProxyScraper()
    scraper.fetch_proxies()
    for request_number in range(1, 100):
        proxy = scraper.get_random_proxy()
        req = urllib.request.Request('https:
        req.set_proxy(proxy['ip'] + ':' + proxy['port'], 'http')
        try:
            with urllib.request.urlopen(req) as response:
                my_ip = response.read().decode('utf8')
                print('My IP:', my_ip)
        except urllib.error.URLError:
            scraper.proxies.remove(proxy)
            print(f'Proxy {proxy["ip"]}:{proxy["port"]} deleted.')
if __name__ == '__main__':
    main()