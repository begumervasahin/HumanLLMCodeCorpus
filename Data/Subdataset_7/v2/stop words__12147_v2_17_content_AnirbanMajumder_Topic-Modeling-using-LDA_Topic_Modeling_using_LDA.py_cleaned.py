
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from b2 import get_stop_words
from gensim import corpora, models
b1 = RegexpTokenizer(r'\w+')
b2 = get_stop_words('en')
b3 = PorterStemmer()
b4 = "Broccoli is good to eat. My brother likes to eat good broccoli, but not my mother."
b5 = "My mother spends a lot of time driving my brother around to baseball practice."
b6 = "Some health experts suggest that driving may cause increased tension and blood pressure."
b7 = "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better."
b8 = "Health professionals say that broccoli is good for your health."
b9 = [b4, b5, b6, b7, b8]
b10 = []
for document in b9:
    b11 = document.lower()
    b12 = b1.tokenize(b11)
    b13 = [token for token in b12 if token not in b2]
    b14 = [b3.stem(token) for token in b13]
    b10.append(b14)
b15 = corpora.Dictionary(b10)
b16 = [b15.doc2bow(b12) for b12 in b10]
b17 = models.LdaModel(b16, b18=2, id2word=b15, passes=20)
print(b17.print_topics(b18 = 2, num_words=4))