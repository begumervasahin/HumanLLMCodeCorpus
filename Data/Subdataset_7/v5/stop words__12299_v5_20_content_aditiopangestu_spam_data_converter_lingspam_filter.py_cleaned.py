from collections import Counter
import os
import numpy as np
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
    b7 = {word: count for word, count in b7.items() if word.isalpha() and len(word) > 1}
    b7 = Counter(b7).most_common(a1)
    return b7
def fonk2(mail_dir, b7):
    b8 = [os.path.join(mail_dir, fi) for fi in os.listdir(mail_dir)]
    b9 = np.zeros((len(b8), a1))
    for docID, fil in enumerate(b8):
        with open(fil) as fi:
            for b5, line in enumerate(fi):
                if b5 = = 2:
                    b6 = line.split()
                    for word in b6:
                        a2 = 0
                        for b5, d in enumerate(b7):
                            if d[0] == word:
                                a2 = b5
                                b9[docID, a2] = b6.count(word)
        docID += 1
    return b9
def fonk3(mail_dir):
    b3 = [os.path.splitext(os.path.basename(os.path.join(mail_dir, fi)))[0] for fi in os.listdir(mail_dir)]
    return b3
b7 = fonk1(b1)
b10 = fonk2(b1, b7)
b11 = fonk2(b2, b7)
with open('./training_matrix.arff', 'a') as filetraining:
    filetraining.write("% 1. Title: Spam Dataset training\n%\n% 2. Sources: Hasil Feature Matrix\n%\n@RELATION spam\n")
    for b5, (word, _) in enumerate(b7):
        b12 = "@ATTRIBUTE class_" if word == "class" else f"@ATTRIBUTE {word}"
        filetraining.write(b12 + " NUMERIC\n")
    filetraining.write("@ATTRIBUTE class {spam, not-spam}\n@DATA\n")
    b13 = fonk3(b1)
    for b5, row in enumerate(b10):
        filetraining.write(",".join(map(str, row)) + (",spam\n" if b13[b5].startswith('s') else ",not-spam\n"))
with open('./b11.arff', 'a') as filetest:
    filetest.write("% 1. Title: Spam Dataset test\n%\n% 2. Sources: Hasil Feature Matrix\n%\n@RELATION spam\n")
    for b5, (word, _) in enumerate(b7):
        b12 = "@ATTRIBUTE class_" if word == "class" else f"@ATTRIBUTE {word}"
        filetest.write(b12 + " NUMERIC\n")
    filetest.write("@ATTRIBUTE class {spam, not-spam}\n@DATA\n")
    b13 = fonk3(b2)
    for b5, row in enumerate(b11):
        filetest.write(",".join(map(str, row)) + (",spam\n" if b13[b5].startswith('s') else ",not-spam\n"))