import re
import json
import pickle
import sys
def fonk1(root, b6, b2, b1):
    if b1 = = "unsuz yumusamasi":
        return len(b6) > 0 and b6[0] in ["a", "e", "ý", "i", "o", "ö", "u", "ü"] and fonk3(b6)[0]
    if b1 = = "unlu daralmasi":
        if (b2 = = "demek" or b2 == "yemek") and fonk3(b6)[0]:
            return True
        if b6.startswith("yor"):
            b3 = ""
            for letter in reversed(b2[:-3]):
                if letter in ["a", "e", "ý", "i", "o", "ö", "u", "ü"]:
                    b3 = letter
                    break
            if b3 in ["a", "e"] and fonk3(b6)[0]:
                return True
        return False
    if b1 = = "fiil" or b1 == "olumsuzluk eki":
        return fonk3(b6)[0] and not (
                (root.endswith("la") or root.endswith("le")) and b6.startswith("r"))
    if b1 = = "unlu dusmesi":
        a1 = 0
        for letter in b2:
            if letter in ["a", "e", "ý", "i", "o", "ö", "u", "ü"]:
                a1 += 1
                b3 = letter
        if fonk3(b6)[0] and a1 = = 2 and (b3 in ["ý", "i", "u", "ü"]) and (
                len(b6) > 0 and b6[0] in ["a", "e", "ý", "i", "o", "ö", "u", "ü"]):
            if b3 = = "ý":
                return b6[0] in ["a", "ý"]
            elif b3 = = "i":
                return b6[0] in ["e", "i"]
            elif b3 = = "u":
                return b6[0] in ["a", "u"]
            elif b3 = = "ü":
                return b6[0] in ["e", "ü"]
        return False
    return True
def fonk2(b20, b19):
    b4 = []
    if "'" in b20:
        b4.append([b20[:b20.index("'")] + "_1", "tirnaksiz", b20])
    b5 = []
    for i in range(len(b20)):
        b2 = b20[:len(b20) - i]
        b6 = b20[len(b20) - i:]
        a2 = 1
        while b2 + "_" + str(a2) in b19:
            if fonk1(b2, b6, b19[b2 + "_" + str(a2)][1], b19[b2 + "_" + str(a2)][0]):
                b7 = (b19[b2 + "_" + str(a2)])
                while b7[0] not in ["kok", "fiil", "olumsuzluk"]:
                    b7 = b19[b7[1]]
                b5.append([b7[1], b19[b2 + "_" + str(a2)][0], b2 + "_" + str(a2)])
            a2 = a2 + 1
    b8 = []
    for kel in b5:
        b9 = kel[0][:kel[0].index("_")]
        b10 = len(b9)
        if b9.endswith("mak") or b9.endswith("mek"):
            b10 -= 3
        b11 = True
        for index in range(len(b8)):
            b12 = b8[index]
            b13 = b12[0][:b12[0].index("_")]
            b14 = len(b13)
            if b13.endswith("mak") or b13.endswith("mek"):
                b14 -= 3
            if b10 > b14:
                b8.insert(index, kel)
                b11 = False
        if b11:
            b8.append(kel)
    b15 = b4 + b8
    if len(b15) == 0:
        b15.append([b20 + "_1", "çaresiz", b20 + "_1"])
    return b15
def fonk3(suff):
    b16 = ["", "a", "abil", "acað", "acak", "alým", "ama", "an", "ar", "arak", "asý", "asýnýz", "ayým", "da", "dan", "de", "den", "dý", "dýðý", "dýk", "dýkça", "dýr", "di", "diði", "dik", "dikçe", "dir", "du", "duð", "duk", "dukça", "dur", "dü", "düð", "dük", "dükça", "dür", "e", "ebil", "eceði", "ecek", "elim", "eme", "en", "er", "erek", "esin", "esiniz", "eyim", "ý", "ýl", "im", "imiz", "in", "ince", "iniz", "ip", "ir", "iyor", "iz", "i", "il", "im", "imiz", "in", "ince", "iniz", "ip", "ir", "iyor", "iz", "k", "ken", "la", "lar", "larý", "larýn", "le", "ler", "leri", "lerin", "m", "ma", "madan", "mak", "maksýzýn", "makta", "maktansa", "malý", "maz", "me", "meden", "mek", "meksizin", "mekte", "mektense", "meli", "mez", "mý", "mýþ", "mýz", "mi", "miþ", "miz", "mu", "muþ", "mü", "muz", "müþ", "müz", "n", "nýn", "nýz", "nin", "niz", "nun", "nuz", "nün", "nüz", "r", "sa", "se", "sý", "sýn", "sýnýz", "sýnlar", "si", "sin", "siniz", "sinler", "su", "sun", "sunlar", "sunuz", "sü", "sün", "sünler", "sünüz", "ta", "tan", "te", "ten", "tý", "týðý", "týk", "týkça", "týr", "ti", "tiði", "tik", "tikçe", "tir", "tu", "tuð", "tuk", "tukça", "tur", "tü", "tüð", "tük", "tükça", "tür", "u", "ul", "um", "umuz", "un", "unca", "unuz", "up", "ur", "uyor", "uz", "ü", "ül", "ün", "üm", "ümüz", "ünce", "ünüz", "üp", "ür", "üyor", "üz", "ya", "yabil", "yacað", "yacak", "yalým", "yama", "yan", "yarak", "yasýn", "yasýnýz", "yayým", "ydý", "ydi", "ydu", "ydü", "ye", "yebil", "yeceði", "yecek", "yelim", "yeme", "yen", "yerek", "yesin", "yesiniz", "yeyim", "ý", "ým", "ýn", "ýnca", "ýnýz", "ýp", "ýz", "i", "il", "im", "imiz", "in", "ince", "iniz", "ip", "ir", "iyor", "iz", "k", "ken", "la", "le", "mýþ", "miþ", "muþ", "müþ", "or", "sa", "se", "sý", "sýn", "sýnýz", "sýnlar", "si", "sin", "siniz", "sinler", "su", "sun", "sunlar", "sunuz", "sü", "sün", "sünler", "sünüz", "ta", "tan", "te", "ten", "tý", "týð", "týk", "týkça", "týr", "ti", "tið", "tik", "tikçe", "tir", "tu", "tuð", "tuk", "tukça", "tur", "tü", "tüð", "tük", "tükça", "tür", "u", "ul", "um", "umuz", "un", "unca", "unuz", "up", "ur", "uyor", "uz", "ü", "ül", "ün", "üm", "ümüz", "ünce", "ünüz", "üp", "ür", "üyor", "üz", "ya", "yabil", "yacað", "yacak", "yalým", "yama", "yan", "yarak", "yasýn", "yasýnýz", "yayým", "ydý", "ydi", "ydu", "ydü", "ye", "yebil", "yeceði", "yecek", "yelim", "yeme", "yen", "yerek", "yesin", "yesiniz", "yeyim", "ý", "ým", "ýn", "ýnca", "ýnýz", "ýp", "ýz", "i", "il", "im", "imiz", "in", "ince", "iniz", "ip", "ir", "iyor", "iz", "k", "ken", "la", "le", "mýþ", "miþ", "muþ", "müþ", "or", "sa", "se", "sý", "sýn", "sýnýz", "sýnlar", "si", "sin", "siniz", "sinler", "su", "sun", "sunlar", "sunuz", "sü", "sün", "sünler", "sünüz", "ta", "tan", "te", "ten", "tý", "týð", "týk", "týkça", "týr", "ti", "tið", "tik", "tikçe", "tir", "tu", "tuð", "tuk", "tukça", "tur", "tü", "tüð", "tük", "tükça", "tür", "u", "ul", "um", "umuz", "un", "unca", "unuz", "up", "ur", "uyor", "uz", "ü", "ül", "ün", "üm", "ümüz", "ünce", "ünüz", "üp", "ür", "üyor", "üz", "ya", "yabil", "yacað", "yacak", "yalým", "yama", "yan", "yarak", "yasýn", "yasýnýz", "yayým", "ydý", "ydi", "ydu", "ydü", "ye", "yebil", "yeceði", "yecek", "yelim", "yeme", "yen", "yerek", "yesin", "yesiniz", "yeyim", "ý", "ým", "ýn", "ýnca", "ýnýz", "ýp", "ýz", "i", "il", "im", "imiz", "in", "ince", "iniz", "ip", "ir", "iyor", "iz", "k", "ken", "la", "le", "mýþ", "miþ", "muþ", "müþ", "or", "sa", "se", "sý", "sýn", "sýnýz", "sýnlar", "si", "sin", "siniz", "sinler", "su", "sun", "sunlar", "sunuz", "sü", "sün", "sünler", "sünüz", "ta", "tan", "te", "ten", "tý", "týð", "týk", "týkça", "týr", "ti", "tið", "tik", "tikçe", "tir", "tu", "tuð", "tuk", "tukça", "tur", "tü", "tüð", "tük", "tükça", "tür", "u", "ul", "um", "umuz", "un", "unca", "unuz", "up", "ur", "uyor", "uz", "ü", "ül", "ün", "üm", "ümüz", "ünce", "ünüz", "üp", "ür", "üyor", "üz", "ya", "yabil", "yacað", "yacak", "yalým", "yama", "yan", "yarak", "yasýn", "yasýnýz", "yayým", "ydý", "ydi", "ydu", "ydü", "ye", "yebil", "yeceði", "yecek", "yelim", "yeme", "yen", "yerek", "yesin", "yesiniz", "yeyim", "ý", "ým", "ýn", "ýnca", "ýnýz", "ýp", "ýz", "i", "il", "im", "imiz", "in", "ince", "iniz", "ip", "ir", "iyor", "iz", "k", "ken", "la", "le", "mýþ", "miþ", "muþ", "müþ", "or", "sa", "se", "sý", "sýn", "sýnýz", "sýnlar", "si", "sin", "siniz", "sinler", "su", "sun", "sunlar", "sunuz", "sü", "sün", "sünler", "sünüz", "ta", "tan", "te", "ten", "tý", "týð", "týk", "týkça", "týr", "ti", "tið", "tik", "tikçe", "tir", "tu", "tuð", "tuk", "tukça", "tur", "tü", "tüð", "tük", "tükça", "tür", "u", "ul", "um", "umuz", "un", "unca", "unuz", "up", "ur", "uyor", "uz", "ü", "ül", "ün", "üm", "ümüz", "ünce", "ünüz", "üp", "ür", "üyor", "üz", "ya", "yabil", "yacað", "yacak", "yalým", "yama", "yan", "yarak", "yasýn", "yasýnýz", "yayým", "ydý", "ydi", "ydu", "ydü", "ye", "yebil", "yeceði", "yecek", "yelim", "yeme", "yen", "yerek", "yesin", "yesiniz", "yeyim"]
    b17 = []
    if suff in b16:
        b17.append(suff)
    for ind in range(1, len(suff)):
        if suff[:ind] in b16:
            cont, b18 = fonk3(suff[ind:])
            if cont:
                b18 = [suff[:ind] + "+" + l for l in b18]
                b17 = b17 + b18
    return len(b17) > 0, b17
try:
    with open('revisedDict.pkl', 'rb') as f:
        b19 = pickle.load(f)
except IOError:
    print("Please run trainLexicon.py to generate revisedDict.pkl file")
if len(sys.argv) < 2:
    print("Please provide a b20 as a system argument")
    sys.exit(0)
b20 = sys.argv[1]
print("Possible lemmas for", b20, "in ranked order:")
b21 = fonk2(b20.lower(), b19)
for finding in b21:
    print(finding[0])