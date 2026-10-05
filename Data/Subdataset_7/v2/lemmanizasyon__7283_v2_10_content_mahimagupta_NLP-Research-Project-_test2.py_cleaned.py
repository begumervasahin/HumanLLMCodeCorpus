import string
import re
import nltk
from nltk.b15 import tnt
from nltk.corpus import indian
b1 = open("tech_text_final.txt", "r", b13="utf-8")
b2 = open("output.txt", "w", b13="utf-8")
b3 = open("lemma.txt", "w+", b13="utf-8")
b4 = open("tags.txt", "w", b13="utf-8")
b5 = {}
def fonk1():
    b6 = indian.tagged_sents('hindi.pos')
    b7 = tnt.TnT()
    b7.train(b6)
    return b7
def fonk2(b7):
    b8 = b1.read()
    b9 = b8.split("à¥¤")
    for b10 in b9:
        b10 = re.sub(r'(\d+)', r' ', b10)
        b10 = b10.translate(str.maketrans('', '', string.punctuation))
        b11 = b10.split()
        for word in b11:
            if word:
                b12 = b7.b15(nltk.word_tokenize(word))
                b2.write(word.rstrip() + "\n")
                b4.write(word.rstrip() + " : " + b12[0][1] + "\n")
def fonk3():
    with open("tags.txt", "r", b13 = "utf-8") as tags:
        b14 = tags.read().split("\n")
    for b12 in b14:
        if not b12:
            continue
        word, b15 = b12.split(":")
        if b15.strip().startswith("NN") or b15.strip().startswith("PR") or b15.strip().startswith("VAUX"):
            b5[word.strip()] = [word.strip()]
        else:
            fonk4(word.strip())
def fonk4(word):
    b16 = {
        1: ["à¥", "à¥", "à¥", "à¥", "à¥", "à¤¿", "à¤¾"],
        2: ["à¤à¤°", "à¤¾à¤", "à¤¿à¤", "à¤¾à¤", "à¤¾à¤", "à¤¨à¥", "à¤¨à¥", "à¤¨à¤¾", "à¤¤à¥", "à¥à¤", "à¤¤à¥", "à¤¤à¤¾", "à¤¾à¤", "à¤¾à¤", "à¥à¤", "à¥à¤"],
        3: ["à¤¾à¤à¤°", "à¤¾à¤à¤", "à¤¾à¤à¤", "à¤¾à¤¯à¤¾", "à¥à¤à¥", "à¥à¤à¤¾", "à¥à¤à¥", "à¥à¤à¥", "à¤¾à¤¨à¥", "à¤¾à¤¨à¤¾", "à¤¾à¤¤à¥", "à¤¾à¤¤à¥", "à¤¾à¤¤à¤¾", "à¤¤à¥à¤", "à¤¾à¤à¤", "à¤¾à¤à¤", "à¥à¤à¤", "à¥à¤à¤", "à¥à¤à¤"],
        4: ["à¤¾à¤à¤à¥", "à¤¾à¤à¤à¤¾", "à¤¾à¤à¤à¥", "à¤¾à¤à¤à¥", "à¤à¤à¤à¥", "à¥à¤à¤à¥", "à¤à¤à¤à¥", "à¥à¤à¤à¥", "à¥à¤à¤à¥", "à¥à¤à¤à¤¾", "à¤¾à¤¤à¥à¤", "à¤¨à¤¾à¤à¤", "à¤¨à¤¾à¤à¤", "à¤¤à¤¾à¤à¤", "à¤¤à¤¾à¤à¤", "à¤¿à¤¯à¤¾à¤", "à¤¿à¤¯à¥à¤", "à¤¿à¤¯à¤¾à¤"],
        5: ["à¤¾à¤à¤à¤à¥", "à¤¾à¤à¤à¤à¥", "à¤¾à¤à¤à¤à¥", "à¤¾à¤à¤à¤à¤¾", "à¤¾à¤à¤¯à¤¾à¤", "à¤¾à¤à¤¯à¥à¤", "à¤¾à¤à¤¯à¤¾à¤"],
    }
    b17 = b16[4][17]
    b18 = b16[4][16]
    b19 = b16[1][1]
    b20 = b16[1][6]
    b21 = b16[1][4]
    b22 = b16[5][4]
    b23 = b16[5][5]
    b24 = b16[5][6]
    if word.endswith(b17):
        b5[word] = [word[:word.rindex(b17)] + b16[1][4]]
    elif word.endswith(b18):
        b5[word] = [word[:word.rindex(b18)] + b16[1][4]]
    elif word.endswith(b19):
        b5[word] = [word[:word.rindex(b19)] + b16[1][6]]
    elif word.endswith(b20):
        b5[word] = [word[:word.rindex(b20)] + b16[1][6]]
    elif word.endswith(b21):
        b5[word] = [word[:word.rindex(b21)] + b16[1][4]]
    elif word.endswith(b22):
        b5[word] = [word[:word.rindex(b22)] + b16[3][2]]
    elif word.endswith(b23):
        b5[word] = [word[:word.rindex(b23)] + b16[3][2]]
    elif word.endswith(b24):
        b5[word] = [word[:word.rindex(b24)] + b16[3][2]]
    else:
        if word not in b5:
            b5[word] = []
        for key in b16.keys():
            for value in b16[key]:
                if word.endswith(value):
                    b25 = word.rindex(value)
                    b5[word].append(word[:b25])
def fonk5():
    for word, lemmas in b5.items():
        if not lemmas:
            b3.write(word + ": " + word)
        else:
            b3.write(word + ": " + " ".join(set(lemmas)))
        b3.write("\n")
def fonk6():
    b7 = fonk1()
    fonk2(b7)
    fonk3()
    fonk5()
if b26 = = "__main__":
    fonk6()