
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
    b4 = b3.lower()
    b4 = re.sub(r'\W', ' ', b4)
    b4 = re.sub(r'\d', ' ', b4)
    b4 = re.sub(r'\s+', ' ', b4)
    return b4
def fonk3(b9, b11):
    b5 = {}
    for sentence in b9:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in b11:
                if len(sentence.split(' ')) < 25:
                    if sentence not in b5:
                        b5[sentence] = b11[word]
                    else:
                        b5[sentence] += b11[word]
    return b5
def fonk4():
    b6 = 'https:
    b7 = fonk1(b6)
    b8 = fonk2(b7)
    b9 = nltk.sent_tokenize(b7)
    b10 = set(nltk.corpus.stopwords.words('english'))
    b11 = {}
    for word in nltk.word_tokenize(b8):
        if word not in b10:
            if word not in b11:
                b11[word] = 1
            else:
                b11[word] += 1
    b12 = max(b11.values())
    for word in b11:
        b11[word] = b11[word] / b12
    b5 = fonk3(b9, b11)
    b13 = heapq.nlargest(5, b5, key=b5.get)
    print('------------------------------------------------------------')
    for sentence in b13:
        print(sentence)
if b14 = = '__main__':
    fonk4()