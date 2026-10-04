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
    def fonk4(self, text1, text2):
        b3 = TfidfVectorizer(tokenizer=self.normalize, stop_words='english')
        b4 = b3.fit_transform([text1, text2])
        b5 = ((b4 * b4.T).A)[0, 1]
        return b5
b6 = class1()
print("Similarity between 'a little bird' and 'a little bird':", b6.fonk4('a little bird', 'a little bird'))
print("Similarity between 'a little bird' and 'a little bird chirps':", b6.fonk4('a little bird', 'a little bird chirps'))
print("Similarity between 'a little bird' and 'a big dog barks':", b6.fonk4('a little bird', 'a big dog barks'))