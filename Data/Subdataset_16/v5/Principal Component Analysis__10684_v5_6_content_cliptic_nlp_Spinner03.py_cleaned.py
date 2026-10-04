import nltk
import random
from bs4 import BeautifulSoup
def fonk1(b13):
    with open(b13, 'r') as file:
        b1 = BeautifulSoup(file.read(), 'html.parser')
    return b1.findAll("b3")
def fonk2(reviews):
    b2 = {}
    for b12 in reviews:
        b3 = b12.text.lower()
        b4 = nltk.tokenize.word_tokenize(b3)
        for i in range(len(b4) - 3):
            b5 = (b4[i], b4[i + 2])
            if b5 not in b2:
                b2[b5] = []
            b2[b5].append(b4[i + 1])
    return b2
def fonk3(b2):
    b6 = {}
    for b5, words in b2.items():
        if len(set(words)) > 1:
            b7 = {word: words.count(word) for word in set(words)}
            b8 = sum(b7.values())
            b6[b5] = {word: count / b8 for word, count in b7.items()}
    return b6
def fonk4(prob_dist):
    b9 = random.random()
    a1 = 0
    for word, prob in prob_dist.items():
        a1 += prob
        if b9 < a1:
            return word
def fonk5(b12, b6):
    b3 = b12.text.lower()
    b4 = nltk.tokenize.word_tokenize(b3)
    for i in range(len(b4) - 3):
        if random.random() < 0.85:
            b5 = (b4[i], b4[i + 2])
            if b5 in b6:
                b10 = fonk4(b6[b5])
                if nltk.pos_tag([b10])[0][1] == nltk.pos_tag([b4[i + 1]])[0][1]:
                    b4[i + 1] = b10
    b11 = ' '.join(b4)
    return b11.replace(" :", ":").replace(" .", ".").replace(" ,", ",").replace(" !", "!").replace(" ?", "?").replace("  ' ", "'")
def fonk6(reviews, b6):
    b12 = random.choice(reviews)
    print('Original text:\n', b12.text.lower())
    b11 = fonk5(b12, b6)
    print("Spun text:\n", b11)
b13 = 'electronics/positive.b12'
b14 = fonk1(b13)
b2 = fonk2(b14)
b6 = fonk3(b2)
fonk6(b14, b6)