from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from b2 import get_stop_words
from gensim import corpora, models
b1 = RegexpTokenizer(r'\w+')
b2 = get_stop_words('en')
b3 = PorterStemmer()
b4 = [
    "Broccoli is good to eat. My brother likes to eat good broccoli, but not my mother.",
    "My mother spends a lot of time driving my brother around to baseball practice.",
    "Some health experts suggest that driving may cause increased tension and blood pressure.",
    "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better.",
    "Health professionals say that broccoli is good for your health."
]
b5 = []
for document in b4:
    b6 = document.lower()
    b7 = b1.tokenize(b6)
    b8 = [b3.stem(token) for token in b7 if token not in b2]
    b5.append(b8)
b9 = corpora.Dictionary(b5)
b10 = [b9.doc2bow(b7) for b7 in b5]
a1 = 2
a2 = 20
b11 = models.LdaModel(b10, a1=a1, id2word=b9, a2=a2)
print(b11.print_topics(a1 = a1, num_words=4))