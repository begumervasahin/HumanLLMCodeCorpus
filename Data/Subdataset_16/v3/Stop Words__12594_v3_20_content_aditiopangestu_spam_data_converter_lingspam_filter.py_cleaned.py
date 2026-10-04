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
    b9 = b7.most_common(a1)
    return b9
def fonk2(mail_dir, b7):
    b10 = [os.path.join(mail_dir, fi) for fi in os.listdir(mail_dir)]
    b11 = np.zeros((len(b10), a1))
    for doc_id, file in enumerate(b10):
        with open(file) as f:
            for b5, line in enumerate(f):
                if b5 = = 2:
                    b6 = line.split()
                    for word in b6:
                        for word_id, (b12, _) in enumerate(b7):
                            if b12 = = word:
                                b11[doc_id, word_id] = b6.count(word)
    return b11
def fonk3(mail_dir):
    b3 = [os.path.splitext(os.path.basename(fi))[0] for fi in os.listdir(mail_dir)]
    return b3
def fonk4(filename, matrix, b7, labels):
    with open(filename, 'w') as file:
        file.write("% 1. Title: Spam Dataset\n%\n% 2. Sources: Hasil Feature Matrix\n%\n@RELATION spam\n")
        for word, _ in b7:
            b13 = "class_" if word == "class" else word
            file.write(f"@ATTRIBUTE {b13} NUMERIC\n")
        file.write("@ATTRIBUTE class {spam, not-spam}\n@DATA\n")
        for b5, row in enumerate(matrix):
            b14 = ','.join(map(str, row))
            file.write(f"{b14},{labels[b5]}\n")
def fonk5():
    b7 = fonk1(b1)
    b15 = fonk2(b1, b7)
    b16 = ["spam" if fname.startswith('s') else "not-spam" for fname in fonk3(b1)]
    fonk4('training_matrix.arff', b15, b7, b16)
    b17 = fonk2(b2, b7)
    b18 = ["spam" if fname.startswith('s') else "not-spam" for fname in fonk3(b2)]
    fonk4('b17.arff', b17, b7, b18)
if b19 = = "__main__":
    fonk5()