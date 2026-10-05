import re
import json
import pickle
import sys
def loadWord(dataset):
    if dataset == "wiktionary":
        with open('Datasets/wiktionary.pkl','rb') as f:
            [wordList] = pickle.load(f)
        wordDict = {}
        for i in range(len(wordList)):
            word = wordList[i].replace("Ã¢","a")
            wordDict[findID(wordDict, word)] = ["kok",findID(wordDict, word)]
        return wordDict
    elif dataset == "zargan":
        with open('Datasets/zargan.pkl','rb') as f:
            zarganDict = pickle.load(f)
        wordDict = {}
        for word, valueList in zarganDict.items():
            word = word.replace("Ã¢","a")
            wordDict[findID(wordDict, word)] = ["kok",findID(wordDict, word)]
        return wordDict
def findID(wordDict, word):
    ct = 1
    while word+"_"+str(ct) in wordDict:
        ct = ct+1
    return word+"_"+str(ct)
def generate(wordDict, olay):
    newDict = {}
    if olay == "olumsuzluk eki":
        for kelime, valueList in wordDict.items():
            ind = kelime[kelime.index("_")+1:]
            kelime = kelime[:kelime.index("_")]
            if kelime.endswith("mak"):
                kelime = kelime[:-3]+"mamak"
                newDict[findID(wordDict, kelime)] =  ["olumsuzluk",kelime+"_"+ind]
            if kelime.endswith("mek"):
                kelime = kelime[:-3]+"memek"
                newDict[findID(wordDict, kelime)] =  ["olumsuzluk",kelime+"_"+ind]
    elif olay == "unsuz yumusamasi":
        for kelime, valueList in wordDict.items():
            ind = kelime[kelime.index("_")+1:]
            kelime = kelime[:kelime.index("_")]
            if not (kelime.endswith("mak") or kelime.endswith("mek")):
                if kelime.endswith("p"):
                    newDict[findID(wordDict, kelime[:-1]+"b")] = ["unsuz yumusamasi", kelime+"_"+ind]
                elif kelime.endswith("Ã§"):
                    newDict[findID(wordDict, kelime[:-1]+"c")] = ["unsuz yumusamasi", kelime+"_"+ind]
                elif kelime.endswith("t"):
                    newDict[findID(wordDict, kelime[:-1]+"d")] = ["unsuz yumusamasi", kelime+"_"+ind]
                elif kelime.endswith("k"):
                    if kelime.endswith("nk"):
                        newDict[findID(wordDict, kelime[:-1]+"g")] = ["unsuz yumusamasi", kelime+"_"+ind]
                    else:
                        newDict[findID(wordDict, kelime[:-1]+"Ä")] = ["unsuz yumusamasi", kelime+"_"+ind]
    elif olay == "unlu daralmasi":
         for kelime, valueList in wordDict.items():
            ind = kelime[kelime.index("_")+1:]
            kelime = kelime[:kelime.index("_")]
            if kelime == "demek":
                newDict[findID(wordDict, "di")] = ["unlu daralmasi", kelime+"_"+ind]
            elif kelime == "yemek":
                newDict[findID(wordDict, "yi")] = ["unlu daralmasi", kelime+"_"+ind]
            elif kelime.endswith("amak"):
                newDict[findID(wordDict, kelime[:-4]+"Ä±")] = ["unlu daralmasi", kelime+"_"+ind]
                newDict[findID(wordDict, kelime[:-4]+"u")] = ["unlu daralmasi", kelime+"_"+ind]
            elif kelime.endswith("emek"):
                newDict[findID(wordDict, kelime[:-4]+"i")] = ["unlu daralmasi", kelime+"_"+ind]
                newDict[findID(wordDict, kelime[:-4]+"Ã¼")] = ["unlu daralmasi", kelime+"_"+ind]
    elif olay == "unlu dusmesi":
         for kelime, valueList in wordDict.items():
            ind = kelime[kelime.index("_")+1:]
            kelime = kelime[:kelime.index("_")]
            dusmeDict = {'akis': 'aks', 'akÄ±l': 'akl', 'alÄ±n': 'aln','asÄ±l': 'asl','asÄ±r': 'asr','atÄ±f': 'atf', 'avuÃ§': 'avc','azim': 'azm', 'aÄÄ±z': 'aÄz', 'bahis': 'bahs','baÄÄ±r': 'baÄr','beniz': 'benz','beyin': 'beyn','boyun': 'boyn','burun': 'burn','bÃ¶ÄÃ¼r': 'bÃ¶Är','cebir': 'cebr','cezir': 'cezr','cisim': 'cism','devir': 'devr','emir': 'emr','fasÄ±l': 'fasl','fecir': 'fecr','fesih': 'fesh','fetih': 'feth','fikir': 'fikr','geniz': 'genz','gÃ¶nÃ¼l': 'gÃ¶nl','gÃ¶ÄÃ¼s': 'gÃ¶Äs','hacim': 'hacm','haciz': 'hacz','hapis': 'haps','hatÄ±r': 'hatr','hayÄ±r': 'hayr','hazÄ±m': 'hazm','hÃ¼kÃ¼m': 'hÃ¼km','hÃ¼zÃ¼n': 'hÃ¼zn','hÄ±sÄ±m': 'hÄ±sm','hÄ±ÅÄ±m': 'hÄ±Åm','isim': 'ism','izin': 'izn','kabir': 'kabr','kahÄ±r': 'kahr','karÄ±n': 'karn','kasÄ±r': 'kasr','kasÄ±t': 'kast','kayÄ±p': 'kayb','kayÄ±t': 'kayd','kesir': 'kesr','keyif': 'keyf','keÅif': 'keÅf','kibir': 'kibr','koyun': 'koyn','kusur': 'kusr','kutup': 'kutp','kÃ¼fÃ¼r': 'kÃ¼fr','kÄ±sÄ±m': 'kÄ±sm','metin': 'metn','misil': 'misl','mÃ¼hÃ¼r': 'mÃ¼hr','nabÄ±z': 'nabz','nakil': 'nakl','nakit': 'nakt','nefis': 'nefs','nehir': 'nehr','nesil': 'nesl','nutuk': 'nutk','omuz': 'omz','oÄul': 'oÄl','rehin': 'rehn','resim': 'resm','ritim': 'ritm','sabÄ±r': 'sabr','seyir': 'seyr','tavÄ±r': 'tavr','ufuk': 'ufk','umur': 'umr','vakit': 'vakt','vakÄ±f': 'vakf','vasÄ±f': 'vasf','zikir': 'zikr','zulÃ¼m': 'zulm','Ã¶mÃ¼r': 'Ã¶mr','Ã¶zÃ¼r': 'Ã¶zr','ÅahÄ±s': 'Åahs','Åehir': 'Åehr','Åekil': 'Åekl','ÅÃ¼kÃ¼r': 'ÅÃ¼kr', 'zehir':'zehr'}
            if kelime in dusmeDict:
                newDict[findID(wordDict,dusmeDict[kelime])] = ["unlu dusmesi", kelime+"_"+ind]
    elif olay == "fiil":
        for kelime, valueList in wordDict.items():
            ind = kelime[kelime.index("_")+1:]
            kelime = kelime[:kelime.index("_")]
            if kelime.endswith("mek") or kelime.endswith("mak"):
                newDict[findID(wordDict, kelime[:-3])] = ["fiil", kelime+"_"+ind]
    return newDict
def appendDict(revisedDict, newDict):
    for kelime, valueList in newDict.items():
        if kelime in revisedDict:
            revisedDict[findID(revisedDict, kelime[:kelime.index("_")])] = valueList
        else:
            revisedDict[kelime] = valueList
    return revisedDict
dataset="zargan"
if(len(sys.argv)>1):
	dataset = sys.argv[1]
wordDict = loadWord(dataset)
wordDict = appendDict(wordDict, (generate(wordDict,"olumsuzluk eki")))
print("Negative verbs are added.")
wordDict = appendDict(wordDict, (generate(wordDict,"fiil")))
print("Zero infinitive forms of verbs are added.")
revisedDict = dict(wordDict)
for olay in ["unsuz yumusamasi","unlu daralmasi","unlu dusmesi"]:
    newDict = {}
    newDict = generate(wordDict,olay)
    revisedDict = appendDict(revisedDict,newDict)
    if olay=="unsuz yumusamasi":
        print("Consonant softening forms are added.")
    if olay=="unlu daralmasi":
        print("Becoming close vowel forms are added.")
    if olay=="unsuz yumusamasi":
        print("Dropping vowel forms are added.")
with open('revisedDict.pkl', 'wb') as f:
    pickle.dump(revisedDict, f)
print("Transformed lexicon is saved to revisedDict.pkl")