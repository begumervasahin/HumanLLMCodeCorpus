import re
import json
import pickle
import sys
def fonk1(b10):
    b1 = ["", "a", "abil", "acað", "acak", "alým", "ama", "an", "ar", "arak", "asý", "asýnýz", "ayým", "da", "dan", "de", "den", "dý", "dýðý", "dýk", "dýkça", "dýr", "di", "diði", "dik", "dikçe", "dir", "du", "duð", "duk", "dukça", "dur", "dü", "düð", "dük", "dükça", "dür", "e", "ebil", "eceði", "ecek", "elim", "eme", "en", "er", "erek", "esin", "esiniz", "eyim", "ý", "ýl", "im", "imiz", "in", "ince", "iniz", "ip", "ir", "iyor", "iz", "i", "il", "im", "imiz", "in", "ince", "iniz", "ip", "ir", "iyor", "iz", "k", "ken", "la", "lar", "larý", "larýn", "le", "ler", "leri", "lerin", "m", "ma", "madan", "mak", "maksýzýn", "makta", "maktansa", "malý", "maz", "me", "meden", "mek", "meksizin", "mekte", "mektense", "meli", "mez", "mý", "mýþ", "mýz", "mi", "miþ", "miz", "mu", "muþ", "mü", "muz", "müþ", "müz", "n", "nýn", "nýz", "nin", "niz", "nun", "nuz", "nün", "nüz", "r", "sa", "se", "sý", "sýn", "sýnýz", "sýnlar", "si", "sin", "siniz", "sinler", "su", "sun", "sunlar", "sunuz", "sü", "sün", "sünler", "sünüz", "ta", "tan", "te", "ten", "tý", "týðý", "týk", "týkça", "týr", "ti", "tiði", "tik", "tikçe", "tir", "tu", "tuð", "tuk", "tukça", "tur", "tü", "tüð", "tük", "tükça", "tür", "u", "ul", "um", "umuz", "un", "unca", "unuz", "up", "ur", "uyor", "uz", "ü", "ül", "ün", "üm", "ümüz", "ünce", "ünüz", "üp", "ür", "üyor", "üz", "ya", "yabil", "yacað", "yacak", "yalým", "yama", "yan", "yarak", "yasýn", "yasýnýz", "yayým", "ydý", "ydi", "ydu", "ydü", "ye", "yebil", "yeceði", "yecek", "yelim", "yeme", "yen", "yerek", "yesin", "yesiniz", "yeyim", "ý", "ým", "ýn", "ýnca", "ýnýz", "ýp", "ýz", "i", "il", "im", "imiz", "in", "ince", "iniz", "ip", "ir", "iyor", "iz", "k", "ken", "la", "le", "mýþ", "miþ", "muþ", "müþ", "or", "sa", "se", "sý", "sýn", "sýnýz", "sýnlar", "si", "sin", "siniz", "sinler", "su", "sun", "sunlar", "sunuz", "sü", "sün", "sünler", "sünüz", "ta", "tan", "te", "ten", "tý", "týð", "týk", "týkça", "týr", "ti", "tið", "tik", "tikçe", "tir", "tu", "tuð", "tuk", "tukça", "tur", "tü", "tüð", "tük", "tükça", "tür", "u", "ul", "um", "umuz", "un", "unca", "unuz", "up", "ur", "uyor", "uz", "ü", "ül", "ün", "üm", "ümüz", "ünce", "ünüz", "üp", "ür", "üyor", "üz", "ya", "yabil", "yacað", "yacak", "yalým", "yama", "yan", "yarak", "yasýn", "yasýnýz", "yayým", "ydý", "ydi", "ydu", "ydü", "ye", "yebil", "yeceði", "yecek", "yelim", "yeme", "yen", "yerek", "yesin", "yesiniz", "yeyim", "ý", "ým", "ýn", "ýnca", "ýnýz", "ýp", "ýz", "i", "il", "im", "imiz", "in", "ince", "iniz", "ip", "ir", "iyor", "iz", "k", "ken", "la", "le", "mýþ", "miþ", "muþ", "müþ", "or", "sa", "se", "sý", "sýn", "sýnýz", "sýnlar", "si", "sin", "siniz", "sinler", "su", "sun", "sunlar", "sunuz", "sü", "sün", "sünler", "sünüz", "ta", "tan", "te", "ten", "tý", "týð", "týk", "týkça", "týr", "ti", "tið", "tik", "tikçe", "tir", "tu", "tuð", "tuk", "tukça", "tur", "tü", "tüð", "tük", "tükça", "tür", "u", "ul", "um", "umuz", "un", "unca", "unuz", "up", "ur", "uyor", "uz", "ü", "ül", "ün", "üm", "ümüz", "ünce", "ünüz", "üp", "ür", "üyor", "üz", "ya", "yabil", "yacað", "yacak", "yalým", "yama", "yan", "yarak", "yasýn", "yasýnýz", "yayým", "ydý", "ydi", "ydu", "ydü", "ye", "yebil", "yeceði", "yecek", "yelim", "yeme", "yen", "yerek", "yesin", "yesiniz", "yeyim", "ý", "ým", "ýn", "ýnca", "ýnýz", "ýp", "ýz", "i", "il", "im", "imiz", "in", "ince", "iniz", "ip", "ir", "iyor", "iz", "k", "ken", "la", "le", "mýþ", "miþ", "muþ", "müþ", "or", "sa", "se", "sý", "sýn", "sýnýz", "sýnlar", "si", "sin", "siniz", "sinler", "su", "sun", "sunlar", "sunuz", "sü", "sün", "sünler", "sünüz", "ta", "tan", "te", "ten", "tý", "týð", "týk", "týkça", "týr", "ti", "tið", "tik", "tikçe", "tir", "tu", "tuð", "tuk", "tukça", "tur", "tü", "tüð", "tük", "tükça", "tür", "u", "ul", "um", "umuz", "un", "unca", "unuz", "up", "ur", "uyor", "uz", "ü", "ül", "ün", "üm", "ümüz", "ünce", "ünüz", "üp", "ür", "üyor", "üz", "ya", "yabil", "yacað", "yacak", "yalým", "yama", "yan", "yarak", "yasýn", "yasýnýz", "yayým", "ydý", "ydi", "ydu", "ydü", "ye", "yebil", "yeceði", "yecek", "yelim", "yeme", "yen", "yerek", "yesin", "yesiniz", "yeyim", "ý", "ým", "ýn", "ýnca", "ýnýz", "ýp", "ýz", "i", "il", "im", "imiz", "in", "ince", "iniz", "ip", "ir", "iyor", "iz", "k", "ken", "la", "le", "mýþ", "miþ", "muþ", "müþ", "or", "sa", "se", "sý", "sýn", "sýnýz", "sýnlar", "si", "sin", "siniz", "sinler", "su", "sun", "sunlar", "sunuz", "sü", "sün", "sünler", "sünüz", "ta", "tan", "te", "ten", "tý", "týð", "týk", "týkça", "týr", "ti", "tið", "tik", "tikçe", "tir", "tu", "tuð", "tuk", "tukça", "tur", "tü", "tüð", "tük", "tükça", "tür", "u", "ul", "um", "umuz", "un", "unca", "unuz", "up", "ur", "uyor", "uz", "ü", "ül", "ün", "üm", "ümüz", "ünce", "ünüz", "üp", "ür", "üyor", "üz", "ya", "yabil", "yacað", "yacak", "yalým", "yama", "yan", "yarak", "yasýn", "yasýnýz", "yayým", "ydý", "ydi", "ydu", "ydü", "ye", "yebil", "yeceði", "yecek", "yelim", "yeme", "yen", "yerek", "yesin", "yesiniz", "yeyim"]
    b2 = []
    if b10 in b1:
        b2.append(b10)
    for ind in range(1, len(b10)):
        if b10[:ind] in b1:
            cont, b3 = fonk1(b10[ind:])
            if cont:
                b3 = [b10[:ind] + "+" + l for l in b3]
                b2.extend(b3)
    return len(b2) > 0, b2
def fonk2(root, b10, b5, b4):
    if b4 = = "unsuz yumusamasi":
        return len(b10) > 0 and b10[0] in ["a", "e", "ý", "i", "o", "ö", "u", "ü"] and fonk1(b10)[0]
    if b4 = = "unlu daralmasi":
        if (b5 = = "demek" or b5 == "yemek") and fonk1(b10)[0]:
            return True
        if b10.startswith("yor"):
            b6 = next((letter for letter in reversed(b5[:-3]) if letter in ["a", "e", "ý", "i", "o", "ö", "u", "ü"]), None)
            if b6 in ["a", "e"] and fonk1(b10)[0]:
                return True
        return False
    if b4 = = "fiil" or b4 == "olumsuzluk eki":
        return fonk1(b10)[0] and not ((root.endswith("la") or root.endswith("le")) and b10.startswith("r"))
    if b4 = = "unlu dusmesi":
        b7 = sum(1 for letter in b5 if letter in ["a", "e", "ý", "i", "o", "ö", "u", "ü"])
        b6 = next((letter for letter in reversed(b5) if letter in ["a", "e", "ý", "i", "o", "ö", "u", "ü"]), None)
        if fonk1(b10)[0] and b7 = = 2 and (b6 in ["ý", "i", "u", "ü"]) and (
                len(b10) > 0 and b10[0] in ["a", "e", "ý", "i", "o", "ö", "u", "ü"]):
            if b6 = = "ý":
                return b10[0] in ["a", "ý"]
            elif b6 = = "i":
                return b10[0] in ["e", "i"]
            elif b6 = = "u":
                return b10[0] in ["a", "u"]
            elif b6 = = "ü":
                return b10[0] in ["e", "ü"]
        return False
    return True
def fonk3(b20, b21):
    b8 = []
    if "'" in b20:
        b8.append([b20[:b20.index("'")] + "_1", "tirnaksiz", b20])
    b9 = []
    for i in range(len(b20)):
        b5 = b20[:len(b20) - i]
        b10 = b20[len(b20) - i:]
        a1 = 1
        while b5 + "_" + str(a1) in b21:
            if fonk2(b5, b10, b21[b5 + "_" + str(a1)][1], b21[b5 + "_" + str(a1)][0]):
                b11 = b21[b5 + "_" + str(a1)]
                while b11[0] not in ["kok", "fiil", "olumsuzluk"]:
                    b11 = b21[b11[1]]
                b9.append([b11[1], b21[b5 + "_" + str(a1)][0], b5 + "_" + str(a1)])
            a1 += 1
    b12 = []
    for kel in b9:
        b13 = kel[0][:kel[0].index("_")]
        b14 = len(b13)
        if b13.endswith("mak") or b13.endswith("mek"):
            b14 -= 3
        b15 = True
        for index in range(len(b12)):
            b16 = b12[index]
            b17 = b16[0][:b16[0].index("_")]
            b18 = len(b17)
            if b17.endswith("mak") or b17.endswith("mek"):
                b18 -= 3
            if b14 > b18:
                b12.insert(index, kel)
                b15 = False
        if b15:
            b12.append(kel)
    b19 = b8 + b12
    if len(b19) == 0:
        b19.append([b20 + "_1", "çaresiz", b20 + "_1"])
    return b19
def fonk4():
    try:
        with open('revisedDict.pkl', 'rb') as f:
            return pickle.load(f)
    except IOError:
        print("Please run trainLexicon.py to generate revisedDict.pkl file")
        sys.exit(1)
def fonk5():
    if len(sys.argv) < 2:
        print("Please provide a b20 as a system argument")
        sys.exit(1)
    b20 = sys.argv[1]
    print("Possible lemmas for", b20, "in ranked order:")
    b21 = fonk4()
    b22 = fonk3(b20.lower(), b21)
    for finding in b22:
        print(finding[0])
if b23 = = "__main__":
    fonk5()