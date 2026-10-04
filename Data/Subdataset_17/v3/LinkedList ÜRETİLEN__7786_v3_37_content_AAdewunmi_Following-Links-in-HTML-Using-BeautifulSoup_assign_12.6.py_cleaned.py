import urllib.request
from bs4 import BeautifulSoup
import ssl
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE
def get_html(url, context):
    with urllib.request.urlopen(url, context=context) as response:
        return response.read()
def find_next_url(soup, position):
    tags = soup.find_all('a')
    if len(tags) >= position:
        return tags[position - 1].get('href')
    else:
        print(f"No link found at position {position}")
        return None
def main():
    url = input('Enter URL: ')
    count = int(input('Enter count: '))
    position = int(input('Enter position: '))
    for i in range(count + 1):
        print('Retrieving:', url)
        html = get_html(url, ssl_context)
        soup = BeautifulSoup(html, 'html.parser')
        next_url = find_next_url(soup, position)
        if next_url:
            url = next_url
        else:
            break
if __name__ == "__main__":
    main()