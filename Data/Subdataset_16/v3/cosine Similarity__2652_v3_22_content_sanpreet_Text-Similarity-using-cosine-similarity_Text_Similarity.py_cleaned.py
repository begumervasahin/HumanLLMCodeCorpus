import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
import warnings
warnings.filterwarnings("ignore")
nltk.download('punkt')
class class1:
    def fonk1(self):
        self.b1 = nltk.stem.porter.PorterStemmer()
        self.b2 = dict((ord(char), None) for char in string.punctuation)
    def fonk2(self, tokens):
        return [self.b1.stem(item) for item in tokens]
    def fonk3(self, text):
        return self.fonk2(nltk.word_tokenize(text.lower().translate(self.b2)))
    def fonk4(self, b7, b8):
        b3 = TfidfVectorizer(tokenizer=self.normalize, stop_words='english')
        b4 = b3.fit_transform([b7, b8])
        b5 = ((b4 * b4.T).A)[0, 1]
        return b5
b6 = class1()
b7 = 'a little bird'
b8 = 'a little bird'
b9 = 'a little bird chirps'
b10 = 'a big dog barks'
print("Similarity between Text1 and Text2:", b6.fonk4(b7, b8))
print("Similarity between Text1 and Text3:", b6.fonk4(b7, b9))
print("Similarity between Text1 and Text4:", b6.fonk4(b7, b10))