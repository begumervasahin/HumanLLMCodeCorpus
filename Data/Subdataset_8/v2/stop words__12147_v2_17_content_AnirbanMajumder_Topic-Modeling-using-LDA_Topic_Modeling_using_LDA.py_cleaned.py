
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from stop_words import get_stop_words
from gensim import corpora, models
tokenizer = RegexpTokenizer(r'\w+')
stop_words = get_stop_words('en')
stemmer = PorterStemmer()
document_a = "Broccoli is good to eat. My brother likes to eat good broccoli, but not my mother."
document_b = "My mother spends a lot of time driving my brother around to baseball practice."
document_c = "Some health experts suggest that driving may cause increased tension and blood pressure."
document_d = "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better."
document_e = "Health professionals say that broccoli is good for your health."
documents = [document_a, document_b, document_c, document_d, document_e]
tokenized_documents = []
for document in documents:
    lowercase_document = document.lower()
    tokens = tokenizer.tokenize(lowercase_document)
    meaningful_tokens = [token for token in tokens if token not in stop_words]
    stemmed_tokens = [stemmer.stem(token) for token in meaningful_tokens]
    tokenized_documents.append(stemmed_tokens)
dictionary = corpora.Dictionary(tokenized_documents)
corpus = [dictionary.doc2bow(tokens) for tokens in tokenized_documents]
lda_model = models.LdaModel(corpus, num_topics=2, id2word=dictionary, passes=20)
print(lda_model.print_topics(num_topics=2, num_words=4))