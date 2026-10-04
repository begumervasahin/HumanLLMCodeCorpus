import os
import csv
import string
from os import listdir
from os.path import isfile, join
from nltk.corpus import stopwords
def save(filename, dictionary):
    with open(filename, "w", newline='') as f:
        writer = csv.writer(f)
        for key, val in dictionary.items():
            writer.writerow([key, val])
def load(filename):
    dictionary = {}
    with open(filename, mode='r') as infile:
        reader = csv.reader(infile)
        for rows in reader:
            if len(rows) == 2:
                dictionary[rows[0]] = float(rows[1])
    return dictionary
def cleaner(text):
    text = text.lower()
    translation_table = str.maketrans('', '', string.punctuation + '\0')
    stop_words = set(stopwords.words('english'))
    stop_words.add("subject")
    text = text.replace('\n', ' ')
    text = text.translate(translation_table)
    words = text.split(' ')
    cleaned_words = [word for word in words if word not in stop_words]
    return cleaned_words
def train(directory):
    files = [f for f in listdir(directory) if isfile(join(directory, f))]
    dictionary = {}
    word_count = 0
    for file in files:
        with open(join(directory, file), errors="ignore") as f:
            text = f.read()
        words = cleaner(text)
        for word in words:
            word_count += 1
            dictionary[word] = dictionary.get(word, 0) + 1
    file_count = len(files)
    for word in dictionary:
        dictionary[word] = dictionary[word] / file_count
    dictionary["fileCount"] = file_count
    return dictionary
def classify(input_text, dictionary, prior):
    words = cleaner(input_text)
    probability = 1
    for word in words:
        if word in dictionary:
            probability *= dictionary[word]
        else:
            probability *= 1 / (dictionary["fileCount"] + len(dictionary) + 1)
    return probability * prior
def train_and_save():
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
    print("Spam:\t", spam_count)
    print("Ham:\t", ham_count)
if __name__ == "__main__":
    train_and_save()
    test()