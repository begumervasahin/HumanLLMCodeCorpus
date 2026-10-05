import urllib.request
from bs4 import BeautifulSoup
import ssl
def retrieve_url(url, count, position):
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    for _ in range(count):
        print('Retrieving:', url)
        try:
            html = urllib.request.urlopen(url, context=ssl_context).read()
            soup = BeautifulSoup(html, 'html.parser')
            anchor_tags = soup.find_all('a')
            url = anchor_tags[position - 1].get('href', None)
        except Exception as e:
            print('Error:', e)
            break
if __name__ == "__main__":
    url = input('Enter URL: ')
    count = int(input('Enter count: '))
    position = int(input('Enter position: '))
    retrieve_url(url, count, position)