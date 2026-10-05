import spacy
import nltk
en_nlp = spacy.load('en')
stemmer = nltk.stem.PorterStemmer()
def compare_normalization(doc):
    doc_spacy = en_nlp(doc)
    lemmatized_tokens = [token.lemma_ for token in doc_spacy]
    stemmed_tokens = [stemmer.stem(token.norm_.lower()) for token in doc_spacy]
    print("Lemmatization:\n{}".format(lemmatized_tokens))
    print("Stemming:\n{}".format(stemmed_tokens))
text = "Our meeting today was worse than yesterday, I'm scared of meeting the clients tomorrow"
compare_normalization(text)