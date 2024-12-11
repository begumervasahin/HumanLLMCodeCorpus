import json
from langdetect import detect
import re
from collections import Counter
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
b1 = 'CLEAN_AVA_FULL_COMMENTS.json'
b2 = 'b4.json'
def fonk1(b8):
    try:
        return detect(b8) == 'en'
    except:
        return False
def fonk2(b3):
    b3 = re.sub(r'(.)\1+', r'\1\1', b3)
    b3 = re.sub(r'[^\w\s,!.?]', '', b3)
    return b3
def fonk3(b10, bad_words):
    return [token for token in b10 if token.lower() not in bad_words]
def fonk4(b1, b2):
    b4 = []
    b5 = Counter()
    b6 = Counter()
    with open(b1, 'r') as file:
        b7 = json.load(file)
    for item in b7:
        b8 = item.get('comment', '')
        if fonk1(b8):
            b9 = fonk2(b8)
            b10 = word_tokenize(b9)
            b11 = fonk3(b10, ['badword1', 'badword2'])
            b5.update(b11)
            b6.update(ngrams(b11, 2))
            b4.append({'comment': ' '.join(b11)})
    with open(b2, 'w') as file:
        json.dump(b4, file, b12 = 4)
fonk4(b1, b2)