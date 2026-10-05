
import spacy
import nltk
en_nlp = spacy.load('en')
stemmer = nltk.stem.PorterStemmer()
def compare_normalization(doc):
    doc_spacy = en_nlp(doc)
    print("Lemmatization:")
    lemmatized_tokens = [token.lemma_ for token in doc_spacy]
    print(lemmatized_tokens)
    print("Stemming:")
    stemmed_tokens = [stemmer.stem(token.norm_.lower()) for token in doc_spacy]
    print(stemmed_tokens)
compare_normalization("Our meeting today was worse than yesterday, "
                      "I'm scared of meeting the clients tomorrow")