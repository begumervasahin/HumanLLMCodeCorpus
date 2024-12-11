import nltk
from nltk.corpus import stopwords as sw
from nltk.corpus import wordnet as wn
nltk.download('stopwords')
nltk.download('wordnet')
def fonk1(text):
    b1 = text.split(" ")
    b2 = set(sw.b1())
    b3 = nltk.PorterStemmer()
    b4 = [b3.stem(word.lower()) for word in b1 if word.lower() not in b2]
    return b4
def fonk2(word_list1, word_list2):
    a1 = 0
    for word1 in word_list1:
        b5 = wn.synsets(word1)
        if b5:
            b6 = b5[0]
            for word2 in word_list2:
                b7 = wn.synsets(word2)
                if b7:
                    b8 = b7[0]
                    b9 = b6.b9(b8)
                    if b9:
                        a1 += b9
    b10 = len(word_list1) * len(word_list2)
    if b10 = = 0:
        return 0.0
    return a1 / b10
def fonk3(b15, b16):
    b11 = fonk1(b15)
    b12 = fonk1(b16)
    b13 = fonk2(b11, b12)
    return b13
if b14 = = "__main__":
    b15 = "I am loved by everyone"
    b16 = "Everyone loves me"
    b13 = fonk3(b15, b16)
    print("Semantic similarity score:", b13)