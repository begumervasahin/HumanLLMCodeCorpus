import requests
import os
import re
from bs4 import BeautifulSoup
class PaperSpider:
    def __init__(self, name, url="https:
        self.name = name
        self.url = url
        self.filename = filename
        self.papers_order = 1
    def get_html(self, url):
        try:
            headers = {"User-Agent": "Safari/12.1.2"}
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            response.encoding = response.apparent_encoding
            return os.linesep.join([line for line in response.text.splitlines() if line])
        except requests.RequestException as e:
            print(f"Error fetching URL {url}: {e}")
            return ""
    def parse_page(self, html):
        try:
            soup = BeautifulSoup(html, 'html.parser')
            title_boxes = soup.find_all('h5', class_='issue-item__title')
            current_issue_papers = []
            for title_box in title_boxes:
                title = self.clean_title(title_box.text)
                if title.lower() == "list of reviewers":
                    continue
                doi_link = self.extract_doi_link(title_box)
                current_issue_papers.append((doi_link, title))
            self.store_paper_info(current_issue_papers)
            next_link = self.find_next_link(soup)
            if next_link:
                next_html = self.get_html(next_link)
                self.parse_page(next_html)
        except Exception as e:
            print(f"Error parsing HTML: {e}")
    def clean_title(self, title):
        title = title.strip()
        title = re.sub(' +', ' ', title)
        title = re.sub('\n', ' ', title)
        return title.strip()
    def extract_doi_link(self, title_box):
        doi_num = str(title_box).split("/doi/abs", 1)[1].split("\">", 1)[0]
        return "https:
    def find_next_link(self, soup):
        next_box = soup.find('a', class_='content-navigation__btn--next')
        if next_box and 'href' in next_box.attrs and next_box['href'] != "javascript:void(0)":
            return "https:
        return None
    def store_paper_info(self, papers):
        try:
            with open(self.filename, "a") as f:
                for doi_link, paper_title in papers:
                    f.write(f"paper{self.papers_order}\nTitle: {paper_title}\nDoi_link: {doi_link}\n")
                    f.write("==========================\n")
                    self.papers_order += 1
        except IOError as e:
            print(f"Error writing to file {self.filename}: {e}")
if __name__ == '__main__':
    print("Welcome to the ACM Transactions journal papers Spider!")
    while True:
        start_url = input("Enter a start URL or 'quit' to exit: ")
        if start_url.lower() == 'quit':
            print("Goodbye!")
            break
        file_name = input("Enter a filename (e.g., ACM_papers_list.txt) or 'quit' to exit: ")
        if file_name.lower() == 'quit':
            print("Goodbye!")
            break
        spider = PaperSpider("ACM Spider", start_url, file_name)
        html_result = spider.get_html(start_url)
        if html_result:
            spider.parse_page(html_result)