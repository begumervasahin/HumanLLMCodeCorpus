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
            for filename in b5:
                b6 = {key: True for key in b17.keys()}
                b7 = int("spmsg" in filename)
                b3[b7] += 1
                with open(filename, "rb") as f:
                    b8 = f.readlines()
                    for line in b8:
                        for b9 in line.decode().split():
                            b9 = b4.lemmatize(b9)
                            if b9 in b17 and b6[b9]:
                                b2[b7][b9] += 1
                                b6[b9] = False
    for b7 in range(2):
        b2[b7] = {key: value / b3[b7] for key, value in b2[b7].items()}
    b10 = sum(b3)
    b3 = [count / b10 for count in b3]
    return b2, b3
def fonk2(b2, b3, filename):
    spam, b11 = 1, 1
    b12 = set(b2[0].keys())
    b4 = WordNetLemmatizer()
    with open(filename, "rb") as f:
        b8 = f.readlines()
        for line in b8:
            for b9 in line.decode().split():
                b9 = b4.lemmatize(b9)
                if b9 in b12:
                    b11 *= b2[0][b9]
                    spam *= b2[1][b9]
                    b12.remove(b9)
    for b9 in b12:
        b11 *= 1 - b2[0][b9]
        spam *= 1 - b2[1][b9]
    b11 *= b3[0]
    spam *= b3[1]
    return 1 if spam > b11 else 0
def fonk3(b2, b3, folder):
    b5 = glob.glob(f"lingspam/part{folder}/*.txt")
    TP, FP, TN, b13 = 0, 0, 0, 0
    for filename in b5:
        b7 = int("spmsg" in filename)
        b14 = fonk2(b2, b3, filename)
        if b7 = = 1 and b14 == 1:
            TP += 1
        elif b7 = = 1 and b14 == 0:
            b13 += 1
        elif b7 = = 0 and b14 == 0:
            TN += 1
        else:
            FP += 1
    return TP, FP, TN, b13
def fonk4(b17, partition_index, b18):
    b2, b3 = fonk1(b17, partition_index)
    TP, FP, TN, b13 = fonk3(b2, b3, partition_index)
    with b18:
        print(f"{partition_index} , {TP} , {FP} , {TN} , {b13} ,")
if b15 = = '__main__':
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