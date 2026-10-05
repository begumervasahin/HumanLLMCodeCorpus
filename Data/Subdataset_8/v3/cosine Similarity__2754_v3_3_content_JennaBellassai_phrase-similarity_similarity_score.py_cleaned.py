from nltk.tokenize import word_tokenize
import gensim
def load_word2vec_model(model_path):
    return gensim.models.Word2Vec.load(model_path, mmap='r')
def calculate_similarity_score(seq1, seq2, model, tail_length=100, head_length=10):
    seq1_tail = word_tokenize(seq1.strip().lower())[-tail_length:]
    seq2_head = word_tokenize(seq2.strip().lower())[:head_length]
    return calculate_average_max_similarity(seq1_tail, seq2_head, model)
def calculate_average_max_similarity(word_list1, word_list2, model):
    max_similarities = []
    for word1 in word_list1:
        max_similarity = 0
        for word2 in word_list2:
            if word1 == word2:
                max_similarity = 1
            elif word1 in model.wv.vocab and word2 in model.wv.vocab:
                similarity = model.wv.similarity(word1, word2)
                max_similarity = max(max_similarity, similarity)
        if max_similarity != 0:
            max_similarities.append(max_similarity)
    if max_similarities:
        return sum(max_similarities) / len(max_similarities)
    else:
        return 0
model_path = 'vectors'
word2vec_model = load_word2vec_model(model_path)
sequence1 = "This is an example sequence."
sequence2 = "Another example sentence."
similarity_score = calculate_similarity_score(sequence1, sequence2, word2vec_model)
print("Similarity Score:", similarity_score)