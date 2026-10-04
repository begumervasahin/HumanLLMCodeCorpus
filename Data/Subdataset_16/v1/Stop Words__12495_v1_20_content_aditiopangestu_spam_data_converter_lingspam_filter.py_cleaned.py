import os
import numpy as np
from collections import Counter
a1 = 3000
b1 = 'train-mails'
b2 = 'test-mails'
def fonk1(mail_dir):
    b3 = [os.path.join(mail_dir, f) for f in os.listdir(mail_dir)]
    b4 = []
    for mail in b3:
        with open(mail) as m:
            for b5, line in enumerate(m):
                if b5 = = 2:
                    b6 = line.split()
                    b4 += b6
    b7 = Counter(b4)
    b8 = list(b7.keys())
    for item in b8:
        if not item.isalpha() or len(item) == 1:
            del b7[item]
    b7 = b7.most_common(a1)
    return b7
def fonk2(mail_dir, b7):
    b9 = [os.path.join(mail_dir, fi) for fi in os.listdir(mail_dir)]
    b10 = np.zeros((len(b9), a1))
    for docID, fil in enumerate(b9):
        with open(fil) as fi:
            for b5, line in enumerate(fi):
                if b5 = = 2:
                    b6 = line.split()
                    for word in b6:
                        for wordID, d in enumerate(b7):
                            if d[0] == word:
                                b10[docID, wordID] = b6.count(word)
    return b10
def fonk3(mail_dir):
    b3 = [os.path.join(mail_dir, fi) for fi in os.listdir(mail_dir)]
    for b5, mail in enumerate(b3):
        b3[b5] = os.path.splitext(os.path.basename(mail))[0]
    return b3
def fonk4(filename, matrix, b7, labels):
    with open(filename, 'w') as file:
        file.write("% 1. Title: Spam Dataset\n%\n% 2. Sources: Hasil Feature Matrix\n%\n@RELATION spam\n")
        for d in b7:
            if d[0] == "class":
                file.write("@ATTRIBUTE class_ NUMERIC\n")
            else:
                file.write(f"@ATTRIBUTE {d[0]} NUMERIC\n")
        file.write("@ATTRIBUTE class {spam, not-spam}\n@DATA\n")
        for b5, row in enumerate(matrix):
            b11 = ','.join(map(str, row))
            file.write(f"{b11},{labels[b5]}\n")
b7 = fonk1(b1)
b12 = fonk2(b1, b7)
b13 = ["spam" if fname.startswith('s') else "not-spam" for fname in fonk3(b1)]
fonk4('training_matrix.arff', b12, b7, b13)
b14 = fonk2(b2, b7)
b15 = ["spam" if fname.startswith('s') else "not-spam" for fname in fonk3(b2)]
fonk4('b14.arff', b14, b7, b15)