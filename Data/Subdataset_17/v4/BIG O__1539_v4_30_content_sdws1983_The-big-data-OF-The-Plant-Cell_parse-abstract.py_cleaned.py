from bs4 import BeautifulSoup
import urllib2
import re
import sys
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
    contents = []
    for i in soup.find_all('p'):
        try:
            if u"p-" in str(i.get('id', '')):
                content = str(i)[(str(i).find(">") + 1):(str(i).find("</p>", str(i).find(">") + 1))]
                content = re.sub(r'<.*?>', '', content)
                content = re.sub(r'\n', ' ', content)
                content = re.sub(r' +', ' ', content)
                if len(content) > 250:
                    contents.append(content)
        except Exception:
            pass
    count = 1
    address_list = []
    author_list = []
    for each in soup.find_all('li'):
        try:
            if 'last' in each.get('class', []) and u'name' in str(each):
                author = each.find_all('a')[0].string
                author_list.append(author)
            elif 'aff' in each.get('class', []):
                address = str(each.find_all('address')[0])
                address = re.sub(r'<.*?>', '', address)
                address = re.sub(r' +', ' ', address)
                address = re.sub(r'\n', '', address)
                if re.findall('[a-z]', address[0]):
                    address = address[1:]
                address = f"{count}\t{address}\n"
                address_list.append(address)
                count += 1
        except Exception:
            pass
    if len(contents) > 2:
        print("content error")
        contents = []
        address_list = []
        author_list = []
    return ''.join(contents), ''.join(author_list), ''.join(address_list)
def main(vol, page):
    url = f"http:
    html = get_html(url)
    content, author, address = analyse(html)
    with open(f"{vol}-content.csv", 'a') as f1, \
         open(f"{vol}-author.csv", 'a') as f2, \
         open(f"{vol}-address.csv", 'a') as f3:
        if not content.endswith("\n"):
            content += "\n"
        if not author.endswith("\n"):
            author += "\n"
        if not address.endswith("\n"):
            address += "\n"
        f1.write(f">{page}\n{content}")
        f2.write(f">{page}\n{author}")
        f3.write(f">{page}\n{address}")
if __name__ == "__main__":
    for iss in range(1, 12):
        all_issues = get_issues(iss)
        print(f"vol: {iss}")
        for i in all_issues:
            print(i)
            try:
                main(iss, i)
            except Exception as e:
                print(e)