import json
from langdetect import detect
import re
from collections import Counter
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
b1 = 'CLEAN_AVA_FULL_COMMENTS.json'
b2 = 'b5.json'
def fonk1(b9):
    try:
        return detect(b9) == 'en'
    except:
        return False
def fonk2(b3):
    b3 = re.sub(r'(.)\1+', r'\1\1', b3)
    b3 = re.sub(r'[^\w\s,!.?]', '', b3)
    return b3
def fonk3(b3, bad_words):
    b4 = word_tokenize(b3)
    b4 = [token for token in b4 if token.lower() not in bad_words]
    return b4
def fonk4(b1, b2):
    b5 = []
    b6 = Counter()
    b7 = Counter()
    with open(b1, 'r') as f:
        b8 = json.load(f)
    for item in b8:
        b9 = item.get('b9', '')
        if fonk1(b9):
            b10 = fonk2(b9)
            b4 = fonk3(b10, ['badword1', 'badword2'])
            b6.update(b4)
            b7.update(ngrams(b4, 2))
            b5.append({'b9': ' '.join(b4)})
    with open(b2, 'w') as f:
        json.dump(b5, f, b11 = 4)
fonk4(b1, b2)