
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
def fonk2(b11):
    b3 = re.sub(r'\[[0-9]*\]', ' ', b11)
    b3 = re.sub(r'\s+', ' ', b3)
    b4 = b3.lower()
    b4 = re.sub(r'\W', ' ', b4)
    b4 = re.sub(r'\d', ' ', b4)
    b4 = re.sub(r'\s+', ' ', b4)
    return b3, b4
def fonk3(original_text, b4):
    b5 = nltk.sent_tokenize(original_text)
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
    b11 = fonk1(url)
    original_text, b4 = fonk2(b11)
    b9 = fonk3(original_text, b4)
    b12 = heapq.nlargest(b10, b9, key=b9.get)
    return b12
if b13 = = '__main__':
    b14 = 'https:
    b15 = fonk4(b14)
    print('------------------------------------------------------------')
    for sentence in b15:
        print(sentence)