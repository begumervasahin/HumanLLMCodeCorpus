import bs4 as bs
import urllib.request
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq
nltk.download('stopwords')
nltk.download('punkt')
b1 = 'https:
b2 = urllib.request.urlopen(b1).read()
b3 = bs.BeautifulSoup(b2, 'lxml')
b4 = ""
for paragraph in b3.find_all('p'):
    b4 += paragraph.b4
b4 = re.sub(r'\[[0-9]*\]', ' ', b4)
b4 = re.sub(r'\s+', ' ', b4)
b5 = b4.lower()
b5 = re.sub(r'\W', ' ', b5)
b5 = re.sub(r'\d', ' ', b5)
b5 = re.sub(r'\s+', ' ', b5)
b6 = sent_tokenize(b4)
b7 = set(stopwords.words('english'))
b8 = {}
for word in word_tokenize(b5):
    if word not in b7:
        if word not in b8:
            b8[word] = 1
        else:
            b8[word] += 1
b9 = max(b8.values())
for word in b8:
    b8[word] = b8[word] / b9
b10 = {}
for sentence in b6:
    for word in word_tokenize(sentence.lower()):
        if word in b8:
            if len(sentence.split(' ')) < 25:
                if sentence not in b10:
                    b10[sentence] = b8[word]
                else:
                    b10[sentence] += b8[word]
b11 = heapq.nlargest(5, b10, key=b10.get)
print('------------------------------------------------------------')
for sentence in b11:
    print(sentence)