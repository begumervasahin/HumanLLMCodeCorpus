import pickle
import sys
def fonk1(b1):
    if b1 = = "wiktionary":
        with open('Datasets/wiktionary.pkl', 'rb') as file:
            [word_list] = pickle.load(file)
        b2 = {fonk2({}, word): ["kok", fonk2({}, word)] for word in word_list}
        return b2
    elif b1 = = "zargan":
        with open('Datasets/zargan.pkl', 'rb') as file:
            b3 = pickle.load(file)
        b2 = {fonk2({}, word): ["kok", fonk2({}, word)] for word in b3.keys()}
        return b2
def fonk2(b2, word):
    a1 = 1
    while f"{word}_{a1}" in b2:
        a1 += 1
    return f"{word}_{a1}"
def fonk3(b2, b5):
    b4 = {}
    if b5 = = "negative_suffix":
        for word, value_list in b2.items():
            b6 = word.b6("_") + 1
            b7 = word[:b6 - 1] if word.endswith("mak") or word.endswith("mek") else word[:-3]
            if b7.endswith("p"):
                b4[fonk2(b2, b7 + "b")] = ["unsuz yumusamasi", f"{b7}_{b6}"]
            elif b7.endswith("ç"):
                b4[fonk2(b2, b7 + "c")] = ["unsuz yumusamasi", f"{b7}_{b6}"]
            elif b7.endswith("t"):
                b4[fonk2(b2, b7 + "d")] = ["unsuz yumusamasi", f"{b7}_{b6}"]
            elif b7.endswith("k"):
                if b7.endswith("nk"):
                    b4[fonk2(b2, b7 + "g")] = ["unsuz yumusamasi", f"{b7}_{b6}"]
                else:
                    b4[fonk2(b2, b7 + "ð")] = ["unsuz yumusamasi", f"{b7}_{b6}"]
    return b4
def fonk4(b8, b4):
    for word, value_list in b4.items():
        if word in b8:
            b8[fonk2(b8, word.split("_")[0])] = value_list
        else:
            b8[word] = value_list
    return b8
def fonk5():
    b1 = "zargan"
    if len(sys.argv) > 1:
        b1 = sys.argv[1]
    b2 = fonk1(b1)
    b2 = fonk4(b2, fonk3(b2, "negative_suffix"))
    print("Negative verbs are added.")
    b2 = fonk4(b2, fonk3(b2, "fiil"))
    print("Zero infinitive forms of verbs are added.")
    b8 = dict(b2)
    for b5 in ["consonant_softening", "vowel_becoming_close", "vowel_dropping"]:
        b4 = fonk3(b2, b5)
        b8 = fonk4(b8, b4)
        if b5 = = "consonant_softening":
            print("Consonant softening forms are added.")
        elif b5 = = "vowel_becoming_close":
            print("Becoming close vowel forms are added.")
        elif b5 = = "vowel_dropping":
            print("Dropping vowel forms are added.")
    with open('revisedDict.pkl', 'wb') as file:
        pickle.dump(b8, file)
    print("Transformed lexicon is saved to revisedDict.pkl")
if b9 = = "__main__":
    fonk5()