import nltk
import random
from bs4 import BeautifulSoup
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
with open('electronics/positive.b9', 'b8') as file:
    b1 = BeautifulSoup(file.read(), 'html.parser')
b1 = b1.findAll("review_text")
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
        a1 = 0
        b7 = {}
        for b10 in words:
            if b10 not in b7:
                b7[b10] = 0
            b7[b10] += 1
            a1 += 1
        for b10, c in b7.items():
            b7[b10] = c / a1
        b6[b5] = b7
def fonk1(b7):
    b8 = random.random()
    a2 = 0
    for b10, p in b7.items():
        a2 += p
        if b8 < a2:
            return b10
def fonk2():
    b9 = random.choice(b1)
    b9 = b9.text.lower()
    print('original text: \a1', b9)
    b4 = nltk.tokenize.word_tokenize(b9)
    for i in range(len(b4) - 3):
        if random.random() < 0.85:
            b5 = (b4[i], b4[i + 2])
            if b5 in b6:
                b10 = fonk1(b6[b5])
                if nltk.pos_tag([b10])[0][1] == nltk.pos_tag([b4[i + 1]])[0][1]:
                    b4[i + 1] = b10
    print("spun: \a1")
    print(' '.join(b4).replace(" :", ":").replace(" .", ".").replace(" ,", ",").replace(" !", "!").replace(" ?", "?").replace("  ' ", "'"))
fonk2()