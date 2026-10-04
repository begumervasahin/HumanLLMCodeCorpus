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
def fonk2(text1, text2):
    b5 = fonk1(text1)
    b6 = fonk1(text2)
    a1 = 0
    try:
        for word1 in b5:
            b7 = wn.synsets(word1)
            if b7:
                b7 = b7[0]
                for word2 in b6:
                    b8 = wn.synsets(word2)
                    if b8:
                        b8 = b8[0]
                        b9 = b7.path_similarity(b8)
                        if b9 is not None:
                            a1 += b9
    except Exception as e:
        print(f"Error: {str(e)}")
    if len(b5) > 0 and len(b6) > 0:
        b10 = a1 / (len(b5) * len(b6))
    else:
        b10 = 0
    print(f"Semantic b9: {b10}")
    return b10
fonk2("I am loved by everyone", "Everyone loves me")