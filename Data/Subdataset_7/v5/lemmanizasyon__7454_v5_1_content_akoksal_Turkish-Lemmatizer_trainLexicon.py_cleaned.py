import pickle
import sys
def fonk1(b15):
    b1 = f'Datasets/{b15}.pkl'
    with open(b1, 'rb') as file:
        b2 = pickle.load(file)
    b3 = {}
    for i, word_entry in enumerate(b2):
        b4 = word_entry.replace("Ã¢", "a")
        b5 = fonk2(b3, b4)
        b3[b5] = ["kok", b5]
    return b3
def fonk2(b3, b4):
    a1 = 1
    while f"{b4}_{a1}" in b3:
        a1 += 1
    return f"{b4}_{a1}"
def fonk3(b3, b11):
    b6 = {}
    def fonk4(b10, suffix, category):
        b7 = b10[:-len(suffix)] + suffix
        b8 = fonk2(b3, b7)
        b6[b8] = [category, f"{b7}_{b9}"]
    for b4, value_list in b3.items():
        b9 = b4[b4.index("_") + 1:]
        b10 = b4[:b4.index("_")]
        if b11 = = "olumsuzluk eki" and b10.endswith(("mak", "mek")):
            fonk4(b10, "mamak" if b10.endswith("mak") else "memek", "olumsuzluk")
        elif b11 = = "unsuz yumusamasi" and not b10.endswith(("mak", "mek")):
            b12 = {"p": "b", "Ã§": "c", "t": "d", "k": "g" if b10.endswith("nk") else "Ä"}
            for end, replacement in b12.items():
                if b10.endswith(end):
                    fonk4(b10, replacement, "unsuz yumusamasi")
        elif b11 = = "unlu daralmasi":
            b13 = {"demek": "di", "yemek": "yi", "amak": "Ä±", "emek": "i"}
            if b10 in b13:
                fonk4(b10, b13[b10], "unlu daralmasi")
        elif b11 = = "unlu dusmesi":
            b14 = {'akis': 'aks', 'akÄ±l': 'akl', 'alÄ±n': 'aln', ...}
            if b10 in b14:
                fonk4(b10, b14[b10], "unlu dusmesi")
        elif b11 = = "fiil" and b10.endswith(("mak", "mek")):
            fonk4(b10, "", "fiil")
    return b6
def fonk5(b16, b6):
    for b4, value_list in b6.items():
        if b4 in b16:
            b16[fonk2(b16, b4[:b4.index("_")])] = value_list
        else:
            b16[b4] = value_list
    return b16
def fonk6():
    b15 = "zargan"
    if len(sys.argv) > 1:
        b15 = sys.argv[1]
    b3 = fonk1(b15)
    b3 = fonk5(b3, fonk3(b3, "olumsuzluk eki"))
    print("Negative verbs are added.")
    b3 = fonk5(b3, fonk3(b3, "fiil"))
    print("Zero infinitive forms of verbs are added.")
    b16 = dict(b3)
    for b11 in ["unsuz yumusamasi", "unlu daralmasi", "unlu dusmesi"]:
        b6 = fonk3(b3, b11)
        b16 = fonk5(b16, b6)
        if b11 = = "unsuz yumusamasi":
            print("Consonant softening forms are added.")
        elif b11 = = "unlu daralmasi":
            print("Becoming close vowel forms are added.")
        elif b11 = = "unlu dusmesi":
            print("Dropping vowel forms are added.")
    with open('revisedDict.pkl', 'wb') as file:
        pickle.dump(b16, file)
    print("Transformed lexicon is saved to revisedDict.pkl")
if b17 = = "__main__":
    fonk6()