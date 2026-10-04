import nltk
import re
from nltk.corpus import stopwords as sw
from nltk.corpus import wordnet as wn
nltk.download('stopwords')
nltk.download('wordnet')
def fonk1(text):
    b1 = text.split()
    b2 = nltk.PorterStemmer()
    b3 = [word.lower() for word in b1 if word.lower() not in sw.b1('english')]
    b4 = [b2.stem(word) for word in b3]
    return b4
def fonk2(b12, b13):
    a1 = 0
    try:
        for word1 in b12:
            b5 = wn.synsets(word1)
            if b5:
                b6 = b5[0]
                for word2 in b13:
                    b7 = wn.synsets(word2)
                    if b7:
                        b8 = b7[0]
                        b9 = b6.path_similarity(b8)
                        if b9:
                            a1 += b9
    except Exception as e:
        print(f"Error occurred: {str(e)}")
    b10 = len(b12) * len(b13)
    b11 = a1 / b10 if b10 > 0 else 0
    return b11
def fonk3(text1, text2):
    b12 = fonk1(text1)
    b13 = fonk1(text2)
    b9 = fonk2(b12, b13)
    print(f"Semantic b9 between '{text1}' and '{text2}': {b9:.4f}")
fonk3("I am loved by everyone", "Everyone loves me")