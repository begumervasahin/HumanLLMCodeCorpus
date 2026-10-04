import nltk
import string
import warnings
from sklearn.feature_extraction.text import TfidfVectorizer
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
    def fonk4(self, b6, b7):
        b3 = TfidfVectorizer(tokenizer=self.normalize, stop_words='english')
        b4 = b3.fit_transform([b6, b7])
        return ((b4 * b4.T).A)[0, 1]
b5 = class1()
b6 = 'a little bird'
b7 = 'a little bird'
b8 = 'a little bird chirps'
b9 = 'a big dog barks'
print("Text1 vs. Text2 similarity:", b5.fonk4(b6, b7))
print("Text1 vs. Text3 similarity:", b5.fonk4(b6, b8))
print("Text1 vs. Text4 similarity:", b5.fonk4(b6, b9))