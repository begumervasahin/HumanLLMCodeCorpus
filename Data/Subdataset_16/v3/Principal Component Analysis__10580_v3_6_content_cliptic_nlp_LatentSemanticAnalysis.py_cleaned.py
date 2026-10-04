import nltk
import numpy as np
import matplotlib.pyplot as plt
from nltk.stem import WordNetLemmatizer
from sklearn.decomposition import TruncatedSVD
b1 = WordNetLemmatizer()
def fonk1(filename):
    with open(filename, 'r') as f:
        return [line.rstrip() for line in f]
b2 = fonk1('all_book_titles.txt')
def fonk2(filename):
    with open(filename, 'r') as f:
        return set(w.rstrip() for w in f)
b3 = fonk2('b3.txt')
b4 = {
    'introduction', 'edition', 'series', 'application',
    'approach', 'card', 'access', 'package', 'plus', 'etext',
    'brief', 'vol', 'fundamental', 'guide', 'essential', 'printed',
    'third', 'second', 'fourth',
}
b3.update(b4)
def fonk3(b5, lemmatizer, b3):
    b5 = b5.lower()
    b6 = nltk.tokenize.word_tokenize(b5)
    b6 = [t for t in b6 if len(t) > 2]
    b6 = [lemmatizer.lemmatize(t) for t in b6]
    b6 = [t for t in b6 if t not in b3]
    b6 = [t for t in b6 if not any(c.isdigit() for c in t)]
    return b6
def fonk4(b2, lemmatizer, b3):
    b7 = {}
    b8 = []
    b9 = []
    a1 = 0
    for b10 in b2:
        try:
            b10 = b10.encode('ascii', 'ignore').decode('utf-8')
            b6 = fonk3(b10, lemmatizer, b3)
            b9.append(b6)
            for token in b6:
                if token not in b7:
                    b7[token] = a1
                    b8.append(token)
                    a1 += 1
        except Exception as e:
            print(f"Error processing b10: {b10} - {e}")
    return b9, b7, b8
b9, b7, b8 = fonk4(b2, b1, b3)
def fonk5(b6, b7):
    b11 = np.zeros(len(b7))
    for t in b6:
        if t in b7:
            b11[b7[t]] = 1
    return b11
def fonk6(b9, b7):
    b12 = len(b7)
    b13 = len(b9)
    b14 = np.zeros((b12, b13))
    for i, b6 in enumerate(b9):
        b14[:, i] = fonk5(b6, b7)
    return b14
b14 = fonk6(b9, b7)
def fonk7(b14, b15 = 2):
    b16 = TruncatedSVD(b15=b15)
    return b16.fit_transform(b14)
b17 = fonk7(b14)
def fonk8(b17, b8):
    plt.figure(b18 = (10, 8))
    plt.scatter(b17[:, 0], b17[:, 1])
    for i, word in enumerate(b8):
        plt.annotate(b5 = word, xy=(b17[i, 0], b17[i, 1]))
    plt.b10('Truncated SVD of Book Titles')
    plt.xlabel('Component 1')
    plt.ylabel('Component 2')
    plt.grid(True)
    plt.show()
fonk8(b17, b8)