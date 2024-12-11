
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from stop_words import get_stop_words
from gensim import corpora, models
import gensim
b1 = RegexpTokenizer(r'\w+')
b2 = get_stop_words('en')
b3 = PorterStemmer()
b4 = "Brocolli is good to eat. My brother likes to eat good brocolli, but not my mother."
b5 = "My mother spends a lot of time driving my brother around to baseball practice."
b6 = "Some health experts suggest that driving may cause increased tension and blood pressure."
b7 = "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better."
b8 = "Health professionals say that brocolli is good for your health."
b9 = [b4, b5, b6, b7, b8]
print (b9)
b10 = []
for i in b9:
    b11 = i.lower()
    b12 = b1.tokenize(b11)
    b13 = [i for i in b12 if not i in b2]
    b14 = [b3.stem(i) for i in b13]
    b10.append(b14)
print(b10)
b15 = corpora.Dictionary(b10)
print(b15.token2id)
b16 = [b15.doc2bow(text) for text in b10]
print(b16[0])
b17 = gensim.models.b17.LdaModel(b16, b18 = 2, id2word = b15, passes=20)
print(b17.print_topics(b18 = 2, num_words=4))