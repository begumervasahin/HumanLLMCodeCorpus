import urllib.request as urllib2
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
from collections import Counter
def get_article_urls(url):
    article_urls = []
    try:
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        article_table = soup.find('table', class_='mw-content-ltr')
        if article_table:
            links = article_table.find_all('a')
            article_urls = ['https:
    except Exception as e:
        print(f"Error occurred while scraping article URLs: {e}")
    return article_urls
def tokenize_text(text):
    tokenizer = RegexpTokenizer(r'\w+')
    return tokenizer.tokenize(text)
def count_and_write_tokens(tokens, filename):
    token_counts = Counter(tokens)
    with open(filename, 'a') as file:
        for token, count in token_counts.items():
            file.write(f"{token}: {count}\n")
def main():
    wiki_page_url = "https:
    article_urls = get_article_urls(wiki_page_url)
    tokenized_text = []
    for i, article_url in enumerate(article_urls, start=1):
        print(f"Processing article {i}/{len(article_urls)}")
        try:
            page = urllib2.urlopen(article_url)
            soup = BeautifulSoup(page, 'html.parser')
            content_div = soup.find('div', class_='mw-parser-output')
            if content_div:
                article_text = content_div.get_text()
                tokens = tokenize_text(article_text)
                tokenized_text.extend(tokens)
        except Exception as e:
            print(f"Error occurred while processing article: {e}")
    count_and_write_tokens(tokenized_text, 'stopwordsAZE.txt')
    print("Token counts written to file.")
if __name__ == "__main__":
    main()