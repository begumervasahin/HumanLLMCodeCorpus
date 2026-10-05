import string
import re
import nltk
from nltk.b18 import tnt
from nltk.corpus import indian
b1 = "tech_text_final.txt"
b2 = "output.txt"
b3 = "lemma.txt"
b4 = "tags.txt"
with open(b1, "r", b5 = "utf-8") as input_file:
    b6 = input_file.read()
b7 = open(b2, "w", b5="utf-8")
b8 = open(b3, "w+", b5="utf-8")
b9 = open(b4, "w", b5="utf-8")
b10 = {}
def fonk1():
    b11 = indian.tagged_sents('hindi.pos')
    b12 = tnt.TnT()
    b12.train(b11)
    return b12
def fonk2(b12):
    b13 = b6.split("à¥¤")
    for b14 in b13:
        b14 = re.sub(r'(\d+)', r' ', b14)
        b14 = b14.translate(str.maketrans('', '', string.punctuation))
        b15 = b14.split()
        for word in b15:
            if word:
                b16 = b12.b18(nltk.word_tokenize(word))
                b7.write(word.rstrip() + "\n")
                b9.write(word.rstrip() + " : " + b16[0][1] + "\n")
def fonk3():
    with open(b4, "r", b5 = "utf-8") as tags:
        b17 = tags.read().split("\n")
    for b16 in b17:
        if not b16:
            continue
        word, b18 = b16.split(":")
        if b18.strip().startswith("NN") or b18.strip().startswith("PR") or b18.strip().startswith("VAUX"):
            b10[word.strip()] = [word.strip()]
        else:
            fonk4(word.strip())
def fonk4(word):
    b19 = {
        1: ["à¥", "à¥", "à¥", "à¥", "à¥", "à¤¿", "à¤¾"],
        2: ["à¤à¤°", "à¤¾à¤", "à¤¿à¤", "à¤¾à¤", "à¤¾à¤", "à¤¨à¥", "à¤¨à¥", "à¤¨à¤¾", "à¤¤à¥", "à¥à¤", "à¤¤à¥", "à¤¤à¤¾", "à¤¾à¤", "à¤¾à¤", "à¥à¤", "à¥à¤"],
        3: ["à¤¾à¤à¤°", "à¤¾à¤à¤", "à¤¾à¤à¤", "à¤¾à¤¯à¤¾", "à¥à¤à¥", "à¥à¤à¤¾", "à¥à¤à¥", "à¥à¤à¥", "à¤¾à¤¨à¥", "à¤¾à¤¨à¤¾", "à¤¾à¤¤à¥", "à¤¾à¤¤à¥", "à¤¾à¤¤à¤¾", "à¤¤à¥à¤", "à¤¾à¤à¤", "à¤¾à¤à¤", "à¥à¤à¤", "à¥à¤à¤", "à¥à¤à¤"],
        4: ["à¤¾à¤à¤à¥", "à¤¾à¤à¤à¤¾", "à¤¾à¤à¤à¥", "à¤¾à¤à¤à¥", "à¤à¤à¤à¥", "à¥à¤à¤à¥", "à¤à¤à¤à¥", "à¥à¤à¤à¥", "à¥à¤à¤à¥", "à¥à¤à¤à¤¾", "à¤¾à¤¤à¥à¤", "à¤¨à¤¾à¤à¤", "à¤¨à¤¾à¤à¤", "à¤¤à¤¾à¤à¤", "à¤¤à¤¾à¤à¤", "à¤¿à¤¯à¤¾à¤", "à¤¿à¤¯à¥à¤", "à¤¿à¤¯à¤¾à¤"],
        5: ["à¤¾à¤à¤à¤à¥", "à¤¾à¤à¤à¤à¥", "à¤¾à¤à¤à¤à¥", "à¤¾à¤à¤à¤à¤¾", "à¤¾à¤à¤¯à¤¾à¤", "à¤¾à¤à¤¯à¥à¤", "à¤¾à¤à¤¯à¤¾à¤"],
    }
    b20 = b19[4][17]
    b21 = b19[4][16]
    b22 = b19[1][1]
    b23 = b19[1][6]
    b24 = b19[1][4]
    b25 = b19[5][4]
    b26 = b19[5][5]
    b27 = b19[5][6]
    if word.endswith(b20):
        b10[word] = [word[:word.rindex(b20)] + b19[1][4]]
    elif word.endswith(b21):
        b10[word] = [word[:word.rindex(b21)] + b19[1][4]]
    elif word.endswith(b22):
        b10[word] = [word[:word.rindex(b22)] + b19[1][6]]
    elif word.endswith(b23):
        b10[word] = [word[:word.rindex(b23)] + b19[1][6]]
    elif word.endswith(b24):
        b10[word] = [word[:word.rindex(b24)] + b19[1][4]]
    elif word.endswith(b25):
        b10[word] = [word[:word.rindex(b25)] + b19[3][2]]
    elif word.endswith(b26):
        b10[word] = [word[:word.rindex(b26)] + b19[3][2]]
    elif word.endswith(b27):
        b10[word] = [word[:word.rindex(b27)] + b19[3][2]]
    else:
        if word not in b10:
            b10[word] = []
        for key in b19.keys():
            for value in b19[key]:
                if word.endswith(value):
                    b28 = word.rindex(value)
                    b10[word].append(word[:b28])
def fonk5():
    for word, lemmas in b10.items():
        if not lemmas:
            b8.write(word + ": " + word)
        else:
            b8.write(word + ": " + " ".join(set(lemmas)))
        b8.write("\n")
def fonk6():
    b12 = fonk1()
    fonk2(b12)
    fonk3()
    fonk5()
if b29 = = "__main__":
    fonk6()