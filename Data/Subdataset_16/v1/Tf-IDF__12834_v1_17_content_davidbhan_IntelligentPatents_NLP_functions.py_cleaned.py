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
    b3 = [word for word in b2 if word not in stopwords.words('english')]
    b4 = WordNetLemmatizer()
    b5 = ' '.join([b4.lemmatize(word) for word in b3])
    return b5
def fonk2(text1, text2):
    b6 = TfidfVectorizer(min_df=1)
    b7 = b6.fit_transform([text1, text2])
    return (b7 * b7.T).A[0, 1]
print(fonk2("hello I'm David, and I love my little bunny \n asdf this code", "hello I'm Juwon, and I love my big bear"))
print(fonk2(fonk1("hello I'm David, and I love my little bunny"), fonk1("hello I'm Juwon, and I love my big bear")))
print(fonk1("hello I'm David, I was born on the best day of the best month because I'm the best of them all!"))