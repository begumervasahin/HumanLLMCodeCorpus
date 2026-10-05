import regex as re
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from abydos.distance import Jaccard
class ElmoSimilarity:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.jaccard_sim_obj = Jaccard()
        self.elmo = hub.Module("https:
    def word_token(self, tokens, lemma=False):
        tokens = str(tokens)
        tokens = re.sub(r"([\w].)([\~\!\@\
        tokens = re.sub(r"\s+", " ", tokens)
        tokens = word_tokenize(tokens.lower())
        if lemma:
            tokens = [self.lemmatizer.lemmatize(token, 'v') for token in tokens if token.isalpha() and token not in self.stop_words]
        else:
            tokens = [token for token in tokens if token.isalpha() and token not in self.stop_words]
        return " ".join(tokens)
    def cos_sim(self, a, b):
        return np.inner(a, b) / (np.linalg.norm(a) * (np.linalg.norm(b)))
    def embed(self, sentences):
        executable = self.elmo(sentences, signature="default", as_dict=True)["elmo"]
        with tf.Session() as sess:
            sess.run([tf.global_variables_initializer(), tf.tables_initializer()])
            return sess.run(executable)[0]
    def word_to_sentence(self, embeddings):
        return embeddings.sum(axis=1)
    def main(self):
        jd = 'machine learning'
        resume = 'lead learning'
        print("=" * 75)
        print("\n Job Description:\n", jd, "\n Resume:\n", resume)
        jd_embeddings = self.embed([self.word_token(jd)])
        print("\n Job Description Embeddings:\n", jd_embeddings, "\n Shape:", jd_embeddings.shape)
        resume_embeddings = self.embed([self.word_token(resume)])
        sim = self.cos_sim(jd_embeddings, resume_embeddings)
        print("\n ELMo Cosine Similarity between Job Description and Resume:\n", sim)
if __name__ == '__main__':
    obj = ElmoSimilarity()
    obj.main()