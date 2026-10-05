import pickle
import sys
def fonk1(b2):
    b1 = {}
    def fonk2(file_path):
        with open(file_path, 'rb') as file:
            return pickle.load(file)
    if b2 = = "wiktionary":
        b3 = fonk2('Datasets/wiktionary.pkl')
        b1 = {fonk3({}, word): ["kok", fonk3({}, word)] for word in b3}
    elif b2 = = "zargan":
        b4 = fonk2('Datasets/zargan.pkl')
        b1 = {fonk3({}, word): ["kok", fonk3({}, word)] for word in b4.keys()}
    return b1
def fonk3(b1, word):
    a1 = 1
    while f"{word}_{a1}" in b1:
        a1 += 1
    return f"{word}_{a1}"
def fonk4(b1, b6):
    b5 = {}
    def fonk5(b8, suffix, new_suffix, event):
        b5[fonk3(b1, b8 + new_suffix)] = [event, f"{b8}_{suffix}"]
    if b6 = = "negative_suffix":
        for word, value_list in b1.items():
            b7 = word.b7("_") + 1
            b8 = word[:b7 - 1] if word.endswith("mak") or word.endswith("mek") else word[:-3]
            if b8.endswith(("p", "ç", "t")):
                fonk5(b8, b7, "b", "unsuz yumusamasi")
            elif b8.endswith("k"):
                fonk5(b8, b7, "g" if b8.endswith("nk") else "ð", "unsuz yumusamasi")
    return b5
def fonk6(b9, b5):
    for word, value_list in b5.items():
        b9[fonk3(b9, word.split("_")[0])] = value_list
    return b9
def fonk7():
    b2 = "zargan"
    if len(sys.argv) > 1:
        b2 = sys.argv[1]
    b1 = fonk1(b2)
    b1 = fonk6(b1, fonk4(b1, "negative_suffix"))
    print("Negative verbs are added.")
    b1 = fonk6(b1, fonk4(b1, "fiil"))
    print("Zero infinitive forms of verbs are added.")
    b9 = dict(b1)
    for b6 in ["consonant_softening", "vowel_becoming_close", "vowel_dropping"]:
        b5 = fonk4(b1, b6)
        b9 = fonk6(b9, b5)
        print(f"{b6.capitalize().replace('_', ' ')} forms are added.")
    with open('revisedDict.pkl', 'wb') as file:
        pickle.dump(b9, file)
    print("Transformed lexicon is saved to revisedDict.pkl")
if b10 = = "__main__":
    fonk7()