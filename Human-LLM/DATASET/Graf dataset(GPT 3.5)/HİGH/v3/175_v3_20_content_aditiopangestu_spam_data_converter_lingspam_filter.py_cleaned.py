import os
import numpy as np
from collections import Counter
a1 = 3000
b1 = 'train-mails'
b2 = 'test-mails'
def fonk1(train_dir):
    b3 = []
    for filename in os.listdir(train_dir):
        b4 = os.path.join(train_dir, filename)
        with open(b4) as file:
            for b5, line in enumerate(file):
                if b5 = = 2:
                    b6 = line.split()
                    b3.extend(b6)
    b7 = Counter(b3)
    for word in list(b7):
        if not word.isalpha() or len(word) == 1:
            del b7[word]
    b8 = b7.most_common(a1)
    return b8
def fonk2(mail_dir, b8):
    b9 = np.zeros((len(os.listdir(mail_dir)), a1))
    for doc_id, filename in enumerate(os.listdir(mail_dir)):
        b4 = os.path.join(mail_dir, filename)
        with open(b4) as file:
            for b5, line in enumerate(file):
                if b5 = = 2:
                    b6 = line.split()
                    for word in b6:
                        for idx, entry in enumerate(b8):
                            if entry[0] == word:
                                b9[doc_id, idx] = b6.count(word)
    return b9
def fonk3(mail_dir):
    b10 = [os.path.splitext(filename)[0] for filename in os.listdir(mail_dir)]
    return b10
b8 = fonk1(b1)
b11 = fonk2(b1, b8)
b12 = fonk2(b2, b8)
with open('./training_matrix.arff', 'w') as filetraining:
    filetraining.write("% 1. Title: Spam Dataset training\n%\n% 2. Sources: Hasil Feature Matrix\n%\n@RELATION spam\n")
    for idx, entry in enumerate(b8):
        b13 = "@ATTRIBUTE class_" if entry[0] == "class" else "@ATTRIBUTE " + entry[0]
        filetraining.write(b13 + " NUMERIC\n")
    filetraining.write("@ATTRIBUTE class {spam, not-spam}\n@DATA\n")
    b14 = fonk3(b1)
    for idx, row in enumerate(b11):
        for n in row:
            filetraining.write(str(n) + ",")
        filetraining.write("spam\n" if b14[idx][:1] == 's' else "not-spam\n")
with open('./b12.arff', 'w') as filetest:
    filetest.write("% 1. Title: Spam Dataset test\n%\n% 2. Sources: Hasil Feature Matrix\n%\n@RELATION spam\n")
    for idx, entry in enumerate(b8):
        b13 = "@ATTRIBUTE class_" if entry[0] == "class" else "@ATTRIBUTE " + entry[0]
        filetest.write(b13 + " NUMERIC\n")
    filetest.write("@ATTRIBUTE class {spam, not-spam}\n@DATA\n")
    b14 = fonk3(b2)
    for idx, row in enumerate(b12):
        for n in row:
            filetest.write(str(n) + ",")
        filetest.write("spam\n" if b14[idx][:1] == 's' else "not-spam\n")