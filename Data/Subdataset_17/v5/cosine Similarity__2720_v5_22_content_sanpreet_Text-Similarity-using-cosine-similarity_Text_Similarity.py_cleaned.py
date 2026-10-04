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
        tokens = nltk.word_tokenize(text.lower().translate(self.remove_punctuation_map))
        return self.stem_tokens(tokens)
    def cosine_similarity(self, text1, text2):
        vectorizer = TfidfVectorizer(tokenizer=self.normalize, stop_words='english')
        tfidf = vectorizer.fit_transform([text1, text2])
        similarity = ((tfidf * tfidf.T).A)[0, 1]
        return similarity
document_similarity = DocumentSimilarity()
text_pairs = [
    ('a little bird', 'a little bird'),
    ('a little bird', 'a little bird chirps'),
    ('a little bird', 'a big dog barks')
]
for text1, text2 in text_pairs:
    print(f"Similarity between '{text1}' and '{text2}':", document_similarity.cosine_similarity(text1, text2))