import io
import string
import re
import nltk
from nltk.tag import tnt
from nltk.corpus import indian
b1 = open("tech_text_final.txt", "r")
b2 = open("output.txt", "w")
b3 = open("lemma.txt", "w+")
b4 = open("tags.txt", "w")
b5 = {}
def fonk1():
    b6 = indian.tagged_sents('hindi.pos')
    b7 = tnt.TnT()
    b7.train(b6)
    b8 = b1.read()
    b9 = b8.split("à¥¤")
    for b10 in b9:
        b10 = re.sub(r'(\d+)', r' ', b10)
        b10 = b10.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
        b11 = b10.split()
        for word in b11:
            if word.strip() != "":
                b12 = b7.tag(nltk.word_tokenize(word))
                b2.write(word.rstrip() + "\n")
                b4.write(word.rstrip() + " : " + b12[0][1] + "\n")
    b4.close()
    b2.close()
def fonk2():
    b13 = open("tags.txt", "r")
    b14 = b13.read().split("\n")
    for b15 in b14:
        if b15 = = '':
            continue
        b16 = b15.split(":")
        if b16[1].strip().startswith("NN") or b16[1].strip().startswith("PR") or b16[1].strip().startswith("VAUX"):
            b5[b16[0].strip()] = [b16[0].strip()]
        else:
            fonk3(b16[0].strip())
def fonk3(word):
    b17 = {
        1: ["à¥", "à¥", "à¥", "à¥", "à¥", "à¤¿", "à¤¾"],
        2: ["à¤à¤°", "à¤¾à¤", "à¤¿à¤", "à¤¾à¤", "à¤¾à¤", "à¤¨à¥", "à¤¨à¥", "à¤¨à¤¾", "à¤¤à¥", "à¥à¤", "à¤¤à¥", "à¤¤à¤¾", "à¤¾à¤", "à¤¾à¤", "à¥à¤", "à¥à¤"],
        3: ["à¤¾à¤à¤°", "à¤¾à¤à¤", "à¤¾à¤à¤", "à¤¾à¤¯à¤¾", "à¥à¤à¥", "à¥à¤à¤¾", "à¥à¤à¥", "à¥à¤à¥", "à¤¾à¤¨à¥", "à¤¾à¤¨à¤¾", "à¤¾à¤¤à¥", "à¤¾à¤¤à¥", "à¤¾à¤¤à¤¾", "à¤¤à¥à¤", "à¤¾à¤à¤", "à¤¾à¤à¤", "à¥à¤à¤", "à¥à¤à¤", "à¥à¤à¤"],
        4: ["à¤¾à¤à¤à¥", "à¤¾à¤à¤à¤¾", "à¤¾à¤à¤à¥", "à¤¾à¤à¤à¥", "à¤à¤à¤à¥", "à¥à¤à¤à¥", "à¤à¤à¤à¥", "à¥à¤à¤à¥", "à¥à¤à¤à¥", "à¥à¤à¤à¤¾", "à¤¾à¤¤à¥à¤", "à¤¨à¤¾à¤à¤", "à¤¨à¤¾à¤à¤", "à¤¤à¤¾à¤à¤", "à¤¤à¤¾à¤à¤", "à¤¿à¤¯à¤¾à¤", "à¤¿à¤¯à¥à¤", "à¤¿à¤¯à¤¾à¤"],
        5: ["à¤¾à¤à¤à¤à¥", "à¤¾à¤à¤à¤à¥", "à¤¾à¤à¤à¤à¥", "à¤¾à¤à¤à¤à¤¾", "à¤¾à¤à¤¯à¤¾à¤", "à¤¾à¤à¤¯à¥à¤", "à¤¾à¤à¤¯à¤¾à¤"],
    }
    b18 = b17[4][17]
    b19 = b17[4][16]
    b20 = b17[1][1]
    b21 = b17[1][6]
    b22 = b17[1][4]
    b23 = b17[5][4]
    b24 = b17[5][5]
    b25 = b17[5][6]
    if word.endswith(b18):
        b5[word] = [word[:word.rindex(b18)] + b17[1][4]]
    elif word.endswith(b19):
        b5[word] = [word[:word.rindex(b19)] + b17[1][4]]
    elif word.endswith(b20):
        b5[word] = [word[:word.rindex(b20)] + b17[1][6]]
    elif word.endswith(b21):
        b5[word] = [word[:word.rindex(b21)] + b17[1][6]]
    elif word.endswith(b22):
        b5[word] = [word[:word.rindex(b22)] + b17[1][4]]
    elif word.endswith(b23):
        b5[word] = [word[:word.rindex(b23)] + b17[3][2]]
    elif word.endswith(b24):
        b5[word] = [word[:word.rindex(b24)] + b17[3][2]]
    elif word.endswith(b25):
        b5[word] = [word[:word.rindex(b25)] + b17[3][2]]
    else:
        if b5.get(word, None) == None:
            b5[word] = []
        for key in b17.keys():
            for value in b17[key]:
                if word.endswith(value):
                    b26 = word.rindex(value)
                    b5[word].append(word[:b26])
def fonk4():
    for k, v in b5.items():
        if not v:
            b3.write(k + ": " + k)
        else:
            b3.write(k + ": ")
            for element in set(v):
                b3.write(element + " ")
        b3.write("\n")
def fonk5():
    fonk1()
    fonk2()
    fonk4()
if b27 = = "__main__":
    fonk5()