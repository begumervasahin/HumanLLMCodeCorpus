import urllib.request
import ssl
from bs4 import BeautifulSoup
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
def get_url_at_position(url, position):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    return tags[position - 1].get('href', None)
def main():
    url = input('Enter URL: ')
    count = int(input('Enter count: '))
    position = int(input('Enter position: '))
    for _ in range(count + 1):
        print('Retrieving:', url)
        url = get_url_at_position(url, position)
        if url is None:
            print("No URL found at the specified position.")
            break
if __name__ == "__main__":
    main()