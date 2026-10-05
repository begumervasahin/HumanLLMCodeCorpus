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
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
    def takeVerbNoun(self, text):
        tagged_tokens = pos_tag(word_tokenize(text))
        return " ".join([token for token, pos in tagged_tokens if pos in ['NN', 'VB']])
    def word_token(self, tokens, lemma=False):
        tokens = str(tokens)
        tokens = re.sub(r"([\w].)([\~\!\@\
        tokens = re.sub(r"\s+", " ", tokens)
        if lemma:
            return " ".join([self.lemmatizer.lemmatize(token.lower(), 'v') for token in word_tokenize(tokens) if token.lower() not in self.stop_words and token.isalpha()])
        else:
            return " ".join([token.lower() for token in word_tokenize(tokens) if token.lower() not in self.stop_words and token.isalpha()])
    def tfIdfVectorizer(self, jd, resume):
        cosine_similarities = ''
        try:
            print("\n TF-IDF Vectorizer --- ")
            print("\n JD --- ", jd, len(jd))
            print("\n Resume --- ", resume, len(resume))
            common_words = list(set(jd.split()) & set(resume.split()))
            print("\n Common words --- ", common_words, len(common_words))
            vectorizer = TfidfVectorizer(use_idf=True, sublinear_tf=True, lowercase=True)
            jd_vector = [jd]
            jd_vector = vectorizer.fit_transform(jd_vector)
            resume_vector = vectorizer.transform([resume])
            cosine_similarities = cosine_similarity(jd_vector, resume_vector).flatten()[0]
            print("\n TF-IDF similarity --- ", cosine_similarities)
        except Exception as e:
            print("\n Error in tfIdfVectorizer():", e, "\n", traceback.format_exc())
        return cosine_similarities
    def main(self, jd, resume):
        jd = self.word_token(jd, True)
        resume = self.word_token(resume, True)
        resume = self.takeVerbNoun(resume)
        return self.tfIdfVectorizer(jd, resume)
    def test(self):
        jd = "Sample job description text"
        resume = "Sample resume text"
        self.main(jd, resume)
if __name__ == '__main__':
    obj = TfIdfSimilarity()
    obj.test()