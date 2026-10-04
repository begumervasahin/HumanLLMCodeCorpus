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
    def fonk2(self, b3):
        return [self.b1.stem(item) for item in b3]
    def fonk3(self, text):
        b3 = nltk.word_tokenize(text.lower().translate(self.b2))
        return self.fonk2(b3)
    def fonk4(self, text1, text2):
        b4 = TfidfVectorizer(tokenizer=self.normalize, stop_words='english')
        b5 = b4.fit_transform([text1, text2])
        b6 = ((b5 * b5.T).A)[0, 1]
        return b6
b7 = class1()
b8 = [
    ('a little bird', 'a little bird'),
    ('a little bird', 'a little bird chirps'),
    ('a little bird', 'a big dog barks')
]
for text1, text2 in b8:
    print(f"Similarity between '{text1}' and '{text2}':", b7.fonk4(text1, text2))