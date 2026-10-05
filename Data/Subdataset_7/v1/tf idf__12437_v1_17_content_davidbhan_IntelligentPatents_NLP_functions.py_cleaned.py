import nltk
import string
from sklearn.feature_extraction.b1 import TfidfVectorizer
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
def fonk1(b1):
    b1 = b1.translate(str.maketrans('', '', string.punctuation)).lower()
    b2 = nltk.word_tokenize(b1)
    b3 = set(stopwords.words('english'))
    b4 = [word for word in b2 if word not in b3]
    b5 = nltk.wordnet.WordNetLemmatizer()
    b6 = " ".join([b5.lemmatize(word) for word in b4])
    return b6
def fonk2(b9, b10):
    b7 = TfidfVectorizer(min_df=1)
    b8 = b7.fit_transform([b9, b10])
    return (b8 * b8.T).A[0,1]
b9 = "hello I'm David, and I love my little bunny \n asdf fuck this code"
b10 = "hello I'm Juwon, and I love my big bear"
print(fonk2(b9, b10))
print(fonk2(fonk1(b9), fonk1(b10)))
print(fonk1("hello I'm David, I was born on the best day of the best month because i'm the best of them all!"))