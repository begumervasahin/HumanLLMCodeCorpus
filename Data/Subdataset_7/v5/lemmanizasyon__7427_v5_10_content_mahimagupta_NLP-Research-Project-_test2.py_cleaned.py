import re
import string
from nltk.tag import tnt
from nltk.corpus import indian
import nltk
b1 = open("tech_text_final.txt", "r")
b2 = open("output.txt", "w")
b3 = open("lemma.txt", "w+")
b4 = open("tags.txt", "w")
b5 = {}
def fonk1(b6):
    b6 = re.sub(r'(\d+)', r' ', b6)
    b6 = b6.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
    return b6
def fonk2():
    b7 = indian.tagged_sents('hindi.pos')
    b8 = tnt.TnT()
    b8.train(b7)
    b6 = b1.read()
    b9 = b6.split("à¥¤")
    for b10 in b9:
        b10 = fonk1(b10)
        b11 = nltk.word_tokenize(b10)
        for word in b11:
            if word.strip() != "":
                b12 = b8.tag([word])
                b2.write(word.rstrip() + "\n")
                b4.write(word.rstrip() + " : " + b12[0][1] + "\n")
    b4.close()
    b2.close()
def fonk3():
    with open("tags.txt", "r") as tag_data:
        b13 = tag_data.read().split("\n")
    for b14 in b13:
        if b14 = = '':
            continue
        b15 = b14.split(":")
        if b15[1].strip().startswith(("NN", "PR", "VAUX")):
            b5[b15[0].strip()] = [b15[0].strip()]
        else:
            fonk4(b15[0].strip())
def fonk4(word):
    b16 = {
        1: ["à¥", "à¥", "à¥", "à¥", "à¥", "à¤¿", "à¤¾"],
        2: ["à¤à¤°", "à¤¾à¤", "à¤¿à¤", "à¤¾à¤", "à¤¾à¤", "à¤¨à¥", "à¤¨à¥", "à¤¨à¤¾", "à¤¤à¥", "à¥à¤", "à¤¤à¥", "à¤¤à¤¾", "à¤¾à¤", "à¤¾à¤", "à¥à¤", "à¥à¤"],
        3: ["à¤¾à¤à¤°", "à¤¾à¤à¤", "à¤¾à¤à¤", "à¤¾à¤¯à¤¾", "à¥à¤à¥", "à¥à¤à¤¾", "à¥à¤à¥", "à¥à¤à¥", "à¤¾à¤¨à¥", "à¤¾à¤¨à¤¾", "à¤¾à¤¤à¥", "à¤¾à¤¤à¥", "à¤¾à¤¤à¤¾", "à¤¤à¥à¤", "à¤¾à¤à¤", "à¤¾à¤à¤", "à¥à¤à¤", "à¥à¤à¤", "à¥à¤à¤"],
        4: ["à¤¾à¤à¤à¥", "à¤¾à¤à¤à¤¾", "à¤¾à¤à¤à¥", "à¤¾à¤à¤à¥", "à¤à¤à¤à¥", "à¥à¤à¤à¥", "à¤à¤à¤à¥", "à¥à¤à¤à¥", "à¥à¤à¤à¥", "à¥à¤à¤à¤¾", "à¤¾à¤¤à¥à¤", "à¤¨à¤¾à¤à¤", "à¤¨à¤¾à¤à¤", "à¤¤à¤¾à¤à¤", "à¤¤à¤¾à¤à¤", "à¤¿à¤¯à¤¾à¤", "à¤¿à¤¯à¥à¤", "à¤¿à¤¯à¤¾à¤"],
        5: ["à¤¾à¤à¤à¤à¥", "à¤¾à¤à¤à¤à¥", "à¤¾à¤à¤à¤à¥", "à¤¾à¤à¤à¤à¤¾", "à¤¾à¤à¤¯à¤¾à¤", "à¤¾à¤à¤¯à¥à¤", "à¤¾à¤à¤¯à¤¾à¤"],
    }
    b17 = [b16[4][17], b16[4][16], b16[1][1], b16[1][6], b16[1][4], b16[5][4], b16[5][5], b16[5][6]]
    for b18 in b17:
        if word.endswith(b18):
            if b18 = = b16[4][17] or b18 == b16[4][16] or b18 == b16[1][4]:
                b19 = b16[1][4]
            elif b18 = = b16[1][1] or b18 == b16[1][6]:
                b19 = b16[1][6]
            elif b18 = = b16[5][4] or b18 == b16[5][5] or b18 == b16[5][6]:
                b19 = b16[3][2]
            b5[word] = [word[:word.rindex(b18)] + b19]
            return
    if word not in b5:
        b5[word] = []
def fonk5():
    with open("lemma.txt", "w+") as b3:
        for k, v in b5.items():
            if not v:
                b3.write(k + ": " + k)
            else:
                b3.write(k + ": ")
                for element in set(v):
                    b3.write(element + " ")
            b3.write("\n")
def fonk6():
    fonk2()
    fonk3()
    fonk5()
if b20 = = "__main__":
    fonk6()