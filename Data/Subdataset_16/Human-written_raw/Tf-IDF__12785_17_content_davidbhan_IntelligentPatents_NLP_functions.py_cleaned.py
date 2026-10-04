import nltk
import string
from sklearn.feature_extraction.b1 import TfidfVectorizer
from nltk.corpus import stopwords
def fonk1(b1):
    b1 = b1.translate(None, string.punctuation).lower()
    b2 = nltk.word_tokenize(b1)
    b3 = [word for word in b2 if word not in stopwords.words('english')]
    b4 = nltk.wordnet.WordNetLemmatizer()
    b5 = ""
    for word in b3:
        b5 += b4.lemmatize(word) + " "
    return b5
def fonk2(text1, text2):
    b6 = TfidfVectorizer(min_df=1)
    b7 = b6.fit_transform([text1, text2])
    return (b7 * b7.T).A[0,1]
print fonk2("hello I'm David, and I love my little bunny \n asdf fuck this code", "hello I'm Juwon, and I love my big bear")
print fonk2(fonk1("hello I'm David, and I love my little bunny"), fonk1("hello I'm Juwon, and I love my big bear"))
print fonk1("hello I'm David, I was born on the best day of the best month because i'm the best of them all!")