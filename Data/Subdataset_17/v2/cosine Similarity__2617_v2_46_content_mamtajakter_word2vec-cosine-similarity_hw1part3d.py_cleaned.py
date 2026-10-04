import gensim
model_path = 'GoogleNews-vectors-negative300.bin.gz'
model = gensim.models.KeyedVectors.load_word2vec_format(model_path, binary=True)
word1 = "rebellion"
word2 = "slave"
similar_words1 = model.most_similar(positive=[word1], topn=10)
similar_words2 = model.most_similar(positive=[word2], topn=10)
similar_words_list1 = [word for word, _ in similar_words1]
similar_words_list2 = [word for word, _ in similar_words2]
cosine_similarities1 = "\n".join(
    f"{word1} - {word}: {model.similarity(word1, word):.4f}"
    for word in similar_words_list1
)
cosine_similarities2 = "\n".join(
    f"{word2} - {word}: {model.similarity(word2, word):.4f}"
    for word in similar_words_list2
)
print(f"Top ten similar words for '{word1}':\n")
print(", ".join(similar_words_list1))
print(f"\nTop ten similar words for '{word2}':\n")
print(", ".join(similar_words_list2))
print(f"\nCosine similarities for '{word1}':\n")
print(cosine_similarities1)
print(f"\nCosine similarities for '{word2}':\n")
print(cosine_similarities2)