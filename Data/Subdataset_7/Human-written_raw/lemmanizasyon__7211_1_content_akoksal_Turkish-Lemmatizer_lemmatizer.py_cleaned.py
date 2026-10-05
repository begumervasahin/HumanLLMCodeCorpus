import re
import json
import pickle
import sys
def fonk1(root, b6, b2, b1):
    if b1 = = "unsuz yumusamasi":
        return len(b6)>0 and b6[0] in ["a","e","Ä±","i","o","Ã¶","u","Ã¼"] and fonk3(b6)[0]
    if b1 = = "unlu daralmasi":
        if b2 = ="demek" and fonk3(b6)[0]:
            return True
        if b2 = ="yemek" and fonk3(b6)[0]:
            return True
        if b6.startswith("yor"):
            b3 = ""
            for letter in reversed(b2[:-3]):
                if letter in ["a","e","Ä±","i","o","Ã¶","u","Ã¼"]:
                    b3 = letter
                    break
            if b3 in ["a","e"] and fonk3(b6)[0]:
                return True
        return False
    if b1 = = "fiil" or b1 == "olumsuzluk eki":
        return fonk3(b6)[0] and not ((root.endswith("la") or (root.endswith("le"))) and b6.startswith("r"))
    if b1 = = "unlu dusmesi":
        a1 = 0
        for letter in b2:
            if letter in ["a","e","Ä±","i","o","Ã¶","u","Ã¼"]:
                a1+=1
                b3 = letter
        if fonk3(b6)[0] and a1 = =2 and (b3 in ["Ä±","i","u","Ã¼"]) and (len(b6)>0 and b6[0] in ["a","e","Ä±","i","o","Ã¶","u","Ã¼"]):
            if b3 = = "Ä±":
                return b6[0] in ["a","Ä±"]
            elif b3 = = "i":
                return b6[0] in ["e","i"]
            elif b3 = = "u":
                return b6[0] in ["a","u"]
            elif b3 = = "Ã¼":
                return b6[0] in ["e","Ã¼"]
        return False
    return True
def fonk2(kelime,b19):
    b4 = []
    if "'" in kelime:
        b4.append([kelime[:kelime.index("'")]+"_1","tirnaksiz",kelime])
    b5 = []
    for i in range(len(kelime)):
        b2 = kelime[:len(kelime)-i]
        b6 = kelime[len(kelime)-i:]
        a2 = 1
        while b2+"_"+str(a2) in b19:
            if fonk1(b2, b6, b19[b2+"_"+str(a2)][1], b19[b2+"_"+str(a2)][0]):
                b7 = (b19[b2+"_"+str(a2)])
                while b7[0] not in ["kok","fiil","olumsuzluk"]:
                    b7 = b19[b7[1]]
                b5.append([b7[1], b19[b2+"_"+str(a2)][0],b2+"_"+str(a2)])
            a2 = a2+1
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
            if(b10>b14):
                b8.insert(index,kel)
                b11 = False
        if b11:
            b8.append(kel)
    b15 = b4+b8
    if len(b15)==0:
        b15.append([kelime+"_1","Ã§aresiz",kelime+"_1",])
    return b15
def fonk3(suff):
    b16 = ["","a", "abil", "acaÄ", "acak", "alÄ±m", "ama", "an", "ar", "arak", "asÄ±n", "asÄ±nÄ±z", "ayÄ±m", "da", "dan", "de", "den", "dÄ±", "dÄ±Ä", "dÄ±k", "dÄ±kÃ§a", "dÄ±r", "di", "diÄ", "dik", "dikÃ§e", "dir", "du", "duÄ", "duk", "dukÃ§a", "dur", "dÃ¼", "dÃ¼Ä", "dÃ¼k", "dÃ¼kÃ§e", "dÃ¼r", "e", "ebil", "eceÄ", "ecek", "elim", "eme", "en", "er", "erek", "esin", "esiniz", "eyim", "Ä±", "Ä±b4", "Ä±m", "Ä±mÄ±z", "Ä±n", "Ä±nca", "Ä±nÄ±z", "Ä±p", "Ä±r", "Ä±yor", "Ä±z", "i", "il", "im", "imiz", "in", "ince", "iniz", "ip", "ir", "iyor", "iz", "k", "ken", "la", "lar", "larÄ±", "larÄ±n", "le", "ler", "leri", "lerin", "m", "ma", "madan", "mak", "maksÄ±zÄ±n", "makta", "maktansa", "malÄ±", "maz", "me", "meden", "mek", "meksizin", "mekte", "mektense", "meli", "mez", "mÄ±", "mÄ±Å", "mÄ±z", "mi", "miÅ", "miz", "mu", "muÅ", "mÃ¼", "muz", "mÃ¼Å", "mÃ¼z", "n", "nÄ±n", "nÄ±z", "nin", "niz", "nun", "nuz", "nÃ¼n", "nÃ¼z", "r", "sa", "se", "sÄ±", "sÄ±n", "sÄ±nÄ±z", "sÄ±nlar", "si", "sin", "siniz", "sinler", "su", "sun", "sunlar", "sunuz", "sÃ¼", "sÃ¼n", "sÃ¼nler", "sÃ¼nÃ¼z", "ta", "tan", "te", "ten", "tÄ±", "tÄ±Ä", "tÄ±k", "tÄ±kÃ§a", "tÄ±r", "ti", "tiÄ", "tik", "tikÃ§e", "tir", "tu", "tuÄ", "tuk", "tukÃ§a", "tur", "tÃ¼", "tÃ¼Ä", "tÃ¼k", "tÃ¼kÃ§e", "tÃ¼r", "u", "ul", "um", "umuz", "un", "unca", "unuz", "up", "ur", "uyor", "uz", "Ã¼", "Ã¼l", "Ã¼n", "Ã¼m", "Ã¼mÃ¼z", "Ã¼nce", "Ã¼nÃ¼z", "Ã¼p", "Ã¼r", "Ã¼yor", "Ã¼z", "ya", "yabil", "yacaÄ", "yacak", "yalÄ±m", "yama", "yan", "yarak", "yasÄ±n", "yasÄ±nÄ±z", "yayÄ±m", "ydÄ±", "ydi", "ydu", "ydÃ¼", "ye", "yebil", "yeceÄ", "yecek", "yelim", "yeme", "yen", "yerek", "yesin", "yesiniz", "yeyim", "yÄ±", "yÄ±m", "yÄ±n", "yÄ±nca", "yÄ±nÄ±z", "yÄ±p", "yÄ±z", "yi", "yim", "yin", "yince", "yiniz", "yip", "yiz", "yken", "yla", "yle", "ymÄ±Å", "ymiÅ", "ymuÅ", "ymÃ¼Å", "yor", "ysa", "yse", "yu", "yum", "yun", "yunca", "yunuz", "yup", "yÃ¼", "yuz", "yÃ¼m", "yÃ¼n", "yÃ¼nce", "yÃ¼nÃ¼z", "yÃ¼p", "yÃ¼z"]
    b17 = []
    if suff in b16:
        b17.append(suff)
    for ind in range(1,len(suff)):
        if(suff[:ind] in b16):
            cont, b18 = fonk3(suff[ind:])
            if cont:
                b18 = [suff[:ind]+"+"+b4 for b4 in b18]
                b17 = b17+b18
    return len(b17)>0,b17
try:
	with open('b19.pkl', 'rb') as f:
		b19 = pickle.load(f)
except IOError:
	print("Please run trainLexicon.py to generate b19.pkl file")
if(len(sys.argv)<1):
	print("Please provide a b20 as a system arguments")
	sys.exit(0)
b20 = sys.argv[1]
print("Possible lemmas for",b20,"in ranked order:")
b21 = fonk2(b20.lower(), b19)
for finding in b21:
	print(finding[0])