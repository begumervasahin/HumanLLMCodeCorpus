import urllib.request
from bs4 import BeautifulSoup
import ssl
def retrieve_url(url, count, position):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    for i in range(count):
        print('Retrieving:', url)
        try:
            html = urllib.request.urlopen(url, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            tags = soup('a')
            url = tags[position - 1].get('href', None)
        except Exception as e:
            print('Error:', e)
            break
if __name__ == "__main__":
    url = input('Enter URL: ')
    count = int(input('Enter count: '))
    position = int(input('Enter position: '))
    retrieve_url(url, count, position)