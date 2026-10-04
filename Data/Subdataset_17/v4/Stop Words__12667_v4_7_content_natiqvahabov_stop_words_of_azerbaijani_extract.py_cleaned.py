import urllib.request as urllib2
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
from collections import Counter
wiki_urls = []
wiki_titles = []
wiki_page_url = "https:
page = urllib2.urlopen(wiki_page_url)
soup = BeautifulSoup(page, 'html.parser')
table_row = soup.find('div', class_='mw-parser-output').find('tr')
table_cells = table_row.find_next('tr').find_all('td')
for cell in table_cells:
    links = cell.find_all('a')
    for link in links:
        if link.get('title'):
            wiki_urls.append('https:
            wiki_titles.append(link.get('title'))
wiki_urls_test = [
    'https:
    'https:
]
tokenized_words = []
for i, url in enumerate(wiki_urls, start=1):
    print(f"Processing article {i}")
    page_single = urllib2.urlopen(url)
    soup_single = BeautifulSoup(page_single, 'html.parser')
    content = soup_single.find('div', class_='mw-parser-output').get_text()
    tokenizer = RegexpTokenizer(r'\w+')
    tokenized_text = tokenizer.tokenize(content)
    tokenized_words += tokenized_text
word_count = Counter(tokenized_words)
with open('stopwordsAZE.txt', 'a') as file:
    file.write(str(word_count))