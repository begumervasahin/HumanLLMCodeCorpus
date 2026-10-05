import spacy
import nltk
nlp = spacy.load('en')
stemmer = nltk.stem.PorterStemmer()
def compare_normalization(text):
    doc = nlp(text)
    lemmatized_tokens = [token.lemma_ for token in doc]
    stemmed_tokens = [stemmer.stem(token.norm_.lower()) for token in doc]
    print("Lemmatization:\n{}".format(lemmatized_tokens))
    print("Stemming:\n{}".format(stemmed_tokens))
example_text = "Our meeting today was worse than yesterday, I'm scared of meeting the clients tomorrow"
compare_normalization(example_text)