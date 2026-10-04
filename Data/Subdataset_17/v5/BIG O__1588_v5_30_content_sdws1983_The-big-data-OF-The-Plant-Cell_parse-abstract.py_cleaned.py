import urllib2
import re
import sys
from bs4 import BeautifulSoup
from pdf_read import get_issues
reload(sys)
sys.setdefaultencoding('utf-8')
def get_html(url):
    send_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Host': 'www.plantcell.org'
    }
    req = urllib2.Request(url, headers=send_headers)
    response = urllib2.urlopen(req)
    html = response.read().decode('utf-8')
    return html
def analyse(html):
    soup = BeautifulSoup(html, 'lxml')
    contents = extract_contents(soup)
    authors, addresses = extract_authors_addresses(soup)
    if len(contents) > 2:
        print("content error")
        return '', '', ''
    return ''.join(contents), ''.join(authors), ''.join(addresses)
def extract_contents(soup):
    contents = []
    for paragraph in soup.find_all('p'):
        try:
            if "p-" in paragraph.get('id', ''):
                content = extract_text_from_html_element(str(paragraph))
                if len(content) > 250:
                    contents.append(content)
        except Exception:
            pass
    return contents
def extract_authors_addresses(soup):
    authors = []
    addresses = []
    count = 1
    for item in soup.find_all('li'):
        try:
            if 'last' in item.get('class', []) and 'name' in str(item):
                author = item.find_all('a')[0].string
                authors.append(author)
            elif 'aff' in item.get('class', []):
                address = extract_text_from_html_element(str(item.find_all('address')[0]))
                address = f"{count}\t{address}\n"
                addresses.append(address)
                count += 1
        except Exception:
            pass
    return authors, addresses
def extract_text_from_html_element(element):
    text = re.sub(r'<.*?>', '', element)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r' +', ' ', text).strip()
    return text
def main(vol, page):
    url = f"http:
    html = get_html(url)
    content, author, address = analyse(html)
    save_to_file(f"{vol}-content.csv", page, content)
    save_to_file(f"{vol}-author.csv", page, author)
    save_to_file(f"{vol}-address.csv", page, address)
def save_to_file(filename, page, data):
    if not data.endswith("\n"):
        data += "\n"
    with open(filename, 'a') as file:
        file.write(f">{page}\n{data}")
if __name__ == "__main__":
    for volume in range(1, 12):
        all_issues = get_issues(volume)
        print(f"vol: {volume}")
        for issue in all_issues:
            print(issue)
            try:
                main(volume, issue)
            except Exception as e:
                print(e)