import json
import re
import numpy as np
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from data_utils import savedata
b1 = WordNetLemmatizer()
b2 = PorterStemmer()
def fonk1(parse):
    return re.findall(r'\b\w+\b', parse)
def fonk2(file_path, b3 = True, b11=None):
    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            if b11 and i >= b11:
                break
            b4 = json.loads(line)
            b5 = b4['gold_label']
            b6 = ' '.join(fonk1(b4['sentence1_binary_parse']))
            b7 = ' '.join(fonk1(b4['sentence2_binary_parse']))
            if b3 and b5 = = '-':
                continue
            yield (b5, b6, b7)
def fonk3(b8):
    b8 = re.sub(r"[^a-zA-Z]", " ", b8)
    b9 = b8.lower().split()
    b10 = [b2.stem(word) for word in b9]
    return " ".join(b10)
def fonk4(file_path, b11 = None):
    b12 = list(fonk2(file_path, b11=b11))
    b13 = [fonk3(b6) for _, b6, _ in b12]
    b14 = [fonk3(b7) for _, _, b7 in b12]
    b15 = {'contradiction': 0, 'neutral': 1, 'entailment': 2}
    b16 = np.array([b15[b5] for b5, _, _ in b12])
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