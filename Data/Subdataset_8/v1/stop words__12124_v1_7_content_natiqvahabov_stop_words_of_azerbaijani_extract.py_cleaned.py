import urllib.request as urllib2
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
from collections import Counter
wiki_page = "https:
def scrape_article_urls(url):
    article_urls = []
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    table = soup.find('table', class_='mw-content-ltr')
    if table:
        links = table.find_all('a')
        for link in links:
            article_urls.append('https:
    return article_urls
def tokenize_text(text):
    tokenizer = RegexpTokenizer(r'\w+')
    return tokenizer.tokenize(text)
def count_and_write_to_file(tokens, filename):
    token_counts = Counter(tokens)
    with open(filename, 'a') as file:
        for token, count in token_counts.items():
            file.write(f"{token}: {count}\n")
def main():
    article_urls = scrape_article_urls(wiki_page)
    tokenized_final = []
    for i, url in enumerate(article_urls, start=1):
        print(f"Processing article {i}/{len(article_urls)}")
        page_single = urllib2.urlopen(url)
        soup_single = BeautifulSoup(page_single, 'html.parser')
        content = soup_single.find('div', class_='mw-parser-output').get_text()
        tokens = tokenize_text(content)
        tokenized_final.extend(tokens)
    count_and_write_to_file(tokenized_final, 'stopwordsAZE.txt')
    print("Token counts written to file.")
if __name__ == "__main__":
    main()