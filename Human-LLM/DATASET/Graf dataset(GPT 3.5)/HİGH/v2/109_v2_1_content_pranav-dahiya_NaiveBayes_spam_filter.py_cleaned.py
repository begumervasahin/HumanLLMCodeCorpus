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
                b6 = int("spmsg" in filename)
                b3[b6] += 1
                with open(filename, "r", b7 = "latin-1") as f:
                    b8 = f.read()
                    b9 = set(b4.lemmatize(word) for word in b8.split())
                    for word in b9:
                        if word in b16:
                            b2[b6][word] += 1
    b10 = sum(b3)
    b3[0] /= b10
    b3[1] /= b10
    for b6 in range(2):
        for word in b16:
            b2[b6][word] /= b3[b6]
    return b2, b3
def fonk2(b2, b3, filename):
    spam_probability, b11 = b3
    b4 = WordNetLemmatizer()
    with open(filename, "r", b7 = "latin-1") as f:
        b8 = f.read()
        b9 = set(b4.lemmatize(word) for word in b8.split())
        for word in b9:
            if word in b2[0]:
                b11 *= b2[0][word]
            if word in b2[1]:
                spam_probability *= b2[1][word]
    if spam_probability > b11:
        return 1
    else:
        return 0
def fonk3(b2, b3, folder):
    TP, FP, TN, b12 = 0, 0, 0, 0
    for filename in glob.glob(f"lingspam/part{folder}/*.txt"):
        b6 = int("spmsg" in filename)
        b13 = fonk2(b2, b3, filename)
        if b6 and b13:
            TP += 1
        elif b6 and not b13:
            b12 += 1
        elif not b6 and not b13:
            TN += 1
        else:
            FP += 1
    return TP, FP, TN, b12
def fonk4(b16, idx, b17):
    b2, b3 = fonk1(b16, idx)
    TP, FP, TN, b12 = fonk3(b2, b3, idx)
    b17.acquire()
    print(f"{idx}, {TP}, {FP}, {TN}, {b12},")
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