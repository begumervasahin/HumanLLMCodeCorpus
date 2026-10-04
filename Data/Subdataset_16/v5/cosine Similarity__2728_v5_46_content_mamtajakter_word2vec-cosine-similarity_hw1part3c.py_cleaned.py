import gensim
from nltk.corpus import brown
b1 = gensim.models.Word2Vec(brown.sents())
b2 = "rebellion"
b3 = "slave"
b4 = b1.most_similar(positive=[b2], topn=10)
b5 = b1.most_similar(positive=[b3], topn=10)
b6 = [word for word, _ in b4]
b7 = [word for word, _ in b5]
b8 = "\n".join(f"{b2} - {word}: {b1.similarity(b2, word):.4f}" for word in b6)
b9 = "\n".join(f"{b3} - {word}: {b1.similarity(b3, word):.4f}" for word in b7)
print(f"Top ten similar words for '{b2}':\n")
print(", ".join(b6))
print(f"\nTop ten similar words for '{b3}':\n")
print(", ".join(b7))
print(f"\nCosine similarities for '{b2}':\n")
print(b8)
print(f"\nCosine similarities for '{b3}':\n")
print(b9)