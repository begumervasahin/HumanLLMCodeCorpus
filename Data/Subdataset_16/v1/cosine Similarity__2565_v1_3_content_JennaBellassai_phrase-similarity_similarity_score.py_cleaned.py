from nltk.tokenize import word_tokenize
import gensim
def fonk1(b7):
    b1 = gensim.models.Word2Vec.load(b7, mmap='r')
    return b1
def fonk2(seq1, seq2, b1, b2 = 100, head=10):
    b3 = word_tokenize(seq1.strip().lower())[-b2:]
    b4 = word_tokenize(seq2.strip().lower())[:head]
    return fonk3(b3, b4, b1)
def fonk3(wordlist1, wordlist2, b1):
    b5 = []
    for b6 in wordlist1:
        a1 = 0
        for word2 in wordlist2:
            if b6 = = word2:
                a2 = 1
                a1 = a2
            elif b6 in b1.vocab and word2 in b1.vocab:
                a2 = b1.similarity(b6, word2)
                if a2 > a1:
                    a1 = a2
        if a1 != 0:
            b5.append(a1)
    if sum(b5) == 0:
        return 0
    return float(sum(b5)) / len(b5)
b7 = 'vectors'
b8 = fonk1(b7)
b9 = "This is a sample sequence for scoring similarity."
b10 = "Sample sequence scoring similarity using Word2Vec b1."
b11 = fonk2(b9, b10, b8)
print(f"Similarity Score: {b11}")