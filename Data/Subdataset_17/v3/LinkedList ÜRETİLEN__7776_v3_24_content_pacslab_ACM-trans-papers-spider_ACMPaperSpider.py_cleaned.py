import requests
import os
import re
from bs4 import BeautifulSoup
class PaperSpider:
    papers_order = 1
    def __init__(self, name, url="https:
        self.name = name
        self.url = url
        self.filename = filename
    def get_html(self, url):
        try:
            headers = {
                "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                               "AppleWebKit/537.36 (KHTML, like Gecko) "
                               "Chrome/58.0.3029.110 Safari/537.3")
            }
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            response.encoding = response.apparent_encoding
            html_content = os.linesep.join([line for line in response.text.splitlines() if line])
            return html_content
        except Exception as e:
            print(f"Failed to get HTML from {url}: {e}")
            return ""
    def parse_page(self, html):
        try:
            current_issue_papers = []
            soup = BeautifulSoup(html, 'html.parser')
            title_boxes = soup.find_all('h5', class_='issue-item__title')
            for title_box in title_boxes:
                title = re.sub(' +', ' ', title_box.text.strip())
                title = re.sub('\n', ' ', title).strip()
                if title == "List of Reviewers":
                    continue
                doi_num = str(title_box).split("/doi/abs", 1)[1].split("\">", 1)[0]
                doi_link = "https:
                current_issue_papers.append([doi_link, title])
            self.store_paper_info(current_issue_papers)
            next_box = soup.find('a', class_='content-navigation__btn--next')
            if not next_box or next_box['href'] == "javascript:void(0)":
                return
            next_link = "https:
            next_html = self.get_html(next_link)
            self.parse_page(next_html)
        except Exception as e:
            print(f"Failed to parse page: {e}")
    def store_paper_info(self, current_issue_papers):
        try:
            with open(self.filename, "a", encoding="utf-8") as file:
                for doi_link, paper_title in current_issue_papers:
                    file.write(f"Paper {self.papers_order}\nTitle: {paper_title}\nDOI Link: {doi_link}\n")
                    file.write("==========================\n")
                    self.papers_order += 1
        except Exception as e:
            print(f"Failed to store paper info: {e}")
def main():
    print("Welcome to the ACM Transactions journal papers Spider!")
    while True:
        start_url = input("Enter a start URL or type 'quit' to exit: ")
        if start_url.lower() == 'quit':
            print("Goodbye!")
            break
        file_name = input("Enter a filename (e.g., ACM_papers_list.txt) or type 'quit' to exit: ")
        if file_name.lower() == 'quit':
            print("Goodbye!")
            break
        acm_spider = PaperSpider("ACMSpider", start_url, file_name)
        html_result = acm_spider.get_html(start_url)
        if html_result:
            acm_spider.parse_page(html_result)
        else:
            print("Failed to retrieve HTML content.")
if __name__ == '__main__':
    main()