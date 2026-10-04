
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from stop_words import get_stop_words
from gensim import corpora, models
import gensim
tokenizer = RegexpTokenizer(r'\w+')
en_stop = get_stop_words('en')
p_stemmer = PorterStemmer()
documents = [
    "Broccoli is good to eat. My brother likes to eat good broccoli, but not my mother.",
    "My mother spends a lot of time driving my brother around to baseball practice.",
    "Some health experts suggest that driving may cause increased tension and blood pressure.",
    "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better.",
    "Health professionals say that broccoli is good for your health."
]
print("Sample Documents:", documents)
def preprocess_documents(documents):
    texts = []
    for doc in documents:
        raw = doc.lower()
        tokens = tokenizer.tokenize(raw)
        stopped_tokens = [token for token in tokens if token not in en_stop]
        stemmed_tokens = [p_stemmer.stem(token) for token in stopped_tokens]
        texts.append(stemmed_tokens)
    return texts
texts = preprocess_documents(documents)
print("Processed Texts:", texts)
dictionary = corpora.Dictionary(texts)
print("Token IDs:", dictionary.token2id)
corpus = [dictionary.doc2bow(text) for text in texts]
print("Document-Term Matrix for First Document:", corpus[0])
def generate_lda_model(corpus, dictionary, num_topics=2, passes=20):
    return gensim.models.ldamodel.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=passes)
ldamodel = generate_lda_model(corpus, dictionary)
def print_lda_topics(ldamodel, num_topics=2, num_words=4):
    for idx, topic in ldamodel.print_topics(num_topics=num_topics, num_words=num_words):
        print(f"Topic {idx + 1}: {topic}")
print("LDA Model Topics:")
print_lda_topics(ldamodel)