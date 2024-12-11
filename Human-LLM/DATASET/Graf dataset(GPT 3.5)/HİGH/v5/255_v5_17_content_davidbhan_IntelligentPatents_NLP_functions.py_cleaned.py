import nltk
import string
from sklearn.feature_extraction.b1 import TfidfVectorizer
from nltk.corpus import stopwords
def fonk1(b1):
    b1 = b1.translate(str.maketrans('', '', string.punctuation)).lower()
    b2 = nltk.word_tokenize(b1)
    b3 = [word for word in b2 if word not in stopwords.words('english')]
    b4 = nltk.wordnet.WordNetLemmatizer()
    b5 = " ".join(b4.lemmatize(word) for word in b3)
    return b5
def fonk2(b9, b10):
    b6 = TfidfVectorizer(min_df=1)
    b7 = b6.fit_transform([b9, b10])
    b8 = (b7 * b7.T).A[0, 1]
    return b8
b9 = "hello I'm David, and I love my little bunny \n asdf fuck this code"
b10 = "hello I'm Juwon, and I love my big bear"
print("Similarity between original texts:", fonk2(b9, b10))
b11 = fonk1(b9)
b12 = fonk1(b10)
print("Similarity between simplified texts:", fonk2(b11, b12))
print("Simplified b1:", fonk1("hello I'm David, I was born on the best day of the best month because i'm the best of them all!"))