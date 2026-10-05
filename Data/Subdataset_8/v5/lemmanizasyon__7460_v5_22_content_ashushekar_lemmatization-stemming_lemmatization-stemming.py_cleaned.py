
import spacy
import nltk
english_nlp = spacy.load('en')
porter_stemmer = nltk.stem.PorterStemmer()
def compare_normalization(text):
    doc = english_nlp(text)
    print("Lemmatization:")
    lemmatized_tokens = [token.lemma_ for token in doc]
    print(lemmatized_tokens)
    print("Stemming:")
    stemmed_tokens = [porter_stemmer.stem(token.norm_.lower()) for token in doc]
    print(stemmed_tokens)
compare_normalization("Our meeting today was worse than yesterday, "
                      "I'm scared of meeting the clients tomorrow")