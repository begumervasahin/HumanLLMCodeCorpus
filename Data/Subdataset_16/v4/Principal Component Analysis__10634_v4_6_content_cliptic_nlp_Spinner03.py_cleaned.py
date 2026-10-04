import nltk
import random
from bs4 import BeautifulSoup
with open('electronics/positive.b9', 'r') as file:
    b1 = BeautifulSoup(file.read(), 'html.parser')
b1 = b1.findAll("b3")
b2 = {}
for b9 in b1:
    b3 = b9.text.lower()
    b4 = nltk.tokenize.word_tokenize(b3)
    for i in range(len(b4) - 3):
        b5 = (b4[i], b4[i + 2])
        if b5 not in b2:
            b2[b5] = []
        b2[b5].append(b4[i + 1])
b6 = {}
for b5, words in b2.items():
    if len(set(words)) > 1:
        b7 = {}
        a1 = 0
        for word in words:
            if word not in b7:
                b7[word] = 0
            b7[word] += 1
            a1 += 1
        b6[b5] = {word: count / a1 for word, count in b7.items()}
def fonk1(prob_dist):
    b8 = random.random()
    a2 = 0
    for word, prob in prob_dist.items():
        a2 += prob
        if b8 < a2:
            return word
def fonk2():
    b9 = random.choice(b1).text.lower()
    print('Original text:\n', b9)
    b4 = nltk.tokenize.word_tokenize(b9)
    for i in range(len(b4) - 3):
        if random.random() < 0.85:
            b5 = (b4[i], b4[i + 2])
            if b5 in b6:
                b10 = fonk1(b6[b5])
                if nltk.pos_tag([b10])[0][1] == nltk.pos_tag([b4[i + 1]])[0][1]:
                    b4[i + 1] = b10
    b11 = ' '.join(b4)
    b11 = b11.replace(" :", ":").replace(" .", ".").replace(" ,", ",").replace(" !", "!").replace(" ?", "?").replace("  ' ", "'")
    print("Spun text:\n", b11)
fonk2()