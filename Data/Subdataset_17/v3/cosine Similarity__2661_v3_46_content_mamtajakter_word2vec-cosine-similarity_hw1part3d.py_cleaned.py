import gensim
def load_word2vec_model(model_path):
    return gensim.models.KeyedVectors.load_word2vec_format(model_path, binary=True)
def get_similar_words(model, word, topn=10):
    similar_words = model.most_similar(positive=[word], topn=topn)
    return [word for word, _ in similar_words]
def calculate_cosine_similarities(model, word, similar_words):
    similarities = [
        f"{word} - {similar_word}: {model.similarity(word, similar_word):.4f}"
        for similar_word in similar_words
    ]
    return "\n".join(similarities)
def main():
    model_path = 'GoogleNews-vectors-negative300.bin.gz'
    model = load_word2vec_model(model_path)
    word1 = "rebellion"
    word2 = "slave"
    similar_words1 = get_similar_words(model, word1)
    similar_words2 = get_similar_words(model, word2)
    cosine_similarities1 = calculate_cosine_similarities(model, word1, similar_words1)
    cosine_similarities2 = calculate_cosine_similarities(model, word2, similar_words2)
    print(f"Top ten similar words for '{word1}':\n")
    print(", ".join(similar_words1))
    print(f"\nTop ten similar words for '{word2}':\n")
    print(", ".join(similar_words2))
    print(f"\nCosine similarities for '{word1}':\n")
    print(cosine_similarities1)
    print(f"\nCosine similarities for '{word2}':\n")
    print(cosine_similarities2)
if __name__ == "__main__":
    main()