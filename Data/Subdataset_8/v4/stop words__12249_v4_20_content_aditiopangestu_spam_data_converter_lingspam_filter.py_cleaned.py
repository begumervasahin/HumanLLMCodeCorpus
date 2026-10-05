
from collections import Counter
import os
import numpy as np
numberWordinDict = 3000
train_dir = 'train-mails'
test_dir = 'test-mails'
def make_Dictionary(train_dir):
    emails = [os.path.join(train_dir, f) for f in os.listdir(train_dir)]
    all_words = []
    for mail in emails:
        with open(mail) as m:
            for i, line in enumerate(m):
                if i == 2:
                    words = line.split()
                    all_words += words
    dictionary = Counter(all_words)
    list_to_remove = dictionary.keys()
    for item in list_to_remove:
        if not item.isalpha() or len(item) == 1:
            del dictionary[item]
    dictionary = dictionary.most_common(numberWordinDict)
    return dictionary
def extract_features(mail_dir):
    files = [os.path.join(mail_dir, fi) for fi in os.listdir(mail_dir)]
    features_matrix = np.zeros((len(files), numberWordinDict))
    docID = 0
    for fil in files:
        with open(fil) as fi:
            for i, line in enumerate(fi):
                if i == 2:
                    words = line.split()
                    for word in words:
                        wordID = 0
                        for i, d in enumerate(dictionary):
                            if d[0] == word:
                                wordID = i
                                features_matrix[docID, wordID] = words.count(word)
        docID += 1
    return features_matrix
def getAllFilename(mail_dir):
    emails = [os.path.join(mail_dir, fi) for fi in os.listdir(mail_dir)]
    for i, mail in enumerate(emails):
        emails[i] = os.path.splitext(os.path.basename(mail))[0]
    return emails
dictionary = make_Dictionary(train_dir)
train_matrix = extract_features(train_dir)
test_matrix = extract_features(test_dir)
with open('./training_matrix.arff', 'a') as filetraining:
    filetraining.write("% 1. Title: Spam Dataset training\n%\n% 2. Sources: Hasil Feature Matrix\n%\n@RELATION spam\n")
    for i, d in enumerate(dictionary):
        if d[0] == "class":
            filetraining.write("@ATTRIBUTE class_ NUMERIC\n")
        else:
            filetraining.write("@ATTRIBUTE " + d[0] + " NUMERIC\n")
    filetraining.write("@ATTRIBUTE class {spam, not-spam}\n@DATA\n")
    filename_list = getAllFilename(train_dir)
    for i, d in enumerate(train_matrix):
        for j, n in enumerate(d):
            filetraining.write(str(n) + ",")
        if filename_list[i][:1] == 's':
            filetraining.write("spam\n")
        else:
            filetraining.write("not-spam\n")
with open('./test_matrix.arff', 'a') as filetest:
    filetest.write("% 1. Title: Spam Dataset test\n%\n% 2. Sources: Hasil Feature Matrix\n%\n@RELATION spam\n")
    for i, d in enumerate(dictionary):
        if d[0] == "class":
            filetest.write("@ATTRIBUTE class_ NUMERIC\n")
        else:
            filetest.write("@ATTRIBUTE " + d[0] + " NUMERIC\n")
    filetest.write("@ATTRIBUTE class {spam, not-spam}\n@DATA\n")
    filename_list = getAllFilename(test_dir)
    for i, d in enumerate(test_matrix):
        for j, n in enumerate(d):
            filetest.write(str(n) + ",")
        if filename_list[i][:1] == 's':
            filetest.write("spam\n")
        else:
            filetest.write("not-spam\n")