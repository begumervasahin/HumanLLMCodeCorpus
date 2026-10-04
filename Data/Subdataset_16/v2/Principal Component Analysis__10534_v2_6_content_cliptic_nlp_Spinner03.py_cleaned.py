import nltk
import random
from bs4 import BeautifulSoup
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
def fonk1(file_path):
    with open(file_path, 'b8') as file:
        b1 = BeautifulSoup(file.read(), 'html.parser')
    return [review.text.lower() for review in b1.findAll("review_text")]
def fonk2(reviews):
    b2 = {}
    for review in reviews:
        b3 = nltk.word_tokenize(review)
        for i in range(len(b3) - 3):
            b4 = (b3[i], b3[i + 2])
            if b4 not in b2:
                b2[b4] = []
            b2[b4].append(b3[i + 1])
    return b2
def fonk3(b2):
    b5 = {}
    for b4, words in b2.items():
        if len(set(words)) > 1:
            b6 = len(words)
            b7 = {b9: words.count(b9) / b6 for b9 in set(words)}
            b5[b4] = b7
    return b5
def fonk4(d):
    b8 = random.random()
    a1 = 0
    for b9, p in d.items():
        a1 += p
        if b8 < a1:
            return b9
def fonk5(review, b5):
    b3 = nltk.word_tokenize(review)
    for i in range(len(b3) - 3):
        if random.random() < 0.85:
            b4 = (b3[i], b3[i + 2])
            if b4 in b5:
                b9 = fonk4(b5[b4])
                if nltk.pos_tag([b9])[0][1] == nltk.pos_tag([b3[i + 1]])[0][1]:
                    b3[i + 1] = b9
    return ' '.join(b3).replace(" :", ":").replace(" .", ".").replace(" ,", ",").replace(" !", "!").replace(" ?", "?").replace("  ' ", "'")
def fonk6():
    b10 = fonk1('electronics/positive.review')
    b2 = fonk2(b10)
    b5 = fonk3(b2)
    b11 = random.choice(b10)
    print('Original text:\n', b11)
    b12 = fonk5(b11, b5)
    print("\nSpun text:\n", b12)
fonk6()