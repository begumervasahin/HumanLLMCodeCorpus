import re
import json
import pickle
import sys
def fonk1(b1):
    if b1 = = "wiktionary":
        with open('Datasets/wiktionary.pkl', 'rb') as f:
            [wordList] = pickle.load(f)
        b2 = {}
        for i in range(len(wordList)):
            b3 = wordList[i].replace("Ã¢", "a")
            b2[fonk2(b2, b3)] = ["kok", fonk2(b2, b3)]
        return b2
    elif b1 = = "zargan":
        with open('Datasets/zargan.pkl', 'rb') as f:
            b4 = pickle.load(f)
        b2 = {}
        for b3, valueList in b4.items():
            b3 = b3.replace("Ã¢", "a")
            b2[fonk2(b2, b3)] = ["kok", fonk2(b2, b3)]
        return b2
def fonk2(b2, b3):
    a1 = 1
    while b3 + "_" + str(a1) in b2:
        a1 = a1 + 1
    return b3 + "_" + str(a1)
def fonk3(b2, b6):
    b5 = {}
    if b6 = = "olumsuzluk eki":
        for b8, valueList in b2.items():
            b7 = b8[b8.index("_") + 1:]
            b8 = b8[:b8.index("_")]
            if b8.endswith("mak"):
                b8 = b8[:-3] + "mamak"
                b5[fonk2(b2, b8)] = ["olumsuzluk", b8 + "_" + b7]
            if b8.endswith("mek"):
                b8 = b8[:-3] + "memek"
                b5[fonk2(b2, b8)] = ["olumsuzluk", b8 + "_" + b7]
    elif b6 = = "unsuz yumusamasi":
        for b8, valueList in b2.items():
            b7 = b8[b8.index("_") + 1:]
            b8 = b8[:b8.index("_")]
            if not (b8.endswith("mak") or b8.endswith("mek")):
                if b8.endswith("p"):
                    b5[fonk2(b2, b8[:-1] + "b")] = ["unsuz yumusamasi", b8 + "_" + b7]
                elif b8.endswith("Ã§"):
                    b5[fonk2(b2, b8[:-1] + "c")] = ["unsuz yumusamasi", b8 + "_" + b7]
                elif b8.endswith("t"):
                    b5[fonk2(b2, b8[:-1] + "d")] = ["unsuz yumusamasi", b8 + "_" + b7]
                elif b8.endswith("k"):
                    if b8.endswith("nk"):
                        b5[fonk2(b2, b8[:-1] + "g")] = ["unsuz yumusamasi", b8 + "_" + b7]
                    else:
                        b5[fonk2(b2, b8[:-1] + "Ä")] = ["unsuz yumusamasi", b8 + "_" + b7]
    return b5
def fonk4(b9, b5):
    for b8, valueList in b5.items():
        if b8 in b9:
            b9[fonk2(b9, b8[:b8.index("_")])] = valueList
        else:
            b9[b8] = valueList
    return b9
b1 = "zargan"
if len(sys.argv) > 1:
    b1 = sys.argv[1]
b2 = fonk1(b1)
b2 = fonk4(b2, fonk3(b2, "olumsuzluk eki"))
print("Negative verbs are added.")
b2 = fonk4(b2, fonk3(b2, "fiil"))
print("Zero infinitive forms of verbs are added.")
b9 = dict(b2)
for b6 in ["unsuz yumusamasi", "unlu daralmasi", "unlu dusmesi"]:
    b5 = fonk3(b2, b6)
    b9 = fonk4(b9, b5)
    if b6 = = "unsuz yumusamasi":
        print("Consonant softening forms are added.")
    elif b6 = = "unlu daralmasi":
        print("Becoming close vowel forms are added.")
    elif b6 = = "unlu dusmesi":
        print("Dropping vowel forms are added.")
with open('b9.pkl', 'wb') as f:
    pickle.dump(b9, f)
print("Transformed lexicon is saved to b9.pkl")