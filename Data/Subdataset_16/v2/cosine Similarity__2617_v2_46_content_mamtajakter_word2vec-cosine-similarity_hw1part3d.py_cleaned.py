import gensim
b1 = 'GoogleNews-vectors-negative300.bin.gz'
b2 = gensim.models.KeyedVectors.load_word2vec_format(b1, binary=True)
b3 = "rebellion"
b4 = "slave"
b5 = b2.most_similar(positive=[b3], topn=10)
b6 = b2.most_similar(positive=[b4], topn=10)
b7 = [word for word, _ in b5]
b8 = [word for word, _ in b6]
b9 = "\n".join(
    f"{b3} - {word}: {b2.similarity(b3, word):.4f}"
    for word in b7
)
b10 = "\n".join(
    f"{b4} - {word}: {b2.similarity(b4, word):.4f}"
    for word in b8
)
print(f"Top ten similar words for '{b3}':\n")
print(", ".join(b7))
print(f"\nTop ten similar words for '{b4}':\n")
print(", ".join(b8))
print(f"\nCosine similarities for '{b3}':\n")
print(b9)
print(f"\nCosine similarities for '{b4}':\n")
print(b10)