
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
    b3 = ""
    for paragraph in b2.find_all('p'):
        b3 += paragraph.b3
    return b3
def fonk2(b3):
    b3 = re.sub(r'\[[0-9]*\]', ' ', b3)
    b3 = re.sub(r'\s+', ' ', b3)
    b3 = b3.lower()
    b3 = re.sub(r'\W', ' ', b3)
    b3 = re.sub(r'\d', ' ', b3)
    b3 = re.sub(r'\s+', ' ', b3)
    return b3
def fonk3(b8, b10):
    b4 = {}
    for sentence in b8:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in b10:
                if len(sentence.split()) < 25:
                    if sentence not in b4:
                        b4[sentence] = b10[word]
                    else:
                        b4[sentence] += b10[word]
    return b4
def fonk4():
    b5 = 'https:
    b6 = fonk1(b5)
    b7 = fonk2(b6)
    b8 = nltk.sent_tokenize(b6)
    b9 = set(nltk.corpus.stopwords.words('english'))
    b10 = {}
    for word in nltk.word_tokenize(b7):
        if word not in b9:
            if word not in b10:
                b10[word] = 1
            else:
                b10[word] += 1
    b11 = max(b10.values())
    for word in b10:
        b10[word] = b10[word] / b11
    b4 = fonk3(b8, b10)
    b12 = heapq.nlargest(5, b4, key=b4.get)
    print('-------------------- Summary --------------------')
    for sentence in b12:
        print(sentence)
if b13 = = '__main__':
    fonk4()