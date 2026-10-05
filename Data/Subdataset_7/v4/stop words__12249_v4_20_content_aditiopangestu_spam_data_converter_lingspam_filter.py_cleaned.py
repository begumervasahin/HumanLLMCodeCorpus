
from collections import Counter
import os
import numpy as np
a1 = 3000
b1 = 'train-mails'
b2 = 'test-mails'
def fonk1(b1):
    b3 = [os.path.join(b1, f) for f in os.listdir(b1)]
    b4 = []
    for mail in b3:
        with open(mail) as m:
            for b5, line in enumerate(m):
                if b5 = = 2:
                    b6 = line.split()
                    b4 += b6
    b7 = Counter(b4)
    b8 = b7.keys()
    for item in b8:
        if not item.isalpha() or len(item) == 1:
            del b7[item]
    b7 = b7.most_common(a1)
    return b7
def fonk2(mail_dir):
    b9 = [os.path.join(mail_dir, fi) for fi in os.listdir(mail_dir)]
    b10 = np.zeros((len(b9), a1))
    a2 = 0
    for fil in b9:
        with open(fil) as fi:
            for b5, line in enumerate(fi):
                if b5 = = 2:
                    b6 = line.split()
                    for word in b6:
                        a3 = 0
                        for b5, d in enumerate(b7):
                            if d[0] == word:
                                a3 = b5
                                b10[a2, a3] = b6.count(word)
        a2 += 1
    return b10
def fonk3(mail_dir):
    b3 = [os.path.join(mail_dir, fi) for fi in os.listdir(mail_dir)]
    for b5, mail in enumerate(b3):
        b3[b5] = os.path.splitext(os.path.basename(mail))[0]
    return b3
b7 = fonk1(b1)
b11 = fonk2(b1)
b12 = fonk2(b2)
with open('./training_matrix.arff', 'a') as filetraining:
    filetraining.write("% 1. Title: Spam Dataset training\n%\n% 2. Sources: Hasil Feature Matrix\n%\n@RELATION spam\n")
    for b5, d in enumerate(b7):
        if d[0] == "class":
            filetraining.write("@ATTRIBUTE class_ NUMERIC\n")
        else:
            filetraining.write("@ATTRIBUTE " + d[0] + " NUMERIC\n")
    filetraining.write("@ATTRIBUTE class {spam, not-spam}\n@DATA\n")
    b13 = fonk3(b1)
    for b5, d in enumerate(b11):
        for j, n in enumerate(d):
            filetraining.write(str(n) + ",")
        if b13[b5][:1] == 's':
            filetraining.write("spam\n")
        else:
            filetraining.write("not-spam\n")
with open('./b12.arff', 'a') as filetest:
    filetest.write("% 1. Title: Spam Dataset test\n%\n% 2. Sources: Hasil Feature Matrix\n%\n@RELATION spam\n")
    for b5, d in enumerate(b7):
        if d[0] == "class":
            filetest.write("@ATTRIBUTE class_ NUMERIC\n")
        else:
            filetest.write("@ATTRIBUTE " + d[0] + " NUMERIC\n")
    filetest.write("@ATTRIBUTE class {spam, not-spam}\n@DATA\n")
    b13 = fonk3(b2)
    for b5, d in enumerate(b12):
        for j, n in enumerate(d):
            filetest.write(str(n) + ",")
        if b13[b5][:1] == 's':
            filetest.write("spam\n")
        else:
            filetest.write("not-spam\n")