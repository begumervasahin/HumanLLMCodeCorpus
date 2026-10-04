from nltk.tokenize import word_tokenize
import gensim
def load_word2vec_model(model_path):
    model = gensim.models.Word2Vec.load(model_path, mmap='r')
    return model
def score_similarity(seq1, seq2, model, tail=100, head=10):
    seq1_word_list = word_tokenize(seq1.strip().lower())[-tail:]
    seq2_word_list = word_tokenize(seq2.strip().lower())[:head]
    return calculate_similarity_score(seq1_word_list, seq2_word_list, model)
def calculate_similarity_score(wordlist1, wordlist2, model):
    maxes = []
    for word in wordlist1:
        cur_max = 0
        for word2 in wordlist2:
            if word == word2:
                sim = 1
                cur_max = sim
            elif word in model.vocab and word2 in model.vocab:
                sim = model.similarity(word, word2)
                if sim > cur_max:
                    cur_max = sim
        if cur_max != 0:
            maxes.append(cur_max)
    if sum(maxes) == 0:
        return 0
    return float(sum(maxes)) / len(maxes)
model_path = 'vectors'
word2vec_model = load_word2vec_model(model_path)
sequence1 = "This is a sample sequence for scoring similarity."
sequence2 = "Sample sequence scoring similarity using Word2Vec model."
similarity_score = score_similarity(sequence1, sequence2, word2vec_model)
print(f"Similarity Score: {similarity_score}")