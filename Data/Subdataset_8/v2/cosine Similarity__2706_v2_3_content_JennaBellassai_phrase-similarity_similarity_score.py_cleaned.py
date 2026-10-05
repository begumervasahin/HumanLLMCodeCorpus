from nltk.tokenize import word_tokenize
import gensim
def load_model(model_path):
    model = gensim.models.Word2Vec.load(model_path, mmap='r')
    return model
def calculate_similarity_score(seq1, seq2, model, tail=100, head=10):
    seq1_word_list = word_tokenize(seq1.strip().lower())[-tail:]
    seq2_word_list = word_tokenize(seq2.strip().lower())[:head]
    return calculate_average_max_similarity(seq1_word_list, seq2_word_list, model)
def calculate_average_max_similarity(word_list1, word_list2, model):
    max_similarities = []
    for word1 in word_list1:
        max_similarity = 0
        for word2 in word_list2:
            if word1 == word2:
                max_similarity = 1
            elif word1 in model.wv.vocab and word2 in model.wv.vocab:
                similarity = model.wv.similarity(word1, word2)
                if similarity > max_similarity:
                    max_similarity = similarity
        if max_similarity != 0:
            max_similarities.append(max_similarity)
    if not max_similarities:
        return 0
    return sum(max_similarities) / len(max_similarities)
model_path = 'vectors'
loaded_model = load_model(model_path)
seq1 = "This is an example sequence."
seq2 = "Another example sentence."
similarity_score = calculate_similarity_score(seq1, seq2, loaded_model)
print("Similarity Score:", similarity_score)