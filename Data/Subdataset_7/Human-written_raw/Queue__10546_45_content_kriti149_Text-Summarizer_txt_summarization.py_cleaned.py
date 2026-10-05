
import bs4 as bs
import urllib.request
import re
import nltk
nltk.download('stopwords')
nltk.download('punkt')
import heapq
b1 = urllib.request.urlopen('https:
b2 = bs.BeautifulSoup(b1,'lxml')
b3 = ""
for paragraph in b2.find_all('p'):
     b3 +=paragraph.b3
b3 = re.sub(r'\[[0-9]*\]',' ',b3)
b3 = re.sub(r'\s+',' ',b3)
b4 = b3.lower()
b4 = re.sub(r'\W',' ',b4)
b4 = re.sub(r'\d',' ',b4)
b4 = re.sub(r'\s+',' ',b4)
b5 = nltk.sent_tokenize(b3)
b6 = nltk.corpus.stopwords.words('english')
b7 = {}
for word in nltk.word_tokenize(b4):
    if word not in b6:
        if word not in b7.keys():
            b7[word]=1
        else:
            b7[word]+=1
for word in b7.keys():
    b7[word]=b7[word]/max(b7.values())
b8 = {}
for sentence in b5:
    for word in nltk.word_tokenize(sentence.lower()):
        if word in b7.keys():
            if len(sentence.split(' '))<25:
                if sentence not in b8.keys():
                    b8[sentence]=b7[word]
                else:
                    b8[sentence]+=b7[word]
b9 = heapq.nlargest(5,b8,key=b8.get)
print('------------------------------------------------------------')
for sentence in b9:
    print(sentence)