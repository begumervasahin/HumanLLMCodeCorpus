
import nltk, string, numpy
b1 = nltk.stem.porter.PorterStemmer()
def fonk1(tokens):
     return [b1.stem(token) for token in tokens]
b2 = dict((ord(punct), None) for punct in string.punctuation)
def fonk2(text):
     return fonk1(nltk.word_tokenize(text.lower().translate(b2)))
 b3 = nltk.stem.WordNetLemmatizer()
 def fonk3(tokens):
     return [b3.lemmatize(token) for token in tokens]
 b2 = dict((ord(punct), None) for punct in string.punctuation)
 def fonk4(text):
     return fonk3(nltk.word_tokenize(text.lower().translate(b2)))
 from sklearn.feature_extraction.text import CountVectorizer
 b4 = CountVectorizer(tokenizer=LemNormalize, stop_words='english')
 b4.fit_transform(dataAll)
print (b4.vocabulary_)
b5 = b4.transform(documents).toarray()
print (b5)
 from sklearn.feature_extraction.text import TfidfTransformer
 b6 = TfidfTransformer(norm="l2")
 b6.fit(b5)
 print (b6.idf_)
 b7 = b6.transform(b5)
print (b7.toarray())
b8 = (b7 * b7.T).toarray()
print (b8)
from sklearn.feature_extraction.text import TfidfVectorizer
b9 = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
def fonk5(textlist):
    b10 = b9.fit_transform(textlist)
    return (b10 * b10.T).toarray()
fonk5(dataAll)