import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
def main():
    url = input('Enter URL: ')
    count = int(input('Enter count: '))
    position = int(input('Enter position: '))
    for i in range(count + 1):
        print('Retrieving:', url)
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        if len(tags) >= position:
            url = tags[position - 1].get('href', None)
        else:
            print(f"No link found at position {position}")
            break
if __name__ == "__main__":
    main()