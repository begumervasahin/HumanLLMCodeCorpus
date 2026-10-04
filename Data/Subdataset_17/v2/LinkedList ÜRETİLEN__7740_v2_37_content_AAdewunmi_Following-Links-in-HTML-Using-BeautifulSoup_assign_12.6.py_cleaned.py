import urllib.request
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
def get_html(url, context):
    return urllib.request.urlopen(url, context=context).read()
def find_next_url(soup, position):
    tags = soup('a')
    if len(tags) >= position:
        return tags[position - 1].get('href', None)
    else:
        print(f"No link found at position {position}")
        return None
def main():
    url = input('Enter URL: ')
    count = int(input('Enter count: '))
    position = int(input('Enter position: '))
    for i in range(count + 1):
        print('Retrieving:', url)
        html = get_html(url, ctx)
        soup = BeautifulSoup(html, 'html.parser')
        next_url = find_next_url(soup, position)
        if next_url:
            url = next_url
        else:
            break
if __name__ == "__main__":
    main()