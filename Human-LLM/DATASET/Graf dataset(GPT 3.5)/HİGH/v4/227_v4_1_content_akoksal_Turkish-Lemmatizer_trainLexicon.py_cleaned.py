import re
import json
import pickle
import sys
def fonk1(b1):
    if b1 = = "wiktionary":
        with open('Datasets/wiktionary.pkl', 'rb') as f:
            [word_list] = pickle.load(f)
        b2 = {}
        for i in range(len(word_list)):
            b3 = word_list[i].replace("Ã¢", "a")
            b2[fonk2(b2, b3)] = ["kok", fonk2(b2, b3)]
        return b2
    elif b1 = = "zargan":
        with open('Datasets/zargan.pkl', 'rb') as f:
            b4 = pickle.load(f)
        b2 = {}
        for b3, value_list in b4.items():
            b3 = b3.replace("Ã¢", "a")
            b2[fonk2(b2, b3)] = ["kok", fonk2(b2, b3)]
        return b2
def fonk2(b2, b3):
    a1 = 1
    while f"{b3}_{a1}" in b2:
        a1 += 1
    return f"{b3}_{a1}"
def fonk3(b2, b6):
    b5 = {}
    if b6 = = "olumsuzluk eki":
        for b3, value_list in b2.items():
            b7 = b3[b3.index("_") + 1:]
            b8 = b3[:b3.index("_")]
            if b8.endswith("mak"):
                b8 = b8[:-3] + "mamak"
                b5[fonk2(b2, b8)] = ["olumsuzluk", f"{b8}_{b7}"]
            elif b8.endswith("mek"):
                b8 = b8[:-3] + "memek"
                b5[fonk2(b2, b8)] = ["olumsuzluk", f"{b8}_{b7}"]
    elif b6 = = "unsuz yumusamasi":
        for b3, value_list in b2.items():
            b7 = b3[b3.index("_") + 1:]
            b8 = b3[:b3.index("_")]
            if not (b8.endswith("mak") or b8.endswith("mek")):
                if b8.endswith("p"):
                    b5[fonk2(b2, b8[:-1] + "b")] = ["unsuz yumusamasi", f"{b8}_{b7}"]
                elif b8.endswith("Ã§"):
                    b5[fonk2(b2, b8[:-1] + "c")] = ["unsuz yumusamasi", f"{b8}_{b7}"]
                elif b8.endswith("t"):
                    b5[fonk2(b2, b8[:-1] + "d")] = ["unsuz yumusamasi", f"{b8}_{b7}"]
                elif b8.endswith("k"):
                    if b8.endswith("nk"):
                        b5[fonk2(b2, b8[:-1] + "g")] = ["unsuz yumusamasi", f"{b8}_{b7}"]
                    else:
                        b5[fonk2(b2, b8[:-1] + "Ä")] = ["unsuz yumusamasi", f"{b8}_{b7}"]
    elif b6 = = "unlu daralmasi":
        for b3, value_list in b2.items():
            b7 = b3[b3.index("_") + 1:]
            b8 = b3[:b3.index("_")]
            if b8 = = "demek":
                b5[fonk2(b2, "di")] = ["unlu daralmasi", f"{b8}_{b7}"]
            elif b8 = = "yemek":
                b5[fonk2(b2, "yi")] = ["unlu daralmasi", f"{b8}_{b7}"]
            elif b8.endswith("amak"):
                b5[fonk2(b2, b8[:-4] + "Ä±")] = ["unlu daralmasi", f"{b8}_{b7}"]
                b5[fonk2(b2, b8[:-4] + "u")] = ["unlu daralmasi", f"{b8}_{b7}"]
            elif b8.endswith("emek"):
                b5[fonk2(b2, b8[:-4] + "i")] = ["unlu daralmasi", f"{b8}_{b7}"]
                b5[fonk2(b2, b8[:-4] + "Ã¼")] = ["unlu daralmasi", f"{b8}_{b7}"]
    elif b6 = = "unlu dusmesi":
        for b3, value_list in b2.items():
            b7 = b3[b3.index("_") + 1:]
            b8 = b3[:b3.index("_")]
            b9 = {'akis': 'aks', 'akÄ±l': 'akl', 'alÄ±n': 'aln', ...}
            if b8 in b9:
                b5[fonk2(b2, b9[b8])] = ["unlu dusmesi", f"{b8}_{b7}"]
    elif b6 = = "fiil":
        for b3, value_list in b2.items():
            b7 = b3[b3.index("_") + 1:]
            b8 = b3[:b3.index("_")]
            if b8.endswith("mek") or b8.endswith("mak"):
                b5[fonk2(b2, b8[:-3])] = ["fiil", f"{b8}_{b7}"]
    return b5
def fonk4(b10, b5):
    for b3, value_list in b5.items():
        if b3 in b10:
            b10[fonk2(b10, b3[:b3.index("_")])] = value_list
        else:
            b10[b3] = value_list
    return b10
def fonk5():
    b1 = "zargan"
    if len(sys.argv) > 1:
        b1 = sys.argv[1]
    b2 = fonk1(b1)
    b2 = fonk4(b2, fonk3(b2, "olumsuzluk eki"))
    print("Negative verbs are added.")
    b2 = fonk4(b2, fonk3(b2, "fiil"))
    print("Zero infinitive forms of verbs are added.")
    b10 = dict(b2)
    for b6 in ["unsuz yumusamasi", "unlu daralmasi", "unlu dusmesi"]:
        b5 = fonk3(b2, b6)
        b10 = fonk4(b10, b5)
        if b6 = = "unsuz yumusamasi":
            print("Consonant softening forms are added.")
        elif b6 = = "unlu daralmasi":
            print("Becoming close vowel forms are added.")
        elif b6 = = "unlu dusmesi":
            print("Dropping vowel forms are added.")
    with open('revisedDict.pkl', 'wb') as f:
        pickle.dump(b10, f)
    print("Transformed lexicon is saved to revisedDict.pkl")
if b11 = = "__main__":
    fonk5()