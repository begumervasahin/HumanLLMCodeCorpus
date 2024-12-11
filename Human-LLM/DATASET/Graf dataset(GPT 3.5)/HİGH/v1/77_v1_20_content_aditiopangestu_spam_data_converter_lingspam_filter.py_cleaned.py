from __future__ import print_function
import os
import numpy as np
np.set_printoptions(b1 = np.nan)
from collections import Counter
a1 = 3000
b2 = 'train-mails'
b3 = 'test-mails'
def fonk1(b2):
    b4 = [os.path.join(b2,f) for f in os.listdir(b2)]
    b5 = []
    for mail in b4:
        with open(mail) as m:
            for b6,line in enumerate(m):
                if b6 = = 2:
                    b7 = line.split()
                    b5 += b7
    b8 = Counter(b5)
    b9 = b8.keys()
    for item in b9:
        if not item.isalpha() or len(item) == 1:
            del b8[item]
    b8 = b8.most_common(a1)
    return b8
def fonk2(mail_dir, b8):
    b10 = [os.path.join(mail_dir,fi) for fi in os.listdir(mail_dir)]
    b11 = np.zeros((len(b10), a1))
    a2 = 0
    for fil in b10:
        with open(fil) as fi:
            for b6,line in enumerate(fi):
                if b6 = = 2:
                    b7 = line.split()
                    for word in b7:
                        for b6,d in enumerate(b8):
                            if d[0] == word:
                                b11[a2,b6] = b7.count(word)
        a2 += 1
    return b11
def fonk3(mail_dir):
    b4 = [os.path.join(mail_dir,fi) for fi in os.listdir(mail_dir)]
    for b6,mail in enumerate(b4):
        b4[b6] = os.path.splitext(os.path.basename(mail))[0]
    return b4
b8 = fonk1(b2)
b12 = fonk2(b2, b8)
b13 = fonk2(b3, b8)
with open('./training_matrix.arff', 'w') as filetraining:
    print("% 1. Title: Spam Dataset training\n%\n% 2. Sources: Hasil Feature Matrix\n%\n@RELATION spam", b14 = "\n", file=filetraining)
    for b6,d in enumerate(b8):
        if d[0] == "class":
            print("@ATTRIBUTE class_ NUMERIC", b14 = "\n", file=filetraining)
        else:
            print("@ATTRIBUTE "+d[0]+" NUMERIC", b14 = "\n", file=filetraining)
    print("@ATTRIBUTE class {spam, not-spam}", b14 = "\n", file=filetraining)
    b15 = fonk3(b2)
    print("@DATA", b14 = "\n", file=filetraining)
    for b6, d in enumerate(b12):
        for j, n in enumerate(d):
            print(str(n)+",", b14 = "", file=filetraining)
        if b15[b6][:1] == 's':
            print("spam", b14 = "\n", file=filetraining)
        else:
            print("not-spam", b14 = "\n", file=filetraining)
with open('./b13.arff', 'w') as filetest:
    print("% 1. Title: Spam Dataset test\n%\n% 2. Sources: Hasil Feature Matrix\n%\n@RELATION spam", b14 = "\n", file=filetest)
    for b6,d in enumerate(b8):
        if d[0] == "class":
            print("@ATTRIBUTE class_ NUMERIC", b14 = "\n", file=filetest)
        else:
            print("@ATTRIBUTE "+d[0]+" NUMERIC", b14 = "\n", file=filetest)
    print("@ATTRIBUTE class {spam, not-spam}", b14 = "\n", file=filetest)
    b15 = fonk3(b3)
    print("@DATA", b14 = "\n", file=filetest)
    for b6, d in enumerate(b13):
        for j, n in enumerate(d):
            print(str(n)+",", b14 = "", file=filetest)
        if b15[b6][:1] == 's':
            print("spam", b14 = "\n", file=filetest)
        else:
            print("not-spam", b14 = "\n", file=filetest)