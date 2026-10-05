import os
import numpy as np
from collections import Counter
number_of_words_in_dict = 3000
train_directory = 'train-mails'
test_directory = 'test-mails'
def make_dictionary(train_dir):
    emails = [os.path.join(train_dir, f) for f in os.listdir(train_dir)]
    all_words = []
    for mail in emails:
        with open(mail) as m:
            for i, line in enumerate(m):
                if i == 2:
                    words = line.split()
                    all_words += words
    dictionary = Counter(all_words)
    for item in list(dictionary):
        if not item.isalpha() or len(item) == 1:
            del dictionary[item]
    dictionary = dictionary.most_common(number_of_words_in_dict)
    return dictionary
def extract_features(mail_dir, dictionary):
    files = [os.path.join(mail_dir, fi) for fi in os.listdir(mail_dir)]
    features_matrix = np.zeros((len(files), number_of_words_in_dict))
    docID = 0
    for fil in files:
        with open(fil) as fi:
            for i, line in enumerate(fi):
                if i == 2:
                    words = line.split()
                    for word in words:
                        for i, d in enumerate(dictionary):
                            if d[0] == word:
                                features_matrix[docID, i] = words.count(word)
        docID += 1
    return features_matrix
def get_all_filenames(mail_dir):
    emails = [os.path.splitext(os.path.basename(os.path.join(mail_dir, fi)))[0] for fi in os.listdir(mail_dir)]
    return emails
dictionary = make_dictionary(train_directory)
train_matrix = extract_features(train_directory, dictionary)
test_matrix = extract_features(test_directory, dictionary)
with open('./training_matrix.arff', 'w') as filetraining:
    filetraining.write("% 1. Title: Spam Dataset training\n%\n% 2. Sources: Hasil Feature Matrix\n%\n@RELATION spam\n")
    for i, d in enumerate(dictionary):
        if d[0] == "class":
            filetraining.write("@ATTRIBUTE class_ NUMERIC\n")
        else:
            filetraining.write("@ATTRIBUTE " + d[0] + " NUMERIC\n")
    filetraining.write("@ATTRIBUTE class {spam, not-spam}\n@DATA\n")
    filename_list = get_all_filenames(train_directory)
    for i, d in enumerate(train_matrix):
        for n in d:
            filetraining.write(str(n) + ",")
        filetraining.write("spam\n" if filename_list[i][:1] == 's' else "not-spam\n")
with open('./test_matrix.arff', 'w') as filetest:
    filetest.write("% 1. Title: Spam Dataset test\n%\n% 2. Sources: Hasil Feature Matrix\n%\n@RELATION spam\n")
    for i, d in enumerate(dictionary):
        if d[0] == "class":
            filetest.write("@ATTRIBUTE class_ NUMERIC\n")
        else:
            filetest.write("@ATTRIBUTE " + d[0] + " NUMERIC\n")
    filetest.write("@ATTRIBUTE class {spam, not-spam}\n@DATA\n")
    filename_list = get_all_filenames(test_directory)
    for i, d in enumerate(test_matrix):
        for n in d:
            filetest.write(str(n) + ",")
        filetest.write("spam\n" if filename_list[i][:1] == 's' else "not-spam\n")