import urllib.request as urllib2
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
from collections import Counter
def fetch_wiki_links(url):
    links = []
    titles = []
    try:
        response = urllib2.urlopen(url)
        soup = BeautifulSoup(response, 'html.parser')
        content_div = soup.find('div', class_='mw-parser-output')
        for tr in content_div.find_all('tr'):
            for td in tr.find_all('td'):
                for a_tag in td.find_all('a'):
                    title = a_tag.get('title')
                    if title:
                        full_url = 'https:
                        links.append(full_url)
                        titles.append(title)
    except Exception as e:
        print(f"Error fetching or parsing URL: {e}")
    return links, titles
def tokenize_wiki_pages(links):
    tokenizer = RegexpTokenizer(r'\w+')
    all_tokens = []
    for index, link in enumerate(links):
        print(f"Processing {index + 1}/{len(links)}: {link}")
        try:
            response = urllib2.urlopen(link)
            soup = BeautifulSoup(response, 'html.parser')
            content_div = soup.find('div', class_='mw-parser-output')
            content = content_div.get_text()
            tokens = tokenizer.tokenize(content)
            all_tokens.extend(tokens)
        except Exception as e:
            print(f"Error fetching or parsing URL: {e}")
    return all_tokens
def save_counter_to_file(counter, filename):
    try:
        with open(filename, 'w') as file:
            file.write(str(counter))
    except Exception as e:
        print(f"Error writing to file: {e}")
def main():
    wiki_page_url = "https:
    links, _ = fetch_wiki_links(wiki_page_url)
    test_links = [
        'https:
        'https:
    ]
    tokenized_words = tokenize_wiki_pages(test_links)
    word_counter = Counter(tokenized_words)
    save_counter_to_file(word_counter, 'stopwordsAZE.txt')
if __name__ == "__main__":
    main()