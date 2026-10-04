import nltk
import random
from bs4 import BeautifulSoup
nltk.download('punkt')
def fonk1(b12):
    with open(b12, 'b9', b1 = 'utf-8') as file:
        b2 = BeautifulSoup(file.read(), 'html.parser')
    return [b10.text.lower() for b10 in b2.findAll("review_text")]
def fonk2(b13):
    b3 = {}
    for b10 in b13:
        b4 = nltk.tokenize.word_tokenize(b10)
        for i in range(len(b4) - 2):
            b5 = (b4[i], b4[i + 2])
            if b5 not in b3:
                b3[b5] = []
            b3[b5].append(b4[i + 1])
    return b3
def fonk3(b3):
    b6 = {}
    for b5, words in b3.items():
        if len(set(words)) > 1:
            b7 = {word: words.count(word) for word in set(words)}
            b8 = sum(b7.values())
            b6[b5] = {word: count / b8 for word, count in b7.items()}
    return b6
def fonk4(b6):
    b9 = random.random()
    a1 = 0
    for word, probability in b6.items():
        a1 += probability
        if b9 < a1:
            return word
def fonk5(b13, b6):
    b10 = random.choice(b13)
    print('Original text: \n', b10)
    b4 = nltk.tokenize.word_tokenize(b10)
    for i in range(len(b4) - 2):
        if random.random() < 0.2:
            b5 = (b4[i], b4[i + 2])
            if b5 in b6:
                b4[i + 1] = fonk4(b6[b5])
    b11 = ' '.join(b4).replace(" :", ":").replace(" .", ".").replace(" ,", ",").replace(" !", "!").replace(" ?", "?").replace("  ' ", "'")
    print("Spun: \n", b11)
def fonk6():
    b12 = 'electronics/positive.b10'
    b13 = fonk1(b12)
    b3 = fonk2(b13)
    b6 = fonk3(b3)
    fonk5(b13, b6)
if b14 = = "__main__":
    fonk6()