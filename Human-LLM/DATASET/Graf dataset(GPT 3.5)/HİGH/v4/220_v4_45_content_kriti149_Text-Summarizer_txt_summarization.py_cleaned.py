
import bs4 as bs
import urllib.request
import re
import nltk
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
b5 = nltk.sent_tokenize(b3)
b6 = {}
for word in nltk.word_tokenize(b4):
    if word not in nltk.corpus.stopwords.words('english'):
        if word not in b6.keys():
            b6[word] = 1
        else:
            b6[word] += 1
for word in b6.keys():
    b6[word] = b6[word] / max(b6.values())
b7 = {}
for sentence in b5:
    for word in nltk.word_tokenize(sentence.lower()):
        if word in b6.keys():
            if len(sentence.split(' ')) < 25:
                if sentence not in b7.keys():
                    b7[sentence] = b6[word]
                else:
                    b7[sentence] += b6[word]
b8 = heapq.nlargest(5, b7, key=b7.get)
print('------------------------------------------------------------')
for sentence in b8:
    print(sentence)