from nltk.tokenize import word_tokenize
import gensim
def fonk1(b8):
    b1 = gensim.models.Word2Vec.load(b8, mmap='r')
    return b1
def fonk2(b10, b11, b1, b2 = 100, head=10):
    b3 = word_tokenize(b10.strip().lower())[-b2:]
    b4 = word_tokenize(b11.strip().lower())[:head]
    return fonk3(b3, b4, b1)
def fonk3(word_list1, word_list2, b1):
    b5 = []
    for b6 in word_list1:
        a1 = 0
        for word2 in word_list2:
            if b6 = = word2:
                a1 = 1
            elif b6 in b1.wv.vocab and word2 in b1.wv.vocab:
                b7 = b1.wv.b7(b6, word2)
                if b7 > a1:
                    a1 = b7
        if a1 != 0:
            b5.append(a1)
    if not b5:
        return 0
    return sum(b5) / len(b5)
b8 = 'vectors'
b9 = fonk1(b8)
b10 = "This is an example sequence."
b11 = "Another example sentence."
b12 = fonk2(b10, b11, b9)
print("Similarity Score:", b12)