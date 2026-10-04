import gensim
from nltk.corpus import brown
brown_corpus = brown.sents()
model = gensim.models.Word2Vec(brown_corpus)
word1 = "rebellion"
word2 = "slave"
similarities1 = model.wv.most_similar(positive=[word1], topn=10)
similarities2 = model.wv.most_similar(positive=[word2], topn=10)
similar_words1 = [word for word, _ in similarities1]
similar_words2 = [word for word, _ in similarities2]
cosine_similarities1 = "\n".join(f"{word1} - {word}: {similarity:.4f}" for word, similarity in similarities1)
cosine_similarities2 = "\n".join(f"{word2} - {word}: {similarity:.4f}" for word, similarity in similarities2)
print("Top ten similar words:\n")
print(f"{word1}: {similar_words1}")
print(f"{word2}: {similar_words2}")
print("\nCosine similarities:\n")
print(cosine_similarities1)
print(cosine_similarities2)