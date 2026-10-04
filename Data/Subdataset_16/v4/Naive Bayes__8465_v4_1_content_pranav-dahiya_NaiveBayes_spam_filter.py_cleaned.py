
import glob
import pickle
import numpy as np
from multiprocessing import Process, Lock
from nltk.stem import WordNetLemmatizer
def fonk1(b17, b1 = 0):
    b2 = [{key: 1 for key in b17.keys()}, {key: 1 for key in b17.keys()}]
    b3 = [0, 0]
    b4 = WordNetLemmatizer()
    for i in range(1, 11):
        if i != b1:
            b5 = glob.glob(f"lingspam/part{i}/*.txt")
            for b16 in b5:
                b6 = {key: True for key in b17.keys()}
                b7 = int("spmsg" in b16)
                b3[b7] += 1
                with open(b16, "rb") as f:
                    b8 = f.readlines()
                    for line in b8:
                        for b9 in line.decode().split():
                            b9 = b4.lemmatize(b9)
                            if b9 in b17 and b6[b9]:
                                b2[b7][b9] += 1
                                b6[b9] = False
    for b7 in [0, 1]:
        b10 = b3[b7]
        b2[b7] = {key: value / b10 for key, value in b2[b7].items()}
    b11 = sum(b3)
    b3 = [count / b11 for count in b3]
    return b2, b3
def fonk2(b2, b3, b16):
    spam_prob, b12 = 1, 1
    b13 = list(b2[0].keys())
    b4 = WordNetLemmatizer()
    with open(b16, "rb") as f:
        b8 = f.readlines()
        for line in b8:
            for b9 in line.decode().split():
                b9 = b4.lemmatize(b9)
                if b9 in b13:
                    b12 *= b2[0][b9]
                    spam_prob *= b2[1][b9]
                    b13.remove(b9)
    for b9 in b13:
        b12 *= (1 - b2[0][b9])
        spam_prob *= (1 - b2[1][b9])
    b12 *= b3[0]
    spam_prob *= b3[1]
    return int(spam_prob > b12)
def fonk3(b2, b3, folder):
    b5 = glob.glob(f"lingspam/part{folder}/*.txt")
    TP, FP, TN, b14 = 0, 0, 0, 0
    for b16 in b5:
        b7 = int("spmsg" in b16)
        b15 = fonk2(b2, b3, b16)
        if b7 and b15:
            TP += 1
        elif b7 and not b15:
            b14 += 1
        elif not b7 and not b15:
            TN += 1
        else:
            FP += 1
    return TP, FP, TN, b14
def fonk4(b17, part, b18):
    b2, b3 = fonk1(b17, part)
    TP, FP, TN, b14 = fonk3(b2, b3, part)
    with b18:
        print(f"{part}, {TP}, {FP}, {TN}, {b14},")
def fonk5():
    for v in range(1, 5):
        b16 = f"b17{v}.pickle"
        print(b16)
        with open(b16, "rb") as f:
            b17 = pickle.load(f)
        b18 = Lock()
        b19 = [Process(target=validate, args=(b17, i, b18)) for i in range(1, 11)]
        for process in b19:
            process.start()
        for process in b19:
            process.join()
if b20 = = '__main__':
    fonk5()