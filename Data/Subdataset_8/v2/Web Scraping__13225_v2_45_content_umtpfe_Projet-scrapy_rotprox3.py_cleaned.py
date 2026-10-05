import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
import time
user_agent_generator = UserAgent()
def fetch_proxies():
    proxies = []
    url = 'https:
    headers = {'User-Agent': user_agent_generator.random}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.find(id='proxylisttable').find_all('tr')
    for row in rows:
        columns = row.find_all('td')
        proxy = {
            'ip': columns[0].text,
            'port': columns[1].text
        }
        proxies.append(proxy)
    return proxies
def main():
    proxies_list = fetch_proxies()
    random_proxy_index = random.randint(0, len(proxies_list) - 1)
    proxy = proxies_list[random_proxy_index]
    print("Using proxy:", proxy['ip'] + ':' + proxy['port'])
    for request_number in range(1, 101):
        if request_number % 10 == 0:
            random_proxy_index = random.randint(0, len(proxies_list) - 1)
            proxy = proxies_list[random_proxy_index]
            print("Switching to proxy:", proxy['ip'] + ':' + proxy['port'])
        try:
            response = requests.get('https:
            print('Request', request_number, '- Status Code:', response.status_code)
        except Exception as e:
            print("Request", request_number, "- Error:", e)
        time.sleep(1)
if __name__ == '__main__':
    main()