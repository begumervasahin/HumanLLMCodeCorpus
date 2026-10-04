import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
nltk.download('stopwords')
nltk.download('wordnet')
def fonk1(text):
    b1 = nltk.PorterStemmer()
    b2 = [
        b1.stem(word.lower())
        for word in text.split()
        if word.lower() not in stopwords.words('english')
    ]
    return b2
def fonk2(text1, text2):
    b3 = fonk1(text1)
    b4 = fonk1(text2)
    a1 = 0
    try:
        for word1 in b3:
            b5 = wn.synsets(word1)
            if b5:
                b6 = b5[0]
                for word2 in b4:
                    b7 = wn.synsets(word2)
                    if b7:
                        b8 = b7[0]
                        b9 = b6.path_similarity(b8)
                        if b9:
                            a1 += b9
    except Exception as e:
        print(f"Error occurred: {str(e)}")
    b10 = len(b3) * len(b4)
    b11 = a1 / b10 if b10 > 0 else 0
    print(f"Semantic b9: {b11:.4f}")
    return b11
fonk2("I am loved by everyone", "Everyone loves me")