from nltk.tokenize import word_tokenize
import gensim
def load_model(model_path):
    model = gensim.models.Word2Vec.load(model_path, mmap='r')
    return model
def score(seq1, seq2, model, tail=100, head=10):
    seq1_word_list = word_tokenize(seq1.strip().lower())[-tail:]
    seq2_word_list = word_tokenize(seq2.strip().lower())[:head]
    return sim_score(seq1_word_list, seq2_word_list, model)
def sim_score(wordlist1, wordlist2, model):
    maxes = []
    for word in wordlist1:
        cur_max = 0
        for word2 in wordlist2:
            if word == word2:
                sim = 1
                cur_max = sim
            elif word in model.wv.vocab and word2 in model.wv.vocab:
                sim = model.wv.similarity(word, word2)
                if sim > cur_max:
                    cur_max = sim
        if cur_max != 0:
            maxes.append(cur_max)
    if sum(maxes) == 0:
        return 0
    return float(sum(maxes)) / len(maxes)
model_path = 'vectors'
loaded_model = load_model(model_path)
seq1 = "This is an example sequence."
seq2 = "Another example sentence."
similarity_score = score(seq1, seq2, loaded_model)
print("Similarity Score:", similarity_score)