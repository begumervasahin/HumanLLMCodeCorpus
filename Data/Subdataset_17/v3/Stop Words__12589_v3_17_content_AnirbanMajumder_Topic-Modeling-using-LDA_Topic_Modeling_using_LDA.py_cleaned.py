import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from stop_words import get_stop_words
from gensim import corpora, models
import gensim
nltk.download('stopwords')
def preprocess_documents(documents):
    tokenizer = RegexpTokenizer(r'\w+')
    en_stop = get_stop_words('en')
    p_stemmer = PorterStemmer()
    processed_texts = []
    for doc in documents:
        raw = doc.lower()
        tokens = tokenizer.tokenize(raw)
        stopped_tokens = [token for token in tokens if token not in en_stop]
        stemmed_tokens = [p_stemmer.stem(token) for token in stopped_tokens]
        processed_texts.append(stemmed_tokens)
    return processed_texts
def create_dictionary_and_corpus(texts):
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    return dictionary, corpus
def perform_lda_analysis(corpus, dictionary, num_topics=2, passes=20):
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=passes)
    return ldamodel
def main():
    documents = [
        "Broccoli is good to eat. My brother likes to eat good broccoli, but not my mother.",
        "My mother spends a lot of time driving my brother around to baseball practice.",
        "Some health experts suggest that driving may cause increased tension and blood pressure.",
        "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better.",
        "Health professionals say that broccoli is good for your health."
    ]
    print("Document Set:\n", documents)
    texts = preprocess_documents(documents)
    print("\nTokenized and Stemmed Texts:\n", texts)
    dictionary, corpus = create_dictionary_and_corpus(texts)
    print("\nToken to ID Mapping:\n", dictionary.token2id)
    print("\nCorpus (Document-Term Matrix):\n", corpus)
    ldamodel = perform_lda_analysis(corpus, dictionary, num_topics=2, passes=20)
    print("\nLDA Model Topics:")
    for idx, topic in ldamodel.print_topics(num_topics=2, num_words=4):
        print(f"Topic {idx}: {topic}")
if __name__ == "__main__":
    main()