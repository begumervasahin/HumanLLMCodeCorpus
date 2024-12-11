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
    b4 = nltk.wordnet.WordNetLemmatizer()
    b5 = [b4.lemmatize(word) for word in b2 if word not in b3]
    b6 = " ".join(b5)
    return b6
def fonk2(b10, b11):
    b7 = TfidfVectorizer(min_df=1)
    b8 = b7.fit_transform([b10, b11])
    b9 = (b8 * b8.T).A[0, 1]
    return b9
b10 = "hello I'm David, and I love my little bunny \n asdf fuck this code"
b11 = "hello I'm Juwon, and I love my big bear"
print("Similarity between b10 and b11:", fonk2(b10, b11))
print("Similarity after simplification:", fonk2(fonk1(b10), fonk1(b11)))
print("Example of simplified b1:", fonk1("hello I'm David, I was born on the best day of the best month because i'm the best of them all!"))