import os
import numpy as np
from collections import Counter
a1 = 3000
b1 = 'train-mails'
b2 = 'test-mails'
def fonk1(train_dir):
    b3 = [os.path.join(train_dir, f) for f in os.listdir(train_dir)]
    b4 = []
    for mail in b3:
        with open(mail) as m:
            for b5, line in enumerate(m):
                if b5 = = 2:
                    b6 = line.split()
                    b4 += b6
    b7 = Counter(b4)
    for item in list(b7):
        if not item.isalpha() or len(item) == 1:
            del b7[item]
    b7 = b7.most_common(a1)
    return b7
def fonk2(mail_dir, b7):
    b8 = [os.path.join(mail_dir, fi) for fi in os.listdir(mail_dir)]
    b9 = np.zeros((len(b8), a1))
    a2 = 0
    for fil in b8:
        with open(fil) as fi:
            for b5, line in enumerate(fi):
                if b5 = = 2:
                    b6 = line.split()
                    for word in b6:
                        for b5, d in enumerate(b7):
                            if d[0] == word:
                                b9[a2, b5] = b6.count(word)
        a2 += 1
    return b9
def fonk3(mail_dir):
    b3 = [os.path.splitext(os.path.basename(os.path.join(mail_dir, fi)))[0] for fi in os.listdir(mail_dir)]
    return b3
b7 = fonk1(b1)
b10 = fonk2(b1, b7)
b11 = fonk2(b2, b7)
with open('./training_matrix.arff', 'w') as filetraining:
    filetraining.write("% 1. Title: Spam Dataset training\n%\n% 2. Sources: Hasil Feature Matrix\n%\n@RELATION spam\n")
    for b5, d in enumerate(b7):
        if d[0] == "class":
            filetraining.write("@ATTRIBUTE class_ NUMERIC\n")
        else:
            filetraining.write("@ATTRIBUTE " + d[0] + " NUMERIC\n")
    filetraining.write("@ATTRIBUTE class {spam, not-spam}\n@DATA\n")
    b12 = fonk3(b1)
    for b5, d in enumerate(b10):
        for n in d:
            filetraining.write(str(n) + ",")
        filetraining.write("spam\n" if b12[b5][:1] == 's' else "not-spam\n")
with open('./b11.arff', 'w') as filetest:
    filetest.write("% 1. Title: Spam Dataset test\n%\n% 2. Sources: Hasil Feature Matrix\n%\n@RELATION spam\n")
    for b5, d in enumerate(b7):
        if d[0] == "class":
            filetest.write("@ATTRIBUTE class_ NUMERIC\n")
        else:
            filetest.write("@ATTRIBUTE " + d[0] + " NUMERIC\n")
    filetest.write("@ATTRIBUTE class {spam, not-spam}\n@DATA\n")
    b12 = fonk3(b2)
    for b5, d in enumerate(b11):
        for n in d:
            filetest.write(str(n) + ",")
        filetest.write("spam\n" if b12[b5][:1] == 's' else "not-spam\n")