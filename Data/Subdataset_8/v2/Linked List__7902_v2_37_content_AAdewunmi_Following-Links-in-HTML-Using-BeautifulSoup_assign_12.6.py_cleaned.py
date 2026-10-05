import urllib.request
from bs4 import BeautifulSoup
import ssl
def main():
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    url = input('Enter URL: ')
    count = int(input('Enter count: '))
    position = int(input('Enter position: '))
    for _ in range(count):
        print('Retrieving:', url)
        html = urllib.request.urlopen(url, context=ssl_context).read()
        soup = BeautifulSoup(html, 'html.parser')
        anchor_tags = soup('a')
        url = anchor_tags[position - 1].get('href', None)
if __name__ == '__main__':
    main()