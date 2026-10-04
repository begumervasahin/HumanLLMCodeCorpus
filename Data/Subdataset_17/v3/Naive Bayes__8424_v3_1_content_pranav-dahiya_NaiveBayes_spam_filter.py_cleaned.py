import glob
import pickle
import numpy as np
from multiprocessing import Process, Lock
from nltk.stem import WordNetLemmatizer
def compute_probability(vocabulary, ignore=0):
    conditional_prob = [{key: 1 for key in vocabulary.keys()}, {key: 1 for key in vocabulary.keys()}]
    priori_prob = [0, 0]
    lemmatizer = WordNetLemmatizer()
    for i in range(1, 11):
        if i != ignore:
            filenames = glob.glob(f"lingspam/part{i}/*.txt")
            for filename in filenames:
                flag = {key: True for key in vocabulary.keys()}
                label = int("spmsg" in filename)
                priori_prob[label] += 1
                with open(filename, "rb") as f:
                    text = f.readlines()
                    for line in text:
                        for word in line.decode().split():
                            word = lemmatizer.lemmatize(word)
                            if word in vocabulary and flag[word]:
                                conditional_prob[label][word] += 1
                                flag[word] = False
    for label in range(2):
        conditional_prob[label] = {key: value / priori_prob[label] for key, value in conditional_prob[label].items()}
    total = sum(priori_prob)
    priori_prob = [count / total for count in priori_prob]
    return conditional_prob, priori_prob
def classify(conditional_prob, priori_prob, filename):
    spam_prob, ham_prob = 1, 1
    words = set(conditional_prob[0].keys())
    lemmatizer = WordNetLemmatizer()
    with open(filename, "rb") as f:
        text = f.readlines()
        for line in text:
            for word in line.decode().split():
                word = lemmatizer.lemmatize(word)
                if word in words:
                    ham_prob *= conditional_prob[0][word]
                    spam_prob *= conditional_prob[1][word]
                    words.remove(word)
    for word in words:
        ham_prob *= 1 - conditional_prob[0][word]
        spam_prob *= 1 - conditional_prob[1][word]
    ham_prob *= priori_prob[0]
    spam_prob *= priori_prob[1]
    return 1 if spam_prob > ham_prob else 0
def test(conditional_prob, priori_prob, folder):
    filenames = glob.glob(f"lingspam/part{folder}/*.txt")
    TP, FP, TN, FN = 0, 0, 0, 0
    for filename in filenames:
        label = int("spmsg" in filename)
        predicted_label = classify(conditional_prob, priori_prob, filename)
        if label == 1 and predicted_label == 1:
            TP += 1
        elif label == 1 and predicted_label == 0:
            FN += 1
        elif label == 0 and predicted_label == 0:
            TN += 1
        else:
            FP += 1
    return TP, FP, TN, FN
def validate(vocabulary, partition_index, lock):
    conditional_prob, priori_prob = compute_probability(vocabulary, partition_index)
    TP, FP, TN, FN = test(conditional_prob, priori_prob, partition_index)
    with lock:
        print(f"Partition {partition_index}: TP={TP}, FP={FP}, TN={TN}, FN={FN}")
if __name__ == '__main__':
    for v in range(1, 5):
        vocabulary_file = f"vocabulary{v}.pickle"
        print(f"Using vocabulary file: {vocabulary_file}")
        with open(vocabulary_file, "rb") as f:
            vocabulary = pickle.load(f)
        lock = Lock()
        processes = [Process(target=validate, args=(vocabulary, i, lock)) for i in range(1, 11)]
        for process in processes:
            process.start()
        for process in processes:
            process.join()