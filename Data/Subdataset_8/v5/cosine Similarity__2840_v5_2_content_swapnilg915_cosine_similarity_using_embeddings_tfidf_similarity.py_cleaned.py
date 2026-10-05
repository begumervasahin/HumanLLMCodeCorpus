import json
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
class TfIdfSimilarity:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
    def take_verb_noun(self, text):
        tagged_tokens = pos_tag(word_tokenize(text))
        return " ".join([token for token, pos in tagged_tokens if pos in ['NN', 'VB']])
    def word_token(self, tokens, lemma=False):
        tokens = str(tokens)
        tokens = re.sub(r"([\w].)([\~\!\@\
        tokens = re.sub(r"\s+", " ", tokens)
        tokens = word_tokenize(tokens.lower())
        if lemma:
            tokens = [self.lemmatizer.lemmatize(token, 'v') for token in tokens if token not in self.stop_words and token.isalpha()]
        else:
            tokens = [token for token in tokens if token not in self.stop_words and token.isalpha()]
        return " ".join(tokens)
    def tfidf_vectorizer(self, jd_text, resume_text):
        try:
            vectorizer = TfidfVectorizer(use_idf=True, sublinear_tf=True, lowercase=True)
            jd_vector = vectorizer.fit_transform([jd_text])
            resume_vector = vectorizer.transform([resume_text])
            cosine_similarities = cosine_similarity(jd_vector, resume_vector).flatten()[0]
            return cosine_similarities
        except Exception as e:
            print("\n Error in tfidf_vectorizer():", e)
    def main(self, jd_text, resume_text):
        jd_text = self.word_token(jd_text, True)
        resume_text = self.word_token(resume_text, True)
        resume_text = self.take_verb_noun(resume_text)
        return self.tfidf_vectorizer(jd_text, resume_text)
    def test(self):
        jd_text = "Sample job description text"
        resume_text = "Sample resume text"
        similarity_score = self.main(jd_text, resume_text)
        if similarity_score:
            print("\n TF-IDF similarity:", similarity_score)
if __name__ == '__main__':
    obj = TfIdfSimilarity()
    obj.test()