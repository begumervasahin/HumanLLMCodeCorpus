import io
import string
import re
import nltk
from nltk.tag import tnt
from nltk.corpus import indian
b1 = open("tech_text_final.txt", "r")
b2 = open("output.txt", "w")
b3 = open("lemma.txt", "w+")
b4 = open("tags.txt","w")
b5 = {}
def fonk1():
    b6 = indian.tagged_sents('hindi.pos')
    b7 = tnt.TnT()
    b7.train(b6)
    b8 = b1.read()
    b9 = b8.split("à¥¤")
    for b10 in b9:
        b10 = re.sub(r'(\b12+)',r' ',b10)
        b10 = b10.replace(',',' ')
        b10 = b10.replace('-',' ')
        b10 = b10.replace(':',' ')
        b10 = b10.replace('?',' ')
        b10 = b10.replace('(',' ')
        b10 = b10.replace(')',' ')
        b10 = b10.replace('.',' ')
        b10 = b10.split()
        for word in b10:
            if word!=" ":
                b11 = (b7.tag(nltk.word_tokenize(str(word))))
                b2.write(word.rstrip())
                b4.write(word.rstrip())
                b4.write(" : ")
                b4.write(b11[0][1])
                b2.write("\n")
                b4.write("\n")
    b4.close()
    b2.close()
    return
def fonk2():
    b12 = open("tags.txt","r")
    b13 = b12.read()
    b13 = b13.split("\n")
    b13[-1] = b13[-1].strip('\n')
    for b14 in b13:
        if b14 = ='':
            continue
        b10 = b14.split(":")
        if b10[1].strip().startswith("NN") or b10[1].strip().startswith("PR") or b10[1].strip().startswith("VAUX") :
            b5[b10[0].strip()] = [b10[0].strip()]
        else:
            fonk3(b10[0].strip())
def fonk3(word):
    b15 = {
    1: ["à¥","à¥","à¥","à¥","à¥","à¤¿","à¤¾"],
    2: ["à¤à¤°","à¤¾à¤","à¤¿à¤","à¤¾à¤","à¤¾à¤","à¤¨à¥","à¤¨à¥","à¤¨à¤¾","à¤¤à¥","à¥à¤","à¤¤à¥","à¤¤à¤¾","à¤¾à¤","à¤¾à¤","à¥à¤","à¥à¤"],
    3: ["à¤¾à¤à¤°","à¤¾à¤à¤","à¤¾à¤à¤","à¤¾à¤¯à¤¾","à¥à¤à¥","à¥à¤à¤¾","à¥à¤à¥","à¥à¤à¥","à¤¾à¤¨à¥","à¤¾à¤¨à¤¾","à¤¾à¤¤à¥","à¤¾à¤¤à¥","à¤¾à¤¤à¤¾","à¤¤à¥à¤","à¤¾à¤à¤","à¤¾à¤à¤","à¥à¤à¤","à¥à¤à¤","à¥à¤à¤"],
    4: ["à¤¾à¤à¤à¥","à¤¾à¤à¤à¤¾","à¤¾à¤à¤à¥","à¤¾à¤à¤à¥","à¤à¤à¤à¥","à¥à¤à¤à¥","à¤à¤à¤à¥","à¥à¤à¤à¥","à¥à¤à¤à¥","à¥à¤à¤à¤¾","à¤¾à¤¤à¥à¤","à¤¨à¤¾à¤à¤","à¤¨à¤¾à¤à¤","à¤¤à¤¾à¤à¤","à¤¤à¤¾à¤à¤","à¤¿à¤¯à¤¾à¤","à¤¿à¤¯à¥à¤","à¤¿à¤¯à¤¾à¤"],
    5: ["à¤¾à¤à¤à¤à¥","à¤¾à¤à¤à¤à¥","à¤¾à¤à¤à¤à¥","à¤¾à¤à¤à¤à¤¾","à¤¾à¤à¤¯à¤¾à¤","à¤¾à¤à¤¯à¥à¤","à¤¾à¤à¤¯à¤¾à¤"],
        }
    b16 = b15[4][17]
    b17 = b15[4][16]
    b18 = b15[1][1]
    b19 = b15[1][6]
    b20 = b15[1][4]
    b21 = b15[5][4]
    b22 = b15[5][5]
    b23 = b15[5][6]
    if word.endswith(b16):
        b5[word] = [word[:word.rindex(b16)] + b15[1][4]]
    elif word.endswith(b17):
        b5[word] = [word[:word.rindex(b17)] + b15[1][4]]
    elif word.endswith(b18):
        b5[word] = [word[:word.rindex(b18)] + b15[1][6]]
    elif word.endswith(b19):
        b5[word] = [word[:word.rindex(b19)] + b15[1][6]]
    elif word.endswith(b20):
        b5[word] = [word[:word.rindex(b20)] + b15[1][4]]
    elif word.endswith(b21):
        b5[word] = [word[:word.rindex(b21)] + b15[3][2]]
    elif word.endswith(b22):
        b5[word] = [word[:word.rindex(b22)] + b15[3][2]]
    elif word.endswith(b23):
        b5[word] = [word[:word.rindex(b23)] + b15[3][2]]
    else:
        if b5.get(word,None) == None:
            b5[word] = []
        for key in b15.keys():
            for value in b15[key]:
                if word.endswith(value):
                    b24 = word.rindex(value)
                    b5[word].append(word[:b24])
def fonk4():
    for k,v in b5.items():
        if not v:
            b3.write(k + ": "+ k)
        else:
            b3.write(k + ": ")
            for element in set(v):
                b3.write(element+" ")
        b3.write("\n")
def fonk5():
    fonk1()
    fonk2()
    fonk4()
if b25 = ="__main__":
    fonk5()