
import spacy
import nltk
b1 = spacy.load('en')
b2 = nltk.stem.PorterStemmer()
def fonk1(text_to_process):
    b3 = b1(text_to_process)
    b4 = [token.lemma_ for token in b3]
    b5 = [b2.stem(token.norm_.lower()) for token in b3]
    print("Lemmatization:\n{}".format(b4))
    print("Stemming:\n{}".format(b5))
b6 = "Our meeting today was worse than yesterday, I'm scared of meeting the clients tomorrow"
fonk1(b6)