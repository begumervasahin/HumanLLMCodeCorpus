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
def fonk1(paragraphs):
    b4 = ""
    for paragraph in paragraphs:
        b4 += paragraph.b4
    return b4
def fonk2(b4):
    b4 = re.sub(r'\[[0-9]*\]', ' ', b4)
    b4 = re.sub(r'\s+', ' ', b4)
    b5 = b4.lower()
    b5 = re.sub(r'\W', ' ', b5)
    b5 = re.sub(r'\d', ' ', b5)
    b5 = re.sub(r'\s+', ' ', b5)
    return b5
def fonk3(b4):
    return sent_tokenize(b4)
def fonk4(b5):
    b6 = set(stopwords.words('english'))
    b7 = {}
    for word in word_tokenize(b5):
        if word not in b6:
            if word not in b7:
                b7[word] = 1
            else:
                b7[word] += 1
    return b7
def fonk5(b7):
    b8 = max(b7.values())
    for word in b7:
        b7[word] = b7[word] / b8
    return b7
def fonk6(b11, b7):
    b9 = {}
    for sentence in b11:
        for word in word_tokenize(sentence.lower()):
            if word in b7 and len(sentence.split(' ')) < 25:
                if sentence not in b9:
                    b9[sentence] = b7[word]
                else:
                    b9[sentence] += b7[word]
    return b9
def fonk7(b9):
    return heapq.nlargest(5, b9, b10 = b9.get)
def fonk8(b12):
    print('------------------------------------------------------------')
    for sentence in b12:
        print(sentence)
def fonk9():
    b4 = fonk1(b3.find_all('p'))
    b5 = fonk2(b4)
    b11 = fonk3(b4)
    b7 = fonk4(b5)
    b7 = fonk5(b7)
    b9 = fonk6(b11, b7)
    b12 = fonk7(b9)
    fonk8(b12)
if b13 = = "__main__":
    fonk9()