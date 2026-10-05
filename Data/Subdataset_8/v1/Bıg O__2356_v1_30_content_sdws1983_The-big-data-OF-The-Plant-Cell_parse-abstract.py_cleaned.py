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
def analyse(html):
    soup = BeautifulSoup(html, 'html.parser')
    contents = []
    author_list = []
    address_list = []
    for i in soup.find_all('p', id=re.compile(r'p-\d+')):
        content = i.get_text(strip=True)
        if len(content) > 250:
            contents.append(content)
    count = 1
    for each in soup.find_all('li'):
        try:
            if 'last' in each['class'] and 'name' in str(each):
                author = each.find('a').string
                author_list.append(author)
            elif 'aff' in each['class']:
                address = each.find('address').get_text(strip=True)
                if address and address[0].isalpha():
                    address = address[1:]
                address_list.append(f"{count}\t{address}")
                count += 1
        except Exception as e:
            pass
    if len(contents) > 2:
        print("Content error")
        contents = []
        author_list = []
        address_list = []
    return '\n'.join(contents), '\n'.join(author_list), '\n'.join(address_list)
def main(vol, page):
    url = f"http:
    html = get_html(url)
    content, author, address = analyse(html)
    with open(f"{vol}-content.csv", 'a') as f1, \
            open(f"{vol}-author.csv", 'a') as f2, \
            open(f"{vol}-address.csv", 'a') as f3:
        if content and content[-1] != "\n":
            content += "\n"
        if author and author[-1] != "\n":
            author += "\n"
        if address and address[-1] != "\n":
            address += "\n"
        f1.write(f">{page}\n{content}")
        f2.write(f">{page}\n{author}")
        f3.write(f">{page}\n{address}")
if __name__ == "__main__":
    for iss in range(1, 12):
        all_pages = get_issues(iss)
        print(f"vol: {iss}")
        for page in all_pages:
            print(page)
            try:
                main(iss, page)
            except Exception as e:
                print(e)