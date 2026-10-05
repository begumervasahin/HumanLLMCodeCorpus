import re
from nltk.stem import PorterStemmer
def extractingdata(filepathdoc, stopWordList):
    ps = PorterStemmer()
    totalDoc = ""
    FinalWordList = []
    docnumListForEachFile = []
    with open(filepathdoc) as fp:
        lines = fp.readlines()
    for line in lines:
        stripedString = line.strip() + " "
        totalDoc = totalDoc + stripedString
        if "<DOCNO>" in stripedString:
            docnum = re.search(r'<DOCNO>(.*?)</DOCNO>', stripedString).group(1)
            docnumListForEachFile.append(docnum)
    TotalText = re.findall(r'<TEXT>(.*?)</TEXT>', totalDoc)
    for text in TotalText:
        text = str(text).strip()
        text = re.sub("\w*-*\d+-*\w*", " ", text)
        text = re.sub("\d+", " ", text)
        text = re.sub("\W+", " ", text)
        lowercaseString = text.lower()
        wordlist = re.split('\s+', lowercaseString)
        for stopWord in stopWordList:
            if stopWord in wordlist:
                wordlist = [word for word in wordlist if word != stopWord]
        stemmedList = [ps.stem(word) for word in wordlist if word]
        FinalWordList.extend(stemmedList)
    return FinalWordList, docnumListForEachFile
stopWordList = ["the", "and", "is", "in", "it", "on"]
filepathdoc = "sample.txt"
final_word_list, doc_num_list = extractingdata(filepathdoc, stopWordList)
print("Final Word List:", final_word_list)
print("Doc Number List For Each File:", doc_num_list)