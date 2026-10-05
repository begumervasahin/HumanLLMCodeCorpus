import re
import numpy as np
import spacy
from spacy.lang.en.stop_words import STOP_WORDS as stopwords_en
class SpacySimilarity:
    def __init__(self):
        self.spacy_large_model = spacy.load("en_core_web_lg")
    def clean_text(self, text):
        try:
            text = str(text)
            text = re.sub(r"[^A-Za-z0-9]", " ", text)
            text = re.sub(r"\s+", " ", text)
            text = text.lower().strip()
        except Exception as e:
            print("\n Error in clean_text:", e)
            print("\n Error sent:", text)
        return text
    def get_lemma_tokens(self, text):
        lemmatized_tokens = [token.lemma_.lower().strip() for token in spacy_en(text)
                             if (token.lemma_ != '-PRON-' and token.lemma_ not in stopwords_en and len(token.lemma_)>1)]
        return " ".join(lemmatized_tokens)
    def cleaning_pipeline(self, text):
        text = self.clean_text(text)
        text = self.get_lemma_tokens(text)
        return text
    def cos_sim(self, vector_1, vector_2):
        return np.inner(vector_1, vector_2) / (np.linalg.norm(vector_1) * (np.linalg.norm(vector_2)))
    def main(self, sent1, sent2):
        sent1_cleaned = self.cleaning_pipeline(sent1)
        sent2_cleaned = self.cleaning_pipeline(sent2)
        sent1_vector = self.spacy_large_model(sent1_cleaned).vector
        sent2_vector = self.spacy_large_model(sent2_cleaned).vector
        cosine_sim = self.cos_sim(sent1_vector, sent2_vector)
        print("\n Spacy Cosine Similarity:", cosine_sim)
if __name__ == '__main__':
    obj = SpacySimilarity()
    sent1 = "booking a flight is very easy"
    sent2 = "reading a book is a good habit"
    obj.main(sent1, sent2)