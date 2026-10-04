import os
from os import listdir
from os.path import isfile, join
import csv
import string
from nltk.corpus import stopwords
def save(filename, dictionary):
    with open(filename, "w", newline='') as f:
        w = csv.writer(f)
        for key, val in dictionary.items():
            w.writerow([key, val])
def load(filename):
    d = {}
    with open(filename, mode='r') as infile:
        reader = csv.reader(infile)
        for rows in reader:
            if len(rows) == 2:
                d[rows[0]] = float(rows[1])
    return d
def cleaner(text):
    text = text.lower()
    translation_table = str.maketrans('', '', string.punctuation + '\0')
    stop_words = set(stopwords.words('english'))
    stop_words.add("subject")
    text = text.replace('\n', ' ')
    text = text.translate(translation_table)
    mail = text.split(' ')
    mail = [word for word in mail if word not in stop_words]
    return mail
def train(filename):
    files = [f for f in listdir(filename) if isfile(join(filename, f))]
    dictionary = {}
    counter = 0
    for file in files:
        with open(join(filename, file), errors="ignore") as f:
            text = f.read()
        mail = cleaner(text)
        for word in mail:
            counter += 1
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1
    file_count = len(files)
    for word in dictionary.keys():
        dictionary[word] = float(dictionary[word]) / file_count
    dictionary["fileCount"] = file_count
    return dictionary
def classify(input_text, diction, priori):
    input_text = cleaner(input_text)
    p = 1
    for word in input_text:
        if word in diction:
            p *= diction[word]
        else:
            p *= 1 / (diction["fileCount"] + len(diction) + 1)
    p *= priori
    return p
def train_n_save():
    save("spam_train_results.csv", train("spam"))
    save("ham_train_results.csv", train("ham"))
def test():
    ham_dict = load("ham_train_results.csv")
    spam_dict = load("spam_train_results.csv")
    files = [f for f in listdir("input") if isfile(join("input", f))]
    spam_count = ham_count = 0
    for file in files:
        with open(join("input", file), errors="ignore") as f:
            text = f.read()
        ham_prob = classify(text, ham_dict, 0.67)
        spam_prob = classify(text, spam_dict, 0.33)
        if ham_prob <= spam_prob:
            spam_count += 1
        else:
            ham_count += 1
    print("Spam:\t" + str(spam_count))
    print("Ham:\t" + str(ham_count))
if __name__ == "__main__":
    train_n_save()
    test()