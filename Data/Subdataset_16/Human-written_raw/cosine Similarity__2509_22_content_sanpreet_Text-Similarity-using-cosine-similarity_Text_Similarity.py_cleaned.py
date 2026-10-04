import nltk, string
import warnings
warnings.filterwarnings("ignore")
from sklearn.feature_extraction.text import TfidfVectorizer
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
		return ((b4 * b4.T).A)[0,1]
b5 = class1()
print("Text1", b5.fonk4('a little bird', 'a little bird'))
print("Text2", b5.fonk4('a little bird', 'a little bird chirps'))
print("Text3", b5.fonk4('a little bird', 'a big dog barks'))