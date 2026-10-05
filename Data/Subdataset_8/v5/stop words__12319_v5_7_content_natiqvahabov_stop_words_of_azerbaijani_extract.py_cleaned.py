import urllib.request as urllib2
from bs4 import BeautifulSoup
from collections import Counter
from nltk.tokenize import RegexpTokenizer
def fetch_article_info(page_url):
    page = urllib2.urlopen(page_url)
    soup = BeautifulSoup(page, 'html.parser')
    articles_section = soup.find('div', class_='mw-parser-output').find('tr').find_next('tr')
    article_info = []
    for td in articles_section.find_all('td'):
        for link in td.find_all('a'):
            if link.get('title'):
                article_url = 'https:
                article_title = link.get('title')
                article_info.append((article_title, article_url))
    return article_info
def tokenize_article_content(article_url):
    page_single = urllib2.urlopen(article_url)
    soup_single = BeautifulSoup(page_single, 'html.parser')
    content = soup_single.find('div', class_='mw-parser-output').get_text()
    tokenizer = RegexpTokenizer(r'\w+')
    tokenized_text = tokenizer.tokenize(content)
    return tokenized_text
def process_articles(article_info_list, output_file):
    tokenized_final = []
    for idx, (article_title, article_url) in enumerate(article_info_list, start=1):
        print("Processing article", idx, ":", article_title)
        tokenized_text = tokenize_article_content(article_url)
        tokenized_final += tokenized_text
    token_counter = Counter(tokenized_final)
    with open(output_file, 'a') as file:
        file.write(str(token_counter))
if __name__ == "__main__":
    wiki_page_url = "https:
    output_file = 'stopwordsAZE.txt'
    article_info_list = fetch_article_info(wiki_page_url)
    process_articles(article_info_list, output_file)