import bs4 as bs
import urllib.request
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq
nltk.download('stopwords')
nltk.download('punkt')
source = urllib.request.urlopen('https:
soup = bs.BeautifulSoup(source, 'lxml')
text = ""
for paragraph in soup.find_all('p'):
    text += paragraph.text
text = re.sub(r'\[[0-9]*\]', ' ', text)
text = re.sub(r'\s+', ' ', text)
clean_text = text.lower()
clean_text = re.sub(r'\W', ' ', clean_text)
clean_text = re.sub(r'\d', ' ', clean_text)
clean_text = re.sub(r'\s+', ' ', clean_text)
sentences = sent_tokenize(text)
stop_words = set(stopwords.words('english'))
word2count = {}
for word in word_tokenize(clean_text):
    if word not in stop_words:
        if word not in word2count.keys():
            word2count[word] = 1
        else:
            word2count[word] += 1
max_freq = max(word2count.values())
for word in word2count.keys():
    word2count[word] = word2count[word] / max_freq
sent2score = {}
for sentence in sentences:
    for word in word_tokenize(sentence.lower()):
        if word in word2count.keys():
            if len(sentence.split(' ')) < 25:
                if sentence not in sent2score.keys():
                    sent2score[sentence] = word2count[word]
                else:
                    sent2score[sentence] += word2count[word]
best_sentences = heapq.nlargest(5, sent2score, key=sent2score.get)
print('------------------------------------------------------------')
for sentence in best_sentences:
    print(sentence)