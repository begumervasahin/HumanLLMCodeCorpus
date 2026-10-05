import glob
import pickle
from multiprocessing import Process, Lock
from nltk.stem import WordNetLemmatizer
def compute_probability(vocabulary, ignore=0):
    conditional_probability = [{key: 1 for key in vocabulary}, {key: 1 for key in vocabulary}]
    priori_probability = [0, 0]
    lemmatizer = WordNetLemmatizer()
    for i in range(1, 11):
        if i != ignore:
            filenames = glob.glob(f"lingspam/part{i}/*.txt")
            for filename in filenames:
                flag = {key: True for key in vocabulary}
                label = int("spmsg" in filename)
                priori_probability[label] += 1
                with open(filename, "rb") as f:
                    text = f.read().decode().split()
                    for word in text:
                        word = lemmatizer.lemmatize(word)
                        if word in vocabulary and flag[word]:
                            conditional_probability[label][word] += 1
                            flag[word] = False
    total = sum(priori_probability)
    priori_probability = [p / total for p in priori_probability]
    for i in range(2):
        conditional_probability[i] = {key: value / priori_probability[i] for key, value in conditional_probability[i].items()}
    return conditional_probability, priori_probability
def classify(conditional_probability, priori_probability, filename):
    spam_prob, ham_prob = 1, 1
    lemmatizer = WordNetLemmatizer()
    with open(filename, "rb") as f:
        text = f.read().decode().split()
        for word in text:
            word = lemmatizer.lemmatize(word)
            if word in vocabulary:
                ham_prob *= conditional_probability[0].get(word, 1)
                spam_prob *= conditional_probability[1].get(word, 1)
    ham_prob *= priori_probability[0]
    spam_prob *= priori_probability[1]
    return int(spam_prob > ham_prob)
def test(conditional_probability, priori_probability, folder):
    filenames = glob.glob(f"lingspam/part{folder}/*.txt")
    TP, FP, TN, FN = 0, 0, 0, 0
    for filename in filenames:
        label = int("spmsg" in filename)
        label_ = classify(conditional_probability, priori_probability, filename)
        if label and label_:
            TP += 1
        elif label and not label_:
            FN += 1
        elif not label and not label_:
            TN += 1
        else:
            FP += 1
    return TP, FP, TN, FN
def validate(vocabulary, i, lock):
    conditional_probability, priori_probability = compute_probability(vocabulary, i)
    TP, FP, TN, FN = test(conditional_probability, priori_probability, i)
    lock.acquire()
    print(f"{i}, {TP}, {FP}, {TN}, {FN},")
    lock.release()
if __name__ == '__main__':
    for v in range(1, 5):
        fname = f"vocabulary{v}.pickle"
        print(fname)
        with open(fname, "rb") as f:
            vocabulary = pickle.load(f)
        lock = Lock()
        process_list = [Process(target=validate, args=(vocabulary, i, lock)) for i in range(1, 11)]
        for process in process_list:
            process.start()
        for process in process_list:
            process.join()