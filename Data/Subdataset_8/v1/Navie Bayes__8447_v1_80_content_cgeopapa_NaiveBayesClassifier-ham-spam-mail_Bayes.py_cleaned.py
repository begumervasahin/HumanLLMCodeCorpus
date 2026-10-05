import os
import csv
import string
from nltk.corpus import stopwords
def save(filename, dictionary):
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        for key, val in dictionary.items():
            writer.writerow([key, val])
def load(filename):
    d = {}
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:
                d[row[0]] = float(row[1])
    return d
def cleaner(text):
    text = text.lower()
    translation_table = dict.fromkeys(map(ord, string.punctuation + '\0'), None)
    stopWords = set(stopwords.words('english'))
    stopWords.add("subject")
    text = text.replace('\n', ' ')
    text = text.translate(translation_table)
    words = text.split(' ')
    words = [word for word in words if word not in stopWords]
    return words
def train(filename):
    files = [f for f in os.listdir(filename) if os.path.isfile(os.path.join(filename, f))]
    dictionary = {}
    counter = 0
    for file in files:
        with open(os.path.join(filename, file), errors="ignore") as f:
            text = f.read()
        mail = cleaner(text)
        for word in mail:
            counter += 1
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1
    fileCount = len(files)
    for word in dictionary.keys():
        dictionary[word] = float(dictionary[word]) / fileCount
    dictionary["fileCount"] = fileCount
    return dictionary
def classify(input_text, diction, priori):
    input_words = cleaner(input_text)
    p = 1
    for word in input_words:
        if word in diction:
            p *= diction[word]
        else:
            p *= 1 / (diction["fileCount"] + len(diction) + 1)
    p *= priori
    return p
def train_and_save():
    spam_results = train("spam")
    ham_results = train("ham")
    save("spam_train_results.csv", spam_results)
    save("ham_train_results.csv", ham_results)
def test():
    ham_dict = load("ham_train_results.csv")
    spam_dict = load("spam_train_results.csv")
    input_files = [f for f in os.listdir("input") if os.path.isfile(os.path.join("input", f))]
    spam_count = ham_count = 0
    for file in input_files:
        with open(os.path.join("input", file), errors="ignore") as f:
            text = f.read()
        ham_prob = classify(text, ham_dict, 0.67)
        spam_prob = classify(text, spam_dict, 0.33)
        if ham_prob <= spam_prob:
            spam_count += 1
        else:
            ham_count += 1
    print("Spam:\t" + str(ham_count))
    print("Ham:\t" + str(spam_count))
train_and_save()
test()