import requests
from bs4 import BeautifulSoup
import re
def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Host': 'www.plantcell.org'
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    return response.text
def analyse(html):
    soup = BeautifulSoup(html, 'lxml')
    contents = []
    for paragraph in soup.find_all('p'):
        try:
            if "p-" in paragraph.get('id', ''):
                content = paragraph.get_text(strip=True)
                content = re.sub(r' +', ' ', content)
                if len(content) > 250:
                    contents.append(content)
        except Exception as e:
            print(f"Error extracting content: {e}")
    count = 1
    address_list = []
    author_list = []
    for item in soup.find_all('li'):
        try:
            if 'last' in item.get('class', []) and 'name' in str(item):
                author = item.find('a').string
                author_list.append(author)
            elif 'aff' in item.get('class', []):
                address = item.find('address').get_text(separator=' ', strip=True)
                if re.match(r'[a-z]', address[0]):
                    address = address[1:]
                address = f"{count}\t{address}\n"
                address_list.append(address)
                count += 1
        except Exception as e:
            print(f"Error extracting author/address: {e}")
    if len(contents) > 2:
        print("Content error")
        return '', '', ''
    return ''.join(contents), ''.join(author_list), ''.join(address_list)
def main(vol, page):
    url = f"http:
    html = get_html(url)
    content, author, address = analyse(html)
    with open(f"{vol}-content.csv", 'a', encoding='utf-8') as content_file, \
         open(f"{vol}-author.csv", 'a', encoding='utf-8') as author_file, \
         open(f"{vol}-address.csv", 'a', encoding='utf-8') as address_file:
        if content and content[-1] != "\n":
            content += "\n"
        if author and author[-1] != "\n":
            author += "\n"
        if address and address[-1] != "\n":
            address += "\n"
        content_file.write(f">{page}\n{content}")
        author_file.write(f">{page}\n{author}")
        address_file.write(f">{page}\n{address}")
def get_issues(issue_number):
    return [1, 2, 3, 4, 5]
if __name__ == "__main__":
    for issue in range(1, 12):
        pages = get_issues(issue)
        print(f"Processing volume: {issue}")
        for page in pages:
            print(f"Processing page: {page}")
            try:
                main(issue, page)
            except Exception as e:
                print(f"Error processing volume {issue}, page {page}: {e}")