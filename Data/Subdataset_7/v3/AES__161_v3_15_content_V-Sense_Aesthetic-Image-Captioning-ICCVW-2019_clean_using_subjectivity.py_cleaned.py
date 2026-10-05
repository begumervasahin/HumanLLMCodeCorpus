import json
from langdetect import detect
import re
from collections import Counter
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
b1 = 'CLEAN_AVA_FULL_COMMENTS.json'
b2 = 'b4.json'
def fonk1(comment):
    try:
        return detect(comment) == 'en'
    except Exception as e:
        print(f"Error detecting language: {e}")
        return False
def fonk2(b3):
    b3 = re.sub(r'(.)\1+', r'\1\1', b3)
    b3 = re.sub(r'[^\w\s,!.?]', '', b3)
    return b3
def fonk3(b9, bad_words):
    return [token for token in b9 if token.lower() not in bad_words]
def fonk4(input_path, output_path):
    b4 = []
    b5 = Counter()
    b6 = Counter()
    with open(input_path, 'r') as file:
        b7 = json.load(file)
    for comment in b7:
        b3 = comment.get('comment', '')
        if fonk1(b3):
            b8 = fonk2(b3)
            b9 = word_tokenize(b8)
            b10 = fonk3(b9, ['badword1', 'badword2'])
            b5.update(b10)
            b6.update(ngrams(b10, 2))
            b4.append({'comment': ' '.join(b10)})
    with open(output_path, 'w') as file:
        json.dump(b4, file, b11 = 4)
fonk4(b1, b2)