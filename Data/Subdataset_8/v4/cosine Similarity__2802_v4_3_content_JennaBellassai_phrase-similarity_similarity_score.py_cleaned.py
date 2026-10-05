from nltk.tokenize import word_tokenize
import gensim
def load_word2vec_model(model_path):
    model = gensim.models.Word2Vec.load(model_path, mmap='r')
    return model
def calculate_similarity(seq1, seq2, model, tail=100, head=10):
    seq1_words = word_tokenize(seq1.strip().lower())[-tail:]
    seq2_words = word_tokenize(seq2.strip().lower())[:head]
    return calculate_average_max_similarity(seq1_words, seq2_words, model)
def calculate_average_max_similarity(words1, words2, model):
    max_similarities = []
    for word1 in words1:
        max_similarity = 0
        for word2 in words2:
            if word1 == word2:
                max_similarity = 1
            elif word1 in model.vocab and word2 in model.vocab:
                similarity = model.similarity(word1, word2)
                max_similarity = max(max_similarity, similarity)
        if max_similarity != 0:
            max_similarities.append(max_similarity)
    if max_similarities:
        return sum(max_similarities) / len(max_similarities)
    else:
        return 0