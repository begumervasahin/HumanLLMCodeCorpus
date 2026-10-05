from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from stop_words import get_stop_words
from gensim import corpora, models
tokenizer = RegexpTokenizer(r'\w+')
stop_words = get_stop_words('en')
stemmer = PorterStemmer()
documents = [
    "Broccoli is good to eat. My brother likes to eat good broccoli, but not my mother.",
    "My mother spends a lot of time driving my brother around to baseball practice.",
    "Some health experts suggest that driving may cause increased tension and blood pressure.",
    "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better.",
    "Health professionals say that broccoli is good for your health."
]
tokenized_documents = []
for document in documents:
    lowercase_document = document.lower()
    tokens = tokenizer.tokenize(lowercase_document)
    meaningful_stemmed_tokens = [stemmer.stem(token) for token in tokens if token not in stop_words]
    tokenized_documents.append(meaningful_stemmed_tokens)
dictionary = corpora.Dictionary(tokenized_documents)
corpus = [dictionary.doc2bow(tokens) for tokens in tokenized_documents]
num_topics = 2
passes = 20
lda_model = models.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=passes)
print(lda_model.print_topics(num_topics=num_topics, num_words=4))