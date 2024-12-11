
import os
import json
import zipfile
import bisect
import sys
from nltk.stem import WordNetLemmatizer
from xml.etree.cElementTree import XML
b1 = '{http:
b2 = b1 + 'p'
b3 = b1 + 't'
b4 = set(["i","me","my","myself","we","our","ours","ourselves","you","your","yours","yourself","yourselves","he","him","his","himself","she","her","hers","herself","it","its","itself","they","them","their","theirs","themselves","what","which","who","whom","this","that","these","those","am","is","are","was","were","be","been","being","have","has","had","having","do","does","did","doing","a","an","the","and","but","if","or","because","as","until","while","of","at","by","for","with","about","against","between","into","through","during","before","after","above","below","to","from","up","down","in","out","on","off","over","under","again","further","then","once","here","there","when","where","why","how","all","any","both","each","few","more","most","other","some","such","no","nor","not","only","own","same","so","than","too","very","s","t","can","will","just","don","should","now"])
def fonk1(path):
    with zipfile.ZipFile(path) as document:
        b5 = document.read('word/document.xml')
    b6 = XML(b5)
    b7 = [''.join(node.text for node in paragraph.getiterator(b3) if node.text) for paragraph in b6.getiterator(b2)]
    return '\n\n'.join(b7)
def fonk2(wordlist):
    return [word for word in wordlist if word not in b4]
if len(sys.argv) < 2:
    print("Missing argument. Expected input docs directory as argument.\nEg: python create_index.py data")
    sys.exit()
b8 = sys.argv[1]
b9 = "b9.INDEX"
b10 = {}
b11 = WordNetLemmatizer()
def fonk3(postings, docid):
    bisect.insort(postings, docid)
    return postings
for filename in os.listdir(b8):
    if filename.endswith(".docx"):
        b12 = fonk1(os.path.join(b8, filename))
        b13 = fonk2(b12.split())
        for word in b13:
            b14 = b11.lemmatize(word)
            b10.setdefault(b14, {'df': 0, 'postings': []})
            if filename not in b10[b14]['postings']:
                b10[b14]['df'] += 1
                b10[b14]['postings'] = fonk3(b10[b14]['postings'], filename)
with open(b9, 'w') as index_file:
    json.dump(b10, index_file, b15 = True)
print("Index file created at b9.INDEX")
print("Index stats\n" + '-' * 50)
print("Number of terms:", len(b10))