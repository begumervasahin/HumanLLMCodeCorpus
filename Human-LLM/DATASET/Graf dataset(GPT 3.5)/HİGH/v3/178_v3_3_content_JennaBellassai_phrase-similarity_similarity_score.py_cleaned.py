from nltk.tokenize import word_tokenize
import gensim
def fonk1(b8):
    return gensim.models.Word2Vec.load(b8, b1 = 'r')
def fonk2(seq1, seq2, model, b2 = 100, head_length=10):
    b3 = word_tokenize(seq1.strip().lower())[-b2:]
    b4 = word_tokenize(seq2.strip().lower())[:head_length]
    return fonk3(b3, b4, model)
def fonk3(word_list1, word_list2, model):
    b5 = []
    for b6 in word_list1:
        a1 = 0
        for word2 in word_list2:
            if b6 = = word2:
                a1 = 1
            elif b6 in model.wv.vocab and word2 in model.wv.vocab:
                b7 = model.wv.b7(b6, word2)
                a1 = max(a1, b7)
        if a1 != 0:
            b5.append(a1)
    if b5:
        return sum(b5) / len(b5)
    else:
        return 0
b8 = 'vectors'
b9 = fonk1(b8)
b10 = "This is an example sequence."
b11 = "Another example sentence."
b12 = fonk2(b10, b11, b9)
print("Similarity Score:", b12)