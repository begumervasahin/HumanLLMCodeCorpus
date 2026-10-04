import gensim
def fonk1(b5):
    return gensim.models.KeyedVectors.load_word2vec_format(b5, b1 = True)
def fonk2(b6, word, b2 = 10):
    b3 = b6.most_similar(positive=[word], b2=b2)
    return [word for word, _ in b3]
def fonk3(b6, word, b3):
    b4 = [
        f"{word} - {similar_word}: {b6.similarity(word, similar_word):.4f}"
        for similar_word in b3
    ]
    return "\n".join(b4)
def fonk4():
    b5 = 'GoogleNews-vectors-negative300.bin.gz'
    b6 = fonk1(b5)
    b7 = "rebellion"
    b8 = "slave"
    b9 = fonk2(b6, b7)
    b10 = fonk2(b6, b8)
    b11 = fonk3(b6, b7, b9)
    b12 = fonk3(b6, b8, b10)
    print(f"Top ten similar words for '{b7}':\n")
    print(", ".join(b9))
    print(f"\nTop ten similar words for '{b8}':\n")
    print(", ".join(b10))
    print(f"\nCosine b4 for '{b7}':\n")
    print(b11)
    print(f"\nCosine b4 for '{b8}':\n")
    print(b12)
if b13 = = "__main__":
    fonk4()