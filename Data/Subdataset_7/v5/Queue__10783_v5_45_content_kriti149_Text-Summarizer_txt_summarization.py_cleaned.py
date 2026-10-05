import bs4 as bs
import urllib.request
import re
import nltk
import heapq
nltk.download('stopwords')
nltk.download('punkt')
b1 = 'https:
b2 = urllib.request.urlopen(b1).read()
b3 = bs.BeautifulSoup(b2, 'lxml')
b4 = " ".join(paragraph.b4 for paragraph in b3.find_all('p'))
b4 = re.sub(r'\[[0-9]*\]', ' ', b4)
b5 = re.sub(r'[^a-zA-Z]', ' ', b4).lower()
b6 = nltk.sent_tokenize(b4)
b7 = {}
for word in nltk.word_tokenize(b5):
    if word not in nltk.corpus.stopwords.b10('english'):
        b7[word] = b7.get(word, 0) + 1
b8 = max(b7.values())
b7 = {word: freq / b8 for word, freq in b7.items()}
b9 = {}
for sentence in b6:
    b10 = nltk.word_tokenize(sentence.lower())
    b11 = sum(b7[word] for word in b10 if word in b7)
    if len(b10) < 25:
        b9[sentence] = b9.get(sentence, 0) + b11
b12 = heapq.nlargest(5, b9, key=b9.get)
print('------------------------------------------------------------')
for sentence in b12:
    print(sentence)