import re
import json
import pickle
import sys
def fonk1(b1):
    if b1 = = "wiktionary":
        with open('Datasets/wiktionary.pkl','rb') as f:
            [wordList] = pickle.load(f)
        b2 = {}
        for i in range(len(wordList)):
            b3 = wordList[i].replace("Ã¢","a")
            b2[fonk2(b2, b3)] = ["kok",fonk2(b2, b3)]
        return b2
    elif b1 = = "zargan":
        with open('Datasets/zargan.pkl','rb') as f:
            b4 = pickle.load(f)
        b2 = {}
        for b3, valueList in b4.items():
            b3 = b3.replace("Ã¢","a")
            b2[fonk2(b2, b3)] = ["kok",fonk2(b2, b3)]
        return b2
def fonk2(b2, b3):
    a1 = 1
    while b3+"_"+str(a1) in b2:
        a1 = a1+1
    return b3+"_"+str(a1)
def fonk3(b2, b6):
    b5 = {}
    if b6 = = "olumsuzluk eki":
        for b8, valueList in b2.items():
            b7 = b8[b8.index("_")+1:]
            b8 = b8[:b8.index("_")]
            if b8.endswith("mak"):
                b8 = b8[:-3]+"mamak"
                b5[fonk2(b2, b8)] =  ["olumsuzluk",b8+"_"+b7]
            if b8.endswith("mek"):
                b8 = b8[:-3]+"memek"
                b5[fonk2(b2, b8)] =  ["olumsuzluk",b8+"_"+b7]
    elif b6 = = "unsuz yumusamasi":
        for b8, valueList in b2.items():
            b7 = b8[b8.index("_")+1:]
            b8 = b8[:b8.index("_")]
            if not (b8.endswith("mak") or b8.endswith("mek")):
                if b8.endswith("p"):
                    b5[fonk2(b2, b8[:-1]+"b")] = ["unsuz yumusamasi", b8+"_"+b7]
                elif b8.endswith("Ã§"):
                    b5[fonk2(b2, b8[:-1]+"c")] = ["unsuz yumusamasi", b8+"_"+b7]
                elif b8.endswith("t"):
                    b5[fonk2(b2, b8[:-1]+"d")] = ["unsuz yumusamasi", b8+"_"+b7]
                elif b8.endswith("k"):
                    if b8.endswith("nk"):
                        b5[fonk2(b2, b8[:-1]+"g")] = ["unsuz yumusamasi", b8+"_"+b7]
                    else:
                        b5[fonk2(b2, b8[:-1]+"Ä")] = ["unsuz yumusamasi", b8+"_"+b7]
    elif b6 = = "unlu daralmasi":
         for b8, valueList in b2.items():
            b7 = b8[b8.index("_")+1:]
            b8 = b8[:b8.index("_")]
            if b8 = = "demek":
                b5[fonk2(b2, "di")] = ["unlu daralmasi", b8+"_"+b7]
            elif b8 = = "yemek":
                b5[fonk2(b2, "yi")] = ["unlu daralmasi", b8+"_"+b7]
            elif b8.endswith("amak"):
                b5[fonk2(b2, b8[:-4]+"Ä±")] = ["unlu daralmasi", b8+"_"+b7]
                b5[fonk2(b2, b8[:-4]+"u")] = ["unlu daralmasi", b8+"_"+b7]
            elif b8.endswith("emek"):
                b5[fonk2(b2, b8[:-4]+"i")] = ["unlu daralmasi", b8+"_"+b7]
                b5[fonk2(b2, b8[:-4]+"Ã¼")] = ["unlu daralmasi", b8+"_"+b7]
    elif b6 = = "unlu dusmesi":
         for b8, valueList in b2.items():
            b7 = b8[b8.index("_")+1:]
            b8 = b8[:b8.index("_")]
            b9 = {'akis': 'aks', 'akÄ±l': 'akl', 'alÄ±n': 'aln','asÄ±l': 'asl','asÄ±r': 'asr','atÄ±f': 'atf', 'avuÃ§': 'avc','azim': 'azm', 'aÄÄ±z': 'aÄz', 'bahis': 'bahs','baÄÄ±r': 'baÄr','beniz': 'benz','beyin': 'beyn','boyun': 'boyn','burun': 'burn','bÃ¶ÄÃ¼r': 'bÃ¶Är','cebir': 'cebr','cezir': 'cezr','cisim': 'cism','devir': 'devr','emir': 'emr','fasÄ±l': 'fasl','fecir': 'fecr','fesih': 'fesh','fetih': 'feth','fikir': 'fikr','geniz': 'genz','gÃ¶nÃ¼l': 'gÃ¶nl','gÃ¶ÄÃ¼s': 'gÃ¶Äs','hacim': 'hacm','haciz': 'hacz','hapis': 'haps','hatÄ±r': 'hatr','hayÄ±r': 'hayr','hazÄ±m': 'hazm','hÃ¼kÃ¼m': 'hÃ¼km','hÃ¼zÃ¼n': 'hÃ¼zn','hÄ±sÄ±m': 'hÄ±sm','hÄ±ÅÄ±m': 'hÄ±Åm','isim': 'ism','izin': 'izn','kabir': 'kabr','kahÄ±r': 'kahr','karÄ±n': 'karn','kasÄ±r': 'kasr','kasÄ±t': 'kast','kayÄ±p': 'kayb','kayÄ±t': 'kayd','kesir': 'kesr','keyif': 'keyf','keÅif': 'keÅf','kibir': 'kibr','koyun': 'koyn','kusur': 'kusr','kutup': 'kutp','kÃ¼fÃ¼r': 'kÃ¼fr','kÄ±sÄ±m': 'kÄ±sm','metin': 'metn','misil': 'misl','mÃ¼hÃ¼r': 'mÃ¼hr','nabÄ±z': 'nabz','nakil': 'nakl','nakit': 'nakt','nefis': 'nefs','nehir': 'nehr','nesil': 'nesl','nutuk': 'nutk','omuz': 'omz','oÄul': 'oÄl','rehin': 'rehn','resim': 'resm','ritim': 'ritm','sabÄ±r': 'sabr','seyir': 'seyr','tavÄ±r': 'tavr','ufuk': 'ufk','umur': 'umr','vakit': 'vakt','vakÄ±f': 'vakf','vasÄ±f': 'vasf','zikir': 'zikr','zulÃ¼m': 'zulm','Ã¶mÃ¼r': 'Ã¶mr','Ã¶zÃ¼r': 'Ã¶zr','ÅahÄ±s': 'Åahs','Åehir': 'Åehr','Åekil': 'Åekl','ÅÃ¼kÃ¼r': 'ÅÃ¼kr', 'zehir':'zehr'}
            if b8 in b9:
                b5[fonk2(b2,b9[b8])] = ["unlu dusmesi", b8+"_"+b7]
    elif b6 = = "fiil":
        for b8, valueList in b2.items():
            b7 = b8[b8.index("_")+1:]
            b8 = b8[:b8.index("_")]
            if b8.endswith("mek") or b8.endswith("mak"):
                b5[fonk2(b2, b8[:-3])] = ["fiil", b8+"_"+b7]
    return b5
def fonk4(b10, b5):
    for b8, valueList in b5.items():
        if b8 in b10:
            b10[fonk2(b10, b8[:b8.index("_")])] = valueList
        else:
            b10[b8] = valueList
    return b10
b1 = "zargan"
if(len(sys.argv)>1):
	b1 = sys.argv[1]
b2 = fonk1(b1)
b2 = fonk4(b2, (fonk3(b2,"olumsuzluk eki")))
print("Negative verbs are added.")
b2 = fonk4(b2, (fonk3(b2,"fiil")))
print("Zero infinitive forms of verbs are added.")
b10 = dict(b2)
for b6 in ["unsuz yumusamasi","unlu daralmasi","unlu dusmesi"]:
    b5 = {}
    b5 = fonk3(b2,b6)
    b10 = fonk4(b10,b5)
    if b6 = ="unsuz yumusamasi":
        print("Consonant softening forms are added.")
    if b6 = ="unlu daralmasi":
        print("Becoming close vowel forms are added.")
    if b6 = ="unsuz yumusamasi":
        print("Dropping vowel forms are added.")
with open('b10.pkl', 'wb') as f:
    pickle.dump(b10, f)
print("Transformed lexicon is saved to b10.pkl")