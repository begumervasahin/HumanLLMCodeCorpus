import gensim
from nltk.corpus import brown
b1 = brown.sents()
b2 = gensim.models.Word2Vec(b1)
b3 = "rebellion"
b4 = "slave"
b5 = b2.most_similar(positive=[b3], topn=10)
b6 = b2.most_similar(positive=[b4], topn=10)
b7 = [word for word, _ in b5]
b8 = [word for word, _ in b6]
b9 = "\n".join(f"{b3} - {word}: {b2.similarity(b3, word):.4f}" for word in b7)
b10 = "\n".join(f"{b4} - {word}: {b2.similarity(b4, word):.4f}" for word in b8)
print("Top ten similar words:\n")
print(f"{b3}: {b7}")
print(f"{b4}: {b8}")
print("\nCosine similarities:\n")
print(b9)
print(b10)