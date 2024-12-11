from nltk.tokenize import word_tokenize
import gensim
def fonk1(model_path):
    b1 = gensim.models.Word2Vec.load(model_path, mmap='r')
    return b1
def fonk2(seq1, seq2, b1, b2 = 100, head=10):
    b3 = word_tokenize(seq1.strip().lower())[-b2:]
    b4 = word_tokenize(seq2.strip().lower())[:head]
    return fonk3(b3, b4, b1)
def fonk3(words1, words2, b1):
    b5 = []
    for b6 in words1:
        a1 = 0
        for word2 in words2:
            if b6 = = word2:
                a1 = 1
            elif b6 in b1.vocab and word2 in b1.vocab:
                b7 = b1.b7(b6, word2)
                a1 = max(a1, b7)
        if a1 != 0:
            b5.append(a1)
    if b5:
        return sum(b5) / len(b5)
    else:
        return 0