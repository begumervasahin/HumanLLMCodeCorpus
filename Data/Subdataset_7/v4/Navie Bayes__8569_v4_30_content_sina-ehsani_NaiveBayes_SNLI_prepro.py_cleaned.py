from data_utils import savedata
import json
import re
import numpy as np
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
b1 = WordNetLemmatizer()
b2 = PorterStemmer()
def fonk1(parse):
    return parse.replace('(', ' ').replace(')', ' ').replace('-LRB-', '(').replace('-RRB-', ')').split()
def fonk2(fn, b3 = True, b11=None):
    for i, line in enumerate(open(fn)):
        if b11 and i > b11:
            break
        b4 = json.loads(line)
        b5 = b4['gold_label']
        b6 = ' '.join(fonk1(b4['sentence1_binary_parse']))
        b7 = ' '.join(fonk1(b4['sentence2_binary_parse']))
        if b3 and b5 = = '-':
            continue
        yield (b5, b6, b7)
def fonk3(sentence_list):
    b8 = []
    for b9 in sentence_list:
        b9 = re.sub(r"[^a-zA-Z]", " ", b9)
        b10 = b9.lower().split()
        b10 = [b2.stem(w) for w in b10]
        b8.append(" ".join(b10))
    return b8
def fonk4(fn, b11 = None):
    b12 = list(fonk2(fn=fn, b11=b11))
    b13 = [b6 for _, b6, b7 in b12]
    b14 = [b7 for _, b6, b7 in b12]
    b13 = fonk3(b13)
    b14 = fonk3(b14)
    b15 = {'contradiction': 0, 'neutral': 1, 'entailment': 2}
    b16 = np.array([b15[l] for l, _, _ in b12])
    return b13, b14, b16
def fonk5():
    b17 = fonk4('snli_1.0/snli_1.0_train.jsonl')
    b18 = fonk4('snli_1.0/snli_1.0_test.jsonl')
    b19 = fonk4('snli_1.0/snli_1.0_dev.jsonl')
    savedata(b18, "test_stem")
    savedata(b17, "train_stem")
    savedata(b19, "dev_stem")
if b20 = = '__main__':
    fonk5()