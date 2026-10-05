import glob
import pickle
from multiprocessing import Process, Lock
from nltk.stem import WordNetLemmatizer
def fonk1(b16, b1 = 0):
    b2 = [{key: 1 for key in b16}, {key: 1 for key in b16}]
    b3 = [0, 0]
    b4 = WordNetLemmatizer()
    for i in range(1, 11):
        if i != b1:
            b5 = glob.glob(f"lingspam/part{i}/*.txt")
            for filename in b5:
                b6 = {key: True for key in b16}
                b7 = int("spmsg" in filename)
                b3[b7] += 1
                with open(filename, "rb") as f:
                    b8 = f.read().decode().split()
                    for b9 in b8:
                        b9 = b4.lemmatize(b9)
                        if b9 in b16 and b6[b9]:
                            b2[b7][b9] += 1
                            b6[b9] = False
    b10 = sum(b3)
    b3 = [p / b10 for p in b3]
    for i in range(2):
        b2[i] = {key: value / b3[i] for key, value in b2[i].items()}
    return b2, b3
def fonk2(b2, b3, filename):
    spam_prob, b11 = 1, 1
    b4 = WordNetLemmatizer()
    with open(filename, "rb") as f:
        b8 = f.read().decode().split()
        for b9 in b8:
            b9 = b4.lemmatize(b9)
            if b9 in b16:
                b11 *= b2[0].get(b9, 1)
                spam_prob *= b2[1].get(b9, 1)
    b11 *= b3[0]
    spam_prob *= b3[1]
    return int(spam_prob > b11)
def fonk3(b2, b3, folder):
    b5 = glob.glob(f"lingspam/part{folder}/*.txt")
    TP, FP, TN, b12 = 0, 0, 0, 0
    for filename in b5:
        b7 = int("spmsg" in filename)
        b13 = fonk2(b2, b3, filename)
        if b7 and b13:
            TP += 1
        elif b7 and not b13:
            b12 += 1
        elif not b7 and not b13:
            TN += 1
        else:
            FP += 1
    return TP, FP, TN, b12
def fonk4(b16, i, b17):
    b2, b3 = fonk1(b16, i)
    TP, FP, TN, b12 = fonk3(b2, b3, i)
    b17.acquire()
    print(f"{i}, {TP}, {FP}, {TN}, {b12},")
    b17.release()
if b14 = = '__main__':
    for v in range(1, 5):
        b15 = f"b16{v}.pickle"
        print(b15)
        with open(b15, "rb") as f:
            b16 = pickle.load(f)
        b17 = Lock()
        b18 = [Process(target=validate, args=(b16, i, b17)) for i in range(1, 11)]
        for process in b18:
            process.start()
        for process in b18:
            process.join()