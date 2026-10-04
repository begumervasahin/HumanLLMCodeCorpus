
import bs4 as bs
import urllib.request
import re
import nltk
import heapq
nltk.download('stopwords')
nltk.download('punkt')
def fonk1(url):
    b1 = urllib.request.urlopen(url).read()
    b2 = bs.BeautifulSoup(b1, 'lxml')
    b3 = "".join(paragraph.b3 for paragraph in b2.find_all('p'))
    return b3
def fonk2(b3):
    b3 = re.sub(r'\[[0-9]*\]', ' ', b3)
    b3 = re.sub(r'\s+', ' ', b3)
    b4 = b3.lower()
    b4 = re.sub(r'\W', ' ', b4)
    b4 = re.sub(r'\d', ' ', b4)
    b4 = re.sub(r'\s+', ' ', b4)
    return b3, b4
def fonk3(b3, b4):
    b5 = nltk.sent_tokenize(b3)
    b6 = nltk.corpus.stopwords.words('english')
    b7 = {}
    for word in nltk.word_tokenize(b4):
        if word not in b6:
            b7[word] = b7.get(word, 0) + 1
    b8 = max(b7.values())
    for word in b7:
        b7[word] = b7[word] / b8
    b9 = {}
    for sentence in b5:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in b7:
                if len(sentence.split()) < 25:
                    b9[sentence] = b9.get(sentence, 0) + b7[word]
    return b9
def fonk4(url, b10 = 5):
    b3 = fonk1(url)
    b3, b4 = fonk2(b3)
    b9 = fonk3(b3, b4)
    b11 = heapq.nlargest(b10, b9, key=b9.get)
    return b11
if b12 = = '__main__':
    b13 = 'https:
    b14 = fonk4(b13)
    print('------------------------------------------------------------')
    for sentence in b14:
        print(sentence)