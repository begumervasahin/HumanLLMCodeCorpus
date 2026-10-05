import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
import time
ua = UserAgent()
def get_proxies():
    proxies = []
    url = 'https:
    headers = {'User-Agent': ua.random}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.find(id='proxylisttable').find_all('tr')
    for row in rows:
        columns = row.find_all('td')
        proxies.append({
            'ip': columns[0].text,
            'port': columns[1].text
        })
    return proxies
def main():
    proxies = get_proxies()
    proxy_index = random.randint(0, len(proxies) - 1)
    proxy = proxies[proxy_index]
    print("Using proxy:", proxy['ip'] + ':' + proxy['port'])
    for n in range(1, 101):
        if n % 10 == 0:
            proxy_index = random.randint(0, len(proxies) - 1)
            proxy = proxies[proxy_index]
            print("Switching to proxy:", proxy['ip'] + ':' + proxy['port'])
        try:
            response = requests.get('https:
            print('Request', n, '- Status Code:', response.status_code)
        except Exception as e:
            print("Request", n, "- Error:", e)
        time.sleep(1)
if __name__ == '__main__':
    main()