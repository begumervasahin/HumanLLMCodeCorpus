import regex as re
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from keras import backend as K
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from abydos.distance import Jaccard
class ElmoSimilarity(object):
	def __init__(self):
		self.stop_words = list(stopwords.words('english'))
		self.lemmatizer = WordNetLemmatizer()
		self.jaccard_sim_obj = Jaccard()
		self.elmo = hub.Module("https:
	def word_token(self, tokens, lemma=False):
		tokens = str(tokens)
		tokens = re.sub(r"([\w].)([\~\!\@\
		tokens = re.sub(r"\s+", " ", tokens)
		if lemma:
			return " ".join([self.lemmatizer.lemmatize(token, 'v') for token in word_tokenize(tokens.lower()) if token not in self.stop_words and token.isalpha()])
		else:
			return " ".join([token for token in word_tokenize(tokens.lower()) if token not in self.stop_words and token.isalpha()])
	def cos_sim(self, a, b):
		return np.inner(a, b) / (np.linalg.norm(a) * (np.linalg.norm(b)))
	def embed(self, sentences):
		elmo = hub.Module("https:
		executable = elmo(
			sentences,
			signature="default",
			as_dict=True)["elmo"]
		return self.execute(executable)[0]
	def execute(self, tensor):
		with tf.Session() as sess:
			sess.run(tf.global_variables_initializer())
			sess.run(tf.tables_initializer())
			return sess.run(tensor)
	def word_to_sentence(self, embeddings):
		return embeddings.sum(axis=1)
	def main(self):
		jd = 'machine learning'
		resume = 'lead learning'
		print("==="*25)
		print("\n ", jd, "\n ",resume)
		jd_embeddings = self.embed([jd])
		print("\n jd_embeddings --- ",jd_embeddings, jd_embeddings.shape)
		resume_embeddings = self.embed([resume])
		sim = self.cos_sim(jd_embeddings, resume_embeddings)
		print("\n elmo similarity --- ", sim)
if __name__ == '__main__':
	obj = ElmoSimilarity()
	obj.main()
