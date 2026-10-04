import os
import numpy as np
from collections import Counter
numberWordinDict = 3000
train_dir = 'train-mails'
test_dir = 'test-mails'
def make_dictionary(mail_dir):
    emails = [os.path.join(mail_dir, f) for f in os.listdir(mail_dir)]
    all_words = []
    for mail in emails:
        with open(mail) as m:
            for i, line in enumerate(m):
                if i == 2:
                    words = line.split()
                    all_words += words
    dictionary = Counter(all_words)
    list_to_remove = list(dictionary.keys())
    for item in list_to_remove:
        if not item.isalpha() or len(item) == 1:
            del dictionary[item]
    dictionary = dictionary.most_common(numberWordinDict)
    return dictionary
def extract_features(mail_dir, dictionary):
    files = [os.path.join(mail_dir, fi) for fi in os.listdir(mail_dir)]
    features_matrix = np.zeros((len(files), numberWordinDict))
    for docID, fil in enumerate(files):
        with open(fil) as fi:
            for i, line in enumerate(fi):
                if i == 2:
                    words = line.split()
                    for word in words:
                        for wordID, d in enumerate(dictionary):
                            if d[0] == word:
                                features_matrix[docID, wordID] = words.count(word)
    return features_matrix
def get_all_filenames(mail_dir):
    emails = [os.path.join(mail_dir, fi) for fi in os.listdir(mail_dir)]
    for i, mail in enumerate(emails):
        emails[i] = os.path.splitext(os.path.basename(mail))[0]
    return emails
def save_arff(filename, matrix, dictionary, labels):
    with open(filename, 'w') as file:
        file.write("% 1. Title: Spam Dataset\n%\n% 2. Sources: Hasil Feature Matrix\n%\n@RELATION spam\n")
        for d in dictionary:
            if d[0] == "class":
                file.write("@ATTRIBUTE class_ NUMERIC\n")
            else:
                file.write(f"@ATTRIBUTE {d[0]} NUMERIC\n")
        file.write("@ATTRIBUTE class {spam, not-spam}\n@DATA\n")
        for i, row in enumerate(matrix):
            row_str = ','.join(map(str, row))
            file.write(f"{row_str},{labels[i]}\n")
if __name__ == "__main__":
    dictionary = make_dictionary(train_dir)
    train_matrix = extract_features(train_dir, dictionary)
    train_labels = ["spam" if fname.startswith('s') else "not-spam" for fname in get_all_filenames(train_dir)]
    save_arff('training_matrix.arff', train_matrix, dictionary, train_labels)
    test_matrix = extract_features(test_dir, dictionary)
    test_labels = ["spam" if fname.startswith('s') else "not-spam" for fname in get_all_filenames(test_dir)]
    save_arff('test_matrix.arff', test_matrix, dictionary, test_labels)