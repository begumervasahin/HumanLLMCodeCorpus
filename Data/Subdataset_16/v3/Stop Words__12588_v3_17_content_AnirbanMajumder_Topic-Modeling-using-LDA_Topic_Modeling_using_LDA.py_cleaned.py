import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from stop_words import get_stop_words
from gensim import corpora, models
import gensim
nltk.download('stopwords')
def fonk1(b13):
    b1 = RegexpTokenizer(r'\w+')
    b2 = get_stop_words('en')
    b3 = PorterStemmer()
    b4 = []
    for doc in b13:
        b5 = doc.lower()
        b6 = b1.tokenize(b5)
        b7 = [token for token in b6 if token not in b2]
        b8 = [b3.stem(token) for token in b7]
        b4.append(b8)
    return b4
def fonk2(b14):
    b9 = corpora.Dictionary(b14)
    b10 = [b9.doc2bow(text) for text in b14]
    return b9, b10
def fonk3(b10, b9, b11 = 2, passes=20):
    b12 = gensim.models.b12.LdaModel(b10, b11=b11, id2word=b9, passes=passes)
    return b12
def fonk4():
    b13 = [
        "Broccoli is good to eat. My brother likes to eat good broccoli, but not my mother.",
        "My mother spends a lot of time driving my brother around to baseball practice.",
        "Some health experts suggest that driving may cause increased tension and blood pressure.",
        "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better.",
        "Health professionals say that broccoli is good for your health."
    ]
    print("Document Set:\n", b13)
    b14 = fonk1(b13)
    print("\nTokenized and Stemmed Texts:\n", b14)
    b9, b10 = fonk2(b14)
    print("\nToken to ID Mapping:\n", b9.token2id)
    print("\nCorpus (Document-Term Matrix):\n", b10)
    b12 = fonk3(b10, b9, b11=2, passes=20)
    print("\nLDA Model Topics:")
    for idx, topic in b12.print_topics(b11 = 2, num_words=4):
        print(f"Topic {idx}: {topic}")
if b15 = = "__main__":
    fonk4()