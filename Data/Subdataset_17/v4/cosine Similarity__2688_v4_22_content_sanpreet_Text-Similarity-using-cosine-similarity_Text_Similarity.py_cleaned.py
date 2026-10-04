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
print("Similarity between 'a little bird' and 'a little bird':", document_similarity.cosine_similarity('a little bird', 'a little bird'))
print("Similarity between 'a little bird' and 'a little bird chirps':", document_similarity.cosine_similarity('a little bird', 'a little bird chirps'))
print("Similarity between 'a little bird' and 'a big dog barks':", document_similarity.cosine_similarity('a little bird', 'a big dog barks'))