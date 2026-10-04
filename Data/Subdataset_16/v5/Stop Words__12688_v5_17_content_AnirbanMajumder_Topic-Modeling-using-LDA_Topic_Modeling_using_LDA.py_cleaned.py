
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from stop_words import get_stop_words
from gensim import corpora, models
import gensim
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
print("Sample Documents:", b4)
def fonk1(b4):
    b5 = []
    for doc in b4:
        b6 = doc.lower()
        b7 = b1.tokenize(b6)
        b8 = [token for token in b7 if token not in b2]
        b9 = [b3.stem(token) for token in b8]
        b5.append(b9)
    return b5
b5 = fonk1(b4)
print("Processed Texts:", b5)
b10 = corpora.Dictionary(b5)
print("Token IDs:", b10.token2id)
b11 = [b10.doc2bow(text) for text in b5]
print("Document-Term Matrix for First Document:", b11[0])
def fonk2(b11, b10, b12 = 2, passes=20):
    return gensim.models.b13.LdaModel(b11, b12 = b12, id2word=b10, passes=passes)
b13 = fonk2(b11, b10)
def fonk3(b13, b12 = 2, num_words=4):
    for idx, topic in b13.print_topics(b12 = b12, num_words=num_words):
        print(f"Topic {idx + 1}: {topic}")
print("LDA Model Topics:")
fonk3(b13)