import nltk
from nltk.corpus import stopwords as sw
from nltk.corpus import wordnet as wn
nltk.download('stopwords')
nltk.download('wordnet')
def fonk1(text):
    b1 = nltk.PorterStemmer()
    b2 = text.split()
    b3 = [word.lower() for word in b2 if word.lower() not in sw.b2('english')]
    b4 = [b1.stem(word) for word in b3]
    return b4
def fonk2(b10, b11):
    a1 = 0
    a2 = 0
    for word1 in b10:
        b5 = wn.synsets(word1)
        if not b5:
            continue
        b6 = b5[0]
        for word2 in b11:
            b7 = wn.synsets(word2)
            if not b7:
                continue
            b8 = b7[0]
            b9 = b6.path_similarity(b8)
            if b9 is not None:
                a1 += b9
                a2 += 1
    return a1 / a2 if a2 > 0 else 0
def fonk3(text1, text2):
    b10 = fonk1(text1)
    b11 = fonk1(text2)
    b9 = fonk2(b10, b11)
    print(f"Semantic b9 between '{text1}' and '{text2}': {b9:.4f}")
fonk3("I am loved by everyone", "Everyone loves me")