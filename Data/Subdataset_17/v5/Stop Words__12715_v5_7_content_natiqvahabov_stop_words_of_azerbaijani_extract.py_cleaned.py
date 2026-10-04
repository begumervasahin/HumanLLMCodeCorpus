import urllib.request as urllib2
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
from collections import Counter
def fetch_wikipedia_urls(page_url):
    urls = []
    titles = []
    response = urllib2.urlopen(page_url)
    soup = BeautifulSoup(response, 'html.parser')
    table_row = soup.find('div', class_='mw-parser-output').find('tr')
    table_cells = table_row.find_next('tr').find_all('td')
    for cell in table_cells:
        links = cell.find_all('a')
        for link in links:
            title = link.get('title')
            if title:
                href = link['href']
                urls.append(f'https:
                titles.append(title)
    return urls, titles
def tokenize_wikipedia_articles(urls):
    tokenizer = RegexpTokenizer(r'\w+')
    all_tokens = []
    for index, url in enumerate(urls, start=1):
        print(f"Processing article {index} from {url}")
        response = urllib2.urlopen(url)
        soup = BeautifulSoup(response, 'html.parser')
        content = soup.find('div', class_='mw-parser-output').get_text()
        tokens = tokenizer.tokenize(content)
        all_tokens.extend(tokens)
    return all_tokens
def save_word_counts_to_file(tokens, filename='stopwordsAZE.txt'):
    word_counts = Counter(tokens)
    with open(filename, 'a') as file:
        file.write(str(word_counts))
def main():
    wiki_page_url = "https:
    wiki_urls, wiki_titles = fetch_wikipedia_urls(wiki_page_url)
    demo_urls = [
        'https:
        'https:
    ]
    tokens = tokenize_wikipedia_articles(demo_urls)
    save_word_counts_to_file(tokens)
if __name__ == "__main__":
    main()