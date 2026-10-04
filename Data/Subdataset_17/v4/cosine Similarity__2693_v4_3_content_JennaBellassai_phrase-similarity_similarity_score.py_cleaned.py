from nltk.tokenize import word_tokenize
import gensim
def load_word2vec_model(model_path):
    return gensim.models.Word2Vec.load(model_path, mmap='r')
def prepare_inputs_for_scoring(seq1, seq2, model, tail=100, head=10):
    seq1_words = word_tokenize(seq1.strip().lower())[-tail:]
    seq2_words = word_tokenize(seq2.strip().lower())[:head]
    return calculate_similarity_score(seq1_words, seq2_words, model)
def calculate_similarity_score(wordlist1, wordlist2, model):
    max_similarities = []
    for word1 in wordlist1:
        cur_max_similarity = 0
        for word2 in wordlist2:
            if word1 == word2:
                similarity = 1
                cur_max_similarity = similarity
            elif word1 in model.vocab and word2 in model.vocab:
                similarity = model.similarity(word1, word2)
                if similarity > cur_max_similarity:
                    cur_max_similarity = similarity
        if cur_max_similarity != 0:
            max_similarities.append(cur_max_similarity)
    if not max_similarities:
        return 0.0
    return sum(max_similarities) / len(max_similarities)
model_path = 'vectors'
word2vec_model = load_word2vec_model(model_path)
sequence1 = "This is a sample sequence for scoring similarity."
sequence2 = "Sample sequence scoring similarity using Word2Vec model."
similarity_score = prepare_inputs_for_scoring(sequence1, sequence2, word2vec_model)
print(f"Similarity Score: {similarity_score}")