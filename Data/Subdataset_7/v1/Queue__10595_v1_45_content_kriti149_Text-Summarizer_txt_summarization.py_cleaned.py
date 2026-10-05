import bs4 as bs
import urllib.request
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq
nltk.download('stopwords')
nltk.download('punkt')
b1 = urllib.request.urlopen('https:
b2 = bs.BeautifulSoup(b1, 'lxml')
b3 = ""
for paragraph in b2.find_all('p'):
    b3 += paragraph.b3
b3 = re.sub(r'\[[0-9]*\]', ' ', b3)
b3 = re.sub(r'\s+', ' ', b3)
b4 = b3.lower()
b4 = re.sub(r'\W', ' ', b4)
b4 = re.sub(r'\d', ' ', b4)
b4 = re.sub(r'\s+', ' ', b4)
b5 = sent_tokenize(b3)
b6 = set(stopwords.words('english'))
b7 = {}
for word in word_tokenize(b4):
    if word not in b6:
        if word not in b7.keys():
            b7[word] = 1
        else:
            b7[word] += 1
b8 = max(b7.values())
for word in b7.keys():
    b7[word] = b7[word] / b8
b9 = {}
for sentence in b5:
    for word in word_tokenize(sentence.lower()):
        if word in b7.keys():
            if len(sentence.split(' ')) < 25:
                if sentence not in b9.keys():
                    b9[sentence] = b7[word]
                else:
                    b9[sentence] += b7[word]
b10 = heapq.nlargest(5, b9, key=b9.get)
print('------------------------------------------------------------')
for sentence in b10:
    print(sentence)