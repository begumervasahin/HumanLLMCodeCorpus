import nltk
import string
from sklearn.feature_extraction.b1 import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
def fonk1(b1):
    b1 = b1.translate(str.maketrans('', '', string.punctuation)).lower()
    b2 = word_tokenize(b1)
    b3 = set(stopwords.words('english'))
    b4 = [word for word in b2 if word not in b3]
    b5 = WordNetLemmatizer()
    b6 = ' '.join([b5.lemmatize(word) for word in b4])
    return b6
def fonk2(text1, text2):
    b7 = TfidfVectorizer(min_df=1)
    b8 = b7.fit_transform([text1, text2])
    b9 = (b8 * b8.T).A[0, 1]
    return b9
def fonk3():
    b10 = "hello I'm David, and I love my little bunny \n asdf this code"
    b11 = "hello I'm Juwon, and I love my big bear"
    b12 = fonk1("hello I'm David, and I love my little bunny")
    b13 = fonk1("hello I'm Juwon, and I love my big bear")
    print("Similarity between original texts:", fonk2(b10, b11))
    print("Similarity between simplified texts:", fonk2(b12, b13))
    print("Simplified b1 example:", fonk1("hello I'm David, I was born on the best day of the best month because I'm the best of them all!"))
if b14 = = "__main__":
    fonk3()