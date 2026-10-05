import glob
import pickle
from multiprocessing import Process, Lock
from nltk.stem import WordNetLemmatizer
def compute_probability(vocabulary, ignore_folder=0):
    conditional_prob = [{key: 1 for key in vocabulary}, {key: 1 for key in vocabulary}]
    priori_prob = [0, 0]
    lemmatizer = WordNetLemmatizer()
    for i in range(1, 11):
        if i != ignore_folder:
            filenames = glob.glob(f"lingspam/part{i}/*.txt")
            for filename in filenames:
                label = int("spmsg" in filename)
                priori_prob[label] += 1
                with open(filename, "r", encoding="latin-1") as f:
                    text = f.read()
                    words = set(lemmatizer.lemmatize(word) for word in text.split())
                    for word in words:
                        if word in vocabulary:
                            conditional_prob[label][word] += 1
    total_docs = sum(priori_prob)
    priori_prob[0] /= total_docs
    priori_prob[1] /= total_docs
    for label in range(2):
        for word in vocabulary:
            conditional_prob[label][word] /= priori_prob[label]
    return conditional_prob, priori_prob
def classify(conditional_prob, priori_prob, filename):
    spam_prob, ham_prob = priori_prob
    lemmatizer = WordNetLemmatizer()
    with open(filename, "r", encoding="latin-1") as f:
        text = f.read()
        words = set(lemmatizer.lemmatize(word) for word in text.split())
        for word in words:
            if word in conditional_prob[0]:
                ham_prob *= conditional_prob[0][word]
            if word in conditional_prob[1]:
                spam_prob *= conditional_prob[1][word]
    return 1 if spam_prob > ham_prob else 0
def test(conditional_prob, priori_prob, folder):
    TP, FP, TN, FN = 0, 0, 0, 0
    for filename in glob.glob(f"lingspam/part{folder}/*.txt"):
        label = int("spmsg" in filename)
        label_ = classify(conditional_prob, priori_prob, filename)
        if label and label_:
            TP += 1
        elif label and not label_:
            FN += 1
        elif not label and not label_:
            TN += 1
        else:
            FP += 1
    return TP, FP, TN, FN
def validate(vocabulary, idx, lock):
    conditional_prob, priori_prob = compute_probability(vocabulary, idx)
    TP, FP, TN, FN = test(conditional_prob, priori_prob, idx)
    lock.acquire()
    print(f"{idx}, {TP}, {FP}, {TN}, {FN},")
    lock.release()
if __name__ == '__main__':
    for vocab_idx in range(1, 5):
        vocab_file = f"vocabulary{vocab_idx}.pickle"
        print(vocab_file)
        with open(vocab_file, "rb") as f:
            vocabulary = pickle.load(f)
        lock = Lock()
        process_list = [Process(target=validate, args=(vocabulary, i, lock)) for i in range(1, 11)]
        for process in process_list:
            process.start()
        for process in process_list:
            process.join()