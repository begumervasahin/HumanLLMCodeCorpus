import nltk
import urllib.request as urllib2
from nltk.tokenize import RegexpTokenizer
from bs4 import BeautifulSoup
from collections import Counter
wiki_page_url = "https:
page = urllib2.urlopen(wiki_page_url)
soup = BeautifulSoup(page, 'html.parser')
articles_section = soup.find('div', attrs={'class': 'mw-parser-output'}).find('tr').find_next('tr')
wiki_list_urls = []
wiki_list_titles = []
for td in articles_section.find_all('td'):
    for link in td.find_all('a'):
        if link.get('title'):
            wiki_list_urls.append('https:
            wiki_list_titles.append(link.get('title'))
wiki_list_test = ['https:
tokenized_final = []
for idx, wiki_url in enumerate(wiki_list_urls, start=1):
    print("Processing article", idx)
    page_single = urllib2.urlopen(wiki_url)
    soup_single = BeautifulSoup(page_single, 'html.parser')
    content = soup_single.find('div', attrs={'class': 'mw-parser-output'}).get_text()
    tokenizer = RegexpTokenizer(r'\w+')
    tokenized_text = tokenizer.tokenize(content)
    tokenized_final += tokenized_text
token_counter = Counter(tokenized_final)
with open('stopwordsAZE.txt', 'a') as file:
    file.write(str(token_counter))