
import spacy
import nltk
b1 = spacy.load('en')
b2 = nltk.stem.PorterStemmer()
def fonk1(text):
    b3 = b1(text)
    print("Lemmatization:")
    b4 = [token.lemma_ for token in b3]
    print(b4)
    print("Stemming:")
    b5 = [b2.stem(token.norm_.lower()) for token in b3]
    print(b5)
fonk1("Our meeting today was worse than yesterday, "
                      "I'm scared of meeting the clients tomorrow")