import json
import os
import traceback
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
class TfIdfSimilarity:
    def __init__(self):
        self.stop_words = list(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
    def take_verb_noun(self, text):
        tagged_tokens = pos_tag(word_tokenize(text))
        return " ".join([token for token, pos in tagged_tokens if pos in ['NN', 'VB']])
    def word_token(self, tokens, lemma=False):
        tokens = str(tokens)
        tokens = re.sub(r"([\w].)([\~\!\@\
        tokens = re.sub(r"\s+", " ", tokens)
        if lemma:
            tokens = word_tokenize(tokens.lower())
            tokens = [self.lemmatizer.lemmatize(token, 'v') for token in tokens if token not in self.stop_words and token.isalpha()]
            return " ".join(tokens)
        else:
            tokens = word_tokenize(tokens.lower())
            tokens = [token for token in tokens if token not in self.stop_words and token.isalpha()]
            return " ".join(tokens)
    def tfidf_vectorizer(self, jd, resume):
        cosine_similarities = ''
        try:
            print("\n TF-IDF Vectorizer --- ")
            print("\n JD --- ", jd, len(jd))
            print("\n Resume --- ", resume, len(resume))
            common_words = set(jd.split()) & set(resume.split())
            print("\n Common words --- ", common_words, len(common_words))
            vectorizer = TfidfVectorizer(use_idf=True, sublinear_tf=True, lowercase=True)
            jd_vector = vectorizer.fit_transform([jd])
            resume_vector = vectorizer.transform([resume])
            cosine_similarities = cosine_similarity(jd_vector, resume_vector).flatten()[0]
            print("\n TF-IDF similarity --- ", cosine_similarities)
        except Exception as e:
            print("\n Error in tfidf_vectorizer():", e, "\n", traceback.format_exc())
        return cosine_similarities
    def main(self, jd, resume):
        jd = self.word_token(jd, True)
        resume = self.word_token(resume, True)
        resume = self.take_verb_noun(resume)
        return self.tfidf_vectorizer(jd, resume)
    def test(self):
        jd = "Sample job description text"
        resume = "Sample resume text"
        self.main(jd, resume)
if __name__ == '__main__':
    obj = TfIdfSimilarity()
    obj.test()