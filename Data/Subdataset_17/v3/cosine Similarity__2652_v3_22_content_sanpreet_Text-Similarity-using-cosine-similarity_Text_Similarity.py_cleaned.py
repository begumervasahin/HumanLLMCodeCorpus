import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
import warnings
warnings.filterwarnings("ignore")
nltk.download('punkt')
class DocumentSimilarity:
    def __init__(self):
        self.stemmer = nltk.stem.porter.PorterStemmer()
        self.remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
    def stem_tokens(self, tokens):
        return [self.stemmer.stem(item) for item in tokens]
    def normalize(self, text):
        return self.stem_tokens(nltk.word_tokenize(text.lower().translate(self.remove_punctuation_map)))
    def cosine_similarity(self, text1, text2):
        vectorizer = TfidfVectorizer(tokenizer=self.normalize, stop_words='english')
        tfidf = vectorizer.fit_transform([text1, text2])
        similarity = ((tfidf * tfidf.T).A)[0, 1]
        return similarity
document_similarity = DocumentSimilarity()
text1 = 'a little bird'
text2 = 'a little bird'
text3 = 'a little bird chirps'
text4 = 'a big dog barks'
print("Similarity between Text1 and Text2:", document_similarity.cosine_similarity(text1, text2))
print("Similarity between Text1 and Text3:", document_similarity.cosine_similarity(text1, text3))
print("Similarity between Text1 and Text4:", document_similarity.cosine_similarity(text1, text4))