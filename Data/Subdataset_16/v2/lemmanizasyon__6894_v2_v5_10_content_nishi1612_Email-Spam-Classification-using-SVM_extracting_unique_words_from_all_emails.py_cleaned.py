import os
import time
import string
import operator
import csv
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
def fonk1(text):
    b1 = ''.join(char for char in text if char not in string.punctuation)
    b2 = set(stopwords.b10('english'))
    b3 = ' '.join(word for word in b1.split() if word.lower() not in b2)
    b4 = WordNetLemmatizer()
    b5 = [b4.lemmatize(word.lower()) for word in b3.split()]
    return b5
def fonk2(directory_path):
    b6 = time.time()
    a1 = 0
    b7 = {}
    for file in os.listdir(directory_path):
        b8 = os.path.join(directory_path, file)
        with open(b8, "r", b9 = 'utf-8', errors='ignore') as file_reader:
            b10 = fonk1(file_reader.read())
            for word in b10:
                if not word.isdigit() and len(word) > 2:
                    b7[word] = b7.get(word, 0) + 1
            a1 += 1
            if a1 % b11 = = 0:
                print(f"Processed {a1} files")
    b12 = dict(sorted(b7.items(), key=operator.itemgetter(1), reverse=True))
    with open("wordslist.csv", "w", b13 = '') as csv_file:
        b14 = csv.b14(csv_file)
        b14.writerow(['word', 'count'])
        for word, count in b12.items():
            if count < b11:
                break
            b14.writerow([word, count])
    print(f'Time taken to preprocess emails: {round(time.time() - b6, 2)} seconds')
if b15 = = "__main__":
    fonk2("emails/")