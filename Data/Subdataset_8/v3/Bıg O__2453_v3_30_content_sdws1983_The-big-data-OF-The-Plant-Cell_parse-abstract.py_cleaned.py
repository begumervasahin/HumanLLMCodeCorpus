from bs4 import BeautifulSoup
import requests
import re
def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Host': 'www.plantcell.org'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text
def extract_contents(soup):
    contents = []
    for paragraph in soup.find_all('p', id=re.compile(r'p-\d+')):
        content = paragraph.get_text(strip=True)
        if len(content) > 250:
            contents.append(content)
    return '\n'.join(contents)
def extract_authors_addresses(soup):
    author_list = []
    address_list = []
    count = 1
    for item in soup.find_all('li'):
        try:
            if 'last' in item['class'] and 'name' in str(item):
                author = item.find('a').string
                author_list.append(author)
            elif 'aff' in item['class']:
                address = item.find('address').get_text(strip=True)
                if address and address[0].isalpha():
                    address = address[1:]
                address_list.append(f"{count}\t{address}")
                count += 1
        except Exception as e:
            pass
    return '\n'.join(author_list), '\n'.join(address_list)
def analyse(html):
    soup = BeautifulSoup(html, 'html.parser')
    contents = extract_contents(soup)
    authors, addresses = extract_authors_addresses(soup)
    if len(contents.split('\n')) > 2:
        print("Content error")
        contents = authors = addresses = ''
    return contents, authors, addresses
def save_to_csv(vol, page, contents, authors, addresses):
    with open(f"{vol}-content.csv", 'a') as content_file, \
         open(f"{vol}-author.csv", 'a') as author_file, \
         open(f"{vol}-address.csv", 'a') as address_file:
        if contents and contents[-1] != "\n":
            contents += "\n"
        if authors and authors[-1] != "\n":
            authors += "\n"
        if addresses and addresses[-1] != "\n":
            addresses += "\n"
        content_file.write(f">{page}\n{contents}")
        author_file.write(f">{page}\n{authors}")
        address_file.write(f">{page}\n{addresses}")
def process_volume(volume):
    for page in get_issues(volume):
        print(f"Volume: {volume}, Page: {page}")
        try:
            url = f"http:
            html = get_html(url)
            content, authors, addresses = analyse(html)
            save_to_csv(volume, page, content, authors, addresses)
        except Exception as e:
            print(e)
if __name__ == "__main__":
    for vol in range(1, 12):
        process_volume(vol)