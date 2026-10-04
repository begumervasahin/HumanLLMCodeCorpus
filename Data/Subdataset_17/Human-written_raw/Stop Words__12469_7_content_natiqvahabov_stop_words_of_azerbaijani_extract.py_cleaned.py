import nltk
import urllib.request as urllib2
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
from bs4 import BeautifulSoup
from collections import Counter
wiki_list = []
wiki_list_titles = []
wiki_page = "https:
page = urllib2.urlopen(wiki_page)
soup = BeautifulSoup(page, 'html.parser')
div_mw_parser_output = soup.find('div', attrs={'class': 'mw-parser-output'})
div_mw_parser_output = div_mw_parser_output.find('tr')
tds = div_mw_parser_output.find_next('tr').find_all('td')
for td in tds:
	hrefs = td.find_all('a')
	for href in hrefs:
		if(href.get('title')):
			wiki_list.append('https:
			wiki_list_titles.append(href.get('title'))
wiki_list_test = ['https:
tokenized_final = []
i=1
for wiki in wiki_list:
	print(i)
	page_single = urllib2.urlopen(wiki)
	soup_single = BeautifulSoup(page_single, 'html.parser')
	div_mw_parser_output_single = soup_single.find('div', attrs={'class': 'mw-parser-output'})
	content = div_mw_parser_output_single.get_text()
	tokenizer = RegexpTokenizer(r'\w+')
	tokenized_text = tokenizer.tokenize(content)
	tokenized_final += tokenized_text
	i=i+1
cnt = Counter(tokenized_final)
with open('stopwordsAZE.txt', 'a') as the_file:
	the_file.write(str(cnt))