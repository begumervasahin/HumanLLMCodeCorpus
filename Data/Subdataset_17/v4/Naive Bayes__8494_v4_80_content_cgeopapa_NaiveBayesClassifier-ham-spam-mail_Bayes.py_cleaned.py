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
    dictionary = {}
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
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
    words = text.split()
    cleaned_words = [word for word in words if word not in stop_words]
    return cleaned_words
def train(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    word_counts = {}
    total_words = 0
    for file in files:
        with open(os.path.join(directory, file), errors="ignore") as f:
            text = f.read()
        words = cleaner(text)
        for word in words:
            total_words += 1
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    num_files = len(files)
    for word in word_counts:
        word_counts[word] = float(word_counts[word]) / num_files
    word_counts["fileCount"] = num_files
    return word_counts
def classify(text, dictionary, prior):
    words = cleaner(text)
    probability = 1
    for word in words:
        if word in dictionary:
            probability *= dictionary[word]
        else:
            probability *= 1 / (dictionary["fileCount"] + len(dictionary) + 1)
    probability *= prior
    return probability
def train_and_save():
    save("spam_train_results.csv", train("spam"))
    save("ham_train_results.csv", train("ham"))
def test():
    ham_dict = load("ham_train_results.csv")
    spam_dict = load("spam_train_results.csv")
    files = [f for f in os.listdir("input") if os.path.isfile(os.path.join("input", f))]
    spam_count = 0
    ham_count = 0
    for file in files:
        with open(os.path.join("input", file), errors="ignore") as f:
            text = f.read()
        ham_probability = classify(text, ham_dict, 0.67)
        spam_probability = classify(text, spam_dict, 0.33)
        if ham_probability <= spam_probability:
            spam_count += 1
        else:
            ham_count += 1
    print("Spam:\t" + str(spam_count))
    print("Ham:\t" + str(ham_count))
if __name__ == "__main__":
    train_and_save()
    test()