import re
import json
import pickle
import sys
def check(root, suffix, guess, action):
    if action == "unsuz yumusamasi":
        return len(suffix)>0 and suffix[0] in ["a","e","Ä±","i","o","Ã¶","u","Ã¼"] and checkSuffixValidation(suffix)[0]
    if action == "unlu daralmasi":
        if guess=="demek" and checkSuffixValidation(suffix)[0]:
            return True
        if guess=="yemek" and checkSuffixValidation(suffix)[0]:
            return True
        if suffix.startswith("yor"):
            lastVowel = ""
            for letter in reversed(guess[:-3]):
                if letter in ["a","e","Ä±","i","o","Ã¶","u","Ã¼"]:
                    lastVowel = letter
                    break
            if lastVowel in ["a","e"] and checkSuffixValidation(suffix)[0]:
                return True
        return False
    if action == "fiil" or action == "olumsuzluk eki":
        return checkSuffixValidation(suffix)[0] and not ((root.endswith("la") or (root.endswith("le"))) and suffix.startswith("r"))
    if action == "unlu dusmesi":
        count = 0
        for letter in guess:
            if letter in ["a","e","Ä±","i","o","Ã¶","u","Ã¼"]:
                count+=1
                lastVowel = letter
        if checkSuffixValidation(suffix)[0] and count==2 and (lastVowel in ["Ä±","i","u","Ã¼"]) and (len(suffix)>0 and suffix[0] in ["a","e","Ä±","i","o","Ã¶","u","Ã¼"]):
            if lastVowel == "Ä±":
                return suffix[0] in ["a","Ä±"]
            elif lastVowel == "i":
                return suffix[0] in ["e","i"]
            elif lastVowel == "u":
                return suffix[0] in ["a","u"]
            elif lastVowel == "Ã¼":
                return suffix[0] in ["e","Ã¼"]
        return False
    return True
def findPos(kelime,revisedDict):
    l = []
    if "'" in kelime:
        l.append([kelime[:kelime.index("'")]+"_1","tirnaksiz",kelime])
    mid = []
    for i in range(len(kelime)):
        guess = kelime[:len(kelime)-i]
        suffix = kelime[len(kelime)-i:]
        ct = 1
        while guess+"_"+str(ct) in revisedDict:
            if check(guess, suffix, revisedDict[guess+"_"+str(ct)][1], revisedDict[guess+"_"+str(ct)][0]):
                guessList = (revisedDict[guess+"_"+str(ct)])
                while guessList[0] not in ["kok","fiil","olumsuzluk"]:
                    guessList = revisedDict[guessList[1]]
                mid.append([guessList[1], revisedDict[guess+"_"+str(ct)][0],guess+"_"+str(ct)])
            ct = ct+1
    temp = []
    for kel in mid:
        kelime_kok = kel[0][:kel[0].index("_")]
        kelime_len = len(kelime_kok)
        if kelime_kok.endswith("mak") or kelime_kok.endswith("mek"):
            kelime_len -= 3
        not_inserted = True
        for index in range(len(temp)):
            temp_kelime = temp[index]
            temp_kelime_kok = temp_kelime[0][:temp_kelime[0].index("_")]
            temp_len = len(temp_kelime_kok)
            if temp_kelime_kok.endswith("mak") or temp_kelime_kok.endswith("mek"):
                temp_len -= 3
            if(kelime_len>temp_len):
                temp.insert(index,kel)
                not_inserted = False
        if not_inserted:
            temp.append(kel)
    output = l+temp
    if len(output)==0:
        output.append([kelime+"_1","Ã§aresiz",kelime+"_1",])
    return output
def checkSuffixValidation(suff):
    suffixList = ["","a", "abil", "acaÄ", "acak", "alÄ±m", "ama", "an", "ar", "arak", "asÄ±n", "asÄ±nÄ±z", "ayÄ±m", "da", "dan", "de", "den", "dÄ±", "dÄ±Ä", "dÄ±k", "dÄ±kÃ§a", "dÄ±r", "di", "diÄ", "dik", "dikÃ§e", "dir", "du", "duÄ", "duk", "dukÃ§a", "dur", "dÃ¼", "dÃ¼Ä", "dÃ¼k", "dÃ¼kÃ§e", "dÃ¼r", "e", "ebil", "eceÄ", "ecek", "elim", "eme", "en", "er", "erek", "esin", "esiniz", "eyim", "Ä±", "Ä±l", "Ä±m", "Ä±mÄ±z", "Ä±n", "Ä±nca", "Ä±nÄ±z", "Ä±p", "Ä±r", "Ä±yor", "Ä±z", "i", "il", "im", "imiz", "in", "ince", "iniz", "ip", "ir", "iyor", "iz", "k", "ken", "la", "lar", "larÄ±", "larÄ±n", "le", "ler", "leri", "lerin", "m", "ma", "madan", "mak", "maksÄ±zÄ±n", "makta", "maktansa", "malÄ±", "maz", "me", "meden", "mek", "meksizin", "mekte", "mektense", "meli", "mez", "mÄ±", "mÄ±Å", "mÄ±z", "mi", "miÅ", "miz", "mu", "muÅ", "mÃ¼", "muz", "mÃ¼Å", "mÃ¼z", "n", "nÄ±n", "nÄ±z", "nin", "niz", "nun", "nuz", "nÃ¼n", "nÃ¼z", "r", "sa", "se", "sÄ±", "sÄ±n", "sÄ±nÄ±z", "sÄ±nlar", "si", "sin", "siniz", "sinler", "su", "sun", "sunlar", "sunuz", "sÃ¼", "sÃ¼n", "sÃ¼nler", "sÃ¼nÃ¼z", "ta", "tan", "te", "ten", "tÄ±", "tÄ±Ä", "tÄ±k", "tÄ±kÃ§a", "tÄ±r", "ti", "tiÄ", "tik", "tikÃ§e", "tir", "tu", "tuÄ", "tuk", "tukÃ§a", "tur", "tÃ¼", "tÃ¼Ä", "tÃ¼k", "tÃ¼kÃ§e", "tÃ¼r", "u", "ul", "um", "umuz", "un", "unca", "unuz", "up", "ur", "uyor", "uz", "Ã¼", "Ã¼l", "Ã¼n", "Ã¼m", "Ã¼mÃ¼z", "Ã¼nce", "Ã¼nÃ¼z", "Ã¼p", "Ã¼r", "Ã¼yor", "Ã¼z", "ya", "yabil", "yacaÄ", "yacak", "yalÄ±m", "yama", "yan", "yarak", "yasÄ±n", "yasÄ±nÄ±z", "yayÄ±m", "ydÄ±", "ydi", "ydu", "ydÃ¼", "ye", "yebil", "yeceÄ", "yecek", "yelim", "yeme", "yen", "yerek", "yesin", "yesiniz", "yeyim", "yÄ±", "yÄ±m", "yÄ±n", "yÄ±nca", "yÄ±nÄ±z", "yÄ±p", "yÄ±z", "yi", "yim", "yin", "yince", "yiniz", "yip", "yiz", "yken", "yla", "yle", "ymÄ±Å", "ymiÅ", "ymuÅ", "ymÃ¼Å", "yor", "ysa", "yse", "yu", "yum", "yun", "yunca", "yunuz", "yup", "yÃ¼", "yuz", "yÃ¼m", "yÃ¼n", "yÃ¼nce", "yÃ¼nÃ¼z", "yÃ¼p", "yÃ¼z"]
    validList = []
    if suff in suffixList:
        validList.append(suff)
    for ind in range(1,len(suff)):
        if(suff[:ind] in suffixList):
            cont, contList = checkSuffixValidation(suff[ind:])
            if cont:
                contList = [suff[:ind]+"+"+l for l in contList]
                validList = validList+contList
    return len(validList)>0,validList
try:
	with open('revisedDict.pkl', 'rb') as f:
		revisedDict = pickle.load(f)
except IOError:
	print("Please run trainLexicon.py to generate revisedDict.pkl file")
if(len(sys.argv)<1):
	print("Please provide a word as a system arguments")
	sys.exit(0)
word = sys.argv[1]
print("Possible lemmas for",word,"in ranked order:")
findings = findPos(word.lower(), revisedDict)
for finding in findings:
	print(finding[0])