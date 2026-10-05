import nltk
from nltk.corpus import stopwords as sw
from nltk.corpus import wordnet as wn
nltk.download('stopwords')
nltk.download('wordnet')
def fonk1(text):
    b1 = text.split()
    b2 = [word.lower() for word in b1 if word.lower() not in sw.b1()]
    b3 = nltk.PorterStemmer()
    b4 = [b3.stem(word) for word in b2]
    return b4
def fonk2(b14, b15):
    b5 = fonk1(b14)
    b6 = fonk1(b15)
    a1 = 0
    try:
        for word1 in b5:
            b7 = wn.synsets(word1)
            if b7:
                b8 = b7[0]
                for word2 in b6:
                    b9 = wn.synsets(word2)
                    if b9:
                        b10 = b9[0]
                        b11 = b8.b11(b10)
                        if b11:
                            a1 += b11
        b12 = len(b5) * len(b6)
        if b12 = = 0:
            return 0.0
        return a1 / b12
    except Exception as e:
        print(str(e))
        return 0.0
if b13 = = "__main__":
    b14 = "I am loved by everyone"
    b15 = "Everyone loves me"
    b16 = fonk2(b14, b15)
    print("Semantic a1 score:", b16)