
import os
import json
import zipfile
import bisect
import sys
import nltk
from nltk.stem import WordNetLemmatizer
b1 = '{http:
b2 = b1 + 'p'
b3 = b1 + 't'
b4 = set(["i","me","my","myself","we","our","ours","ourselves","you","your","yours","yourself","yourselves","he","him","his","himself","she","her","hers","herself","it","its","itself","they","them","their","theirs","themselves","what","which","who","whom","this","that","these","those","am","is","are","was","were","be","been","being","have","has","had","having","do","does","did","doing","a","an","the","and","but","if","or","because","as","until","while","of","at","by","for","with","about","against","between","into","through","during","before","after","above","below","to","from","up","down","in","out","on","off","over","under","again","further","then","once","here","there","when","where","why","how","all","any","both","each","few","more","most","other","some","such","no","nor","not","only","own","same","so","than","too","very","s","t","can","will","just","don","should","now"])
def fonk1(path):
    b5 = zipfile.ZipFile(path)
    b6 = b5.read('word/b5.xml')
    b5.close()
    b7 = XML(b6)
    b8 = []
    for paragraph in b7.getiterator(b2):
        b9 = [node.text for node in paragraph.getiterator(b3) if node.text]
        if b9:
            b8.append(''.join(b9))
    return '\n\n'.join(b8)
def fonk2(wordlist):
    return [set(wordlist) - b4]
if len(sys.argv) < 2:
    print("Missing argument. Expected input docs directory as argument.\nEg: python create_index.py data")
    sys.exit()
b10 = sys.argv[1]
b11 = "b11.INDEX"
b12 = open(b11,'w')
b13 = {}
b14 = WordNetLemmatizer()
def fonk3(postings, docid):
    bisect.insort(postings, docid)
    return postings
for filename in os.listdir(b10):
    if filename.endswith(".docx"):
        b15 = fonk1(os.path.join(b10,filename))
        b16 = b15.split(' ')
        for w in b16:
            if w in b4:
                continue
            b17 = b14.lemmatize(w)
            try:
                b18 = b13[b17]
                if filename in b18['postings']:
                    continue
                b18['df'] += 1
                b18['postings'] = fonk3(b18['postings'],filename)
            except KeyError:
                b13[b17] = {'df': 1,'postings':[filename]}
b19 = json.dumps(b13, sort_keys = True)
b12.write(b19)
print("Index file created at b11.INDEX")
print("Index stats\n"+'-'*50)
print("Number of terms: "+ str(len(b13)))