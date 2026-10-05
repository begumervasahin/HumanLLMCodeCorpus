b1 = "Clyde D'Cruz"
b2 = "GPL"
try:
    from xml.etree.cElementTree import XML
except ImportError:
    from xml.etree.ElementTree import XML
import zipfile
import os
import bisect
import json
import nltk
import sys
from nltk.stem import WordNetLemmatizer
b3 = '{http:
b4 = b3 + 'p'
b5 = b3 + 't'
b6 = set(["i","me","my","myself","we","our","ours","ourselves","you","your","yours","yourself","yourselves","he","him","his","himself","she","her","hers","herself","it","its","itself","they","them","their","theirs","themselves","what","which","who","whom","this","that","these","those","am","is","are","was","were","be","been","being","have","has","had","having","do","does","did","doing","a","an","the","and","but","if","or","because","as","until","while","of","at","by","for","with","about","against","between","into","through","during","before","after","above","below","to","from","up","down","in","out","on","off","over","under","again","further","then","once","here","there","when","where","why","how","all","any","both","each","few","more","most","other","some","such","no","nor","not","only","own","same","so","than","too","very","s","t","can","will","just","don","should","now"])
def fonk1(path):
    b7 = zipfile.ZipFile(path)
    b8 = b7.read('word/b7.xml')
    b7.close()
    b9 = XML(b8)
    b10 = []
    for paragraph in b9.getiterator(b4):
        b11 = [node.text
                 for node in paragraph.getiterator(b5)
                 if node.text]
        if b11:
            b10.append(''.join(b11))
    return '\n\n'.join(b10)
def fonk2(wordlist):
    return [set(wordlist) - b6]
if len(sys.argv) < 2:
    print("Missing argument. Expected input docs directory as argument.\nEg: python create_index.py data")
    sys.exit()
b12 = sys.argv[1]
b13 = "b13.INDEX"
b14 = open(b13,'w')
b15 = {}
b16 = WordNetLemmatizer()
def fonk3(postings, docid):
    bisect.insort(postings, docid)
    return postings
for filename in os.listdir(b12):
    if filename.endswith(".docx"):
        b17 = fonk1(os.path.join(b12,filename))
        b18 = b17.split(' ')
        for w in b18:
            if w in b6:
                continue
            b19 = b16.lemmatize(w)
            try:
                b20 = b15[b19]
                if filename in b20['postings']:
                    continue
                b20['df'] += 1
                b20['postings'] = fonk3(b20['postings'],filename)
            except KeyError:
                b15[b19] = {'df': 1,'postings':[filename]}
b21 = json.dumps(b15, sort_keys = True)
b14.write(b21)
print("Index file created at b13.INDEX")
print("Index stats\n"+'-'*50)
print("Number of terms: "+ str(len(b15)))