
from __future__ import print_function
import os
import numpy as np
from collections import Counter
np.set_printoptions(b1 = np.inf)
a1 = 3000
b2 = 'train-mails'
b3 = 'test-mails'
def fonk1(mail_dir):
    b4 = [os.path.join(mail_dir, f) for f in os.listdir(mail_dir)]
    b5 = []
    for mail in b4:
        with open(mail) as m:
            for b6, line in enumerate(m):
                if b6 = = 2:
                    b7 = line.split()
                    b5 += b7
    b8 = Counter(b5)
    b9 = list(b8.keys())
    for item in b9:
        if not item.isalpha() or len(item) == 1:
            del b8[item]
    b8 = b8.most_common(a1)
    return b8
def fonk2(mail_dir, b8):
    b10 = [os.path.join(mail_dir, fi) for fi in os.listdir(mail_dir)]
    b11 = np.zeros((len(b10), a1))
    for doc_id, fil in enumerate(b10):
        with open(fil) as fi:
            for b6, line in enumerate(fi):
                if b6 = = 2:
                    b7 = line.split()
                    for word in b7:
                        for word_id, d in enumerate(b8):
                            if d[0] == word:
                                b11[doc_id, word_id] = b7.count(word)
    return b11
def fonk3(mail_dir):
    b4 = [os.path.join(mail_dir, fi) for fi in os.listdir(mail_dir)]
    b12 = [os.path.splitext(os.path.basename(mail))[0] for mail in b4]
    return b12
def fonk4(file_path, relation, b8, matrix, b12):
    with open(file_path, 'w') as file:
        file.write(f"% 1. Title: Spam Dataset {relation}\n%\n% 2. Sources: Hasil Feature Matrix\n%\n@RELATION spam\n")
        for word, _ in b8:
            b13 = "class_" if word == "class" else word
            file.write(f"@ATTRIBUTE {b13} NUMERIC\n")
        file.write("@ATTRIBUTE class {spam, not-spam}\n")
        file.write("@DATA\n")
        for b6, features in enumerate(matrix):
            b14 = ",".join(map(str, features))
            b15 = "spam" if b12[b6].startswith('s') else "not-spam"
            file.write(f"{b14},{b15}\n")
b8 = fonk1(b2)
b16 = fonk2(b2, b8)
b17 = fonk2(b3, b8)
b18 = fonk3(b2)
b19 = fonk3(b3)
fonk4('./training_matrix.arff', 'training', b8, b16, b18)
fonk4('./b17.arff', 'test', b8, b17, b19)