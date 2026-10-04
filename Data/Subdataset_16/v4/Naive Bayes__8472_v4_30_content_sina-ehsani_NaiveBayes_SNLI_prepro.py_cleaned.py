import json
import re
import numpy as np
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from data_utils import savedata
b1 = WordNetLemmatizer()
b2 = PorterStemmer()
def fonk1(parse):
    return parse.replace('(', ' ').replace(')', ' ').replace('-LRB-', '(').replace('-RRB-', ')').split()
def fonk2(fn, b3 = True, b12=None):
    with open(fn, 'r', b4 = 'utf-8') as f:
        for i, line in enumerate(f):
            if b12 and i >= b12:
                break
            b5 = json.loads(line)
            b6 = b5['gold_label']
            b7 = ' '.join(fonk1(b5['sentence1_binary_parse']))
            b8 = ' '.join(fonk1(b5['sentence2_binary_parse']))
            if b3 and b6 = = '-':
                continue
            yield (b6, b7, b8)
def fonk3(sentence_list):
    b9 = []
    for b10 in sentence_list:
        b10 = re.sub(r"[^a-zA-Z]", " ", b10)
        b11 = b10.lower().split()
        b11 = [b2.stem(w) for w in b11]
        b9.append(" ".join(b11))
    return b9
def fonk4(fn, b12 = None):
    b13 = list(fonk2(fn=fn, b12=b12))
    b14 = [b7 for _, b7, _ in b13]
    b15 = [b8 for _, _, b8 in b13]
    b16 = fonk3(b14)
    b17 = fonk3(b15)
    b18 = {'contradiction': 0, 'neutral': 1, 'entailment': 2}
    b19 = np.array([b18[b6] for b6, _, _ in b13])
    return b16, b17, b19
def fonk5():
    b20 = fonk4('snli_1.0/snli_1.0_train.jsonl')
    b21 = fonk4('snli_1.0/snli_1.0_test.jsonl')
    b22 = fonk4('snli_1.0/snli_1.0_dev.jsonl')
    savedata(b21, "test_stem")
    savedata(b20, "train_stem")
    savedata(b22, "dev_stem")
if b23 = = '__main__':
    fonk5()