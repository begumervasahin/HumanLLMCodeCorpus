import nltk
import re
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
nltk.download('stopwords')
nltk.download('wordnet')
def fonk1(text):
    b1 = text.split()
    b2 = nltk.PorterStemmer()
    b3 = [word.lower() for word in b1 if word.lower() not in stopwords.b1('english')]
    b4 = [b2.stem(word) for word in b3]
    return b4
def fonk2(text1, text2):
    b5 = fonk1(text1)
    b6 = fonk1(text2)
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
                        b11 = b8.path_similarity(b10)
                        if b11 is not None:
                            a1 += b11
    except Exception as e:
        print(f"Error occurred: {str(e)}")
    b12 = len(b5) * len(b6)
    if b12 > 0:
        b13 = a1 / b12
    else:
        b13 = 0
    print(f"Semantic b11: {b13}")
    return b13
fonk2("I am loved by everyone", "Everyone loves me")