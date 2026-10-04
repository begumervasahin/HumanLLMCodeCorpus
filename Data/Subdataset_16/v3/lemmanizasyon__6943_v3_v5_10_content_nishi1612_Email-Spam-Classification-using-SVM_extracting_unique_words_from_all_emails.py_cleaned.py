import os
import time
import string
import operator
import csv
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
def fonk1(b1):
    b1 = ''.join(char for char in b1 if char not in string.punctuation)
    b2 = set(stopwords.b9('english'))
    b1 = ' '.join(word for word in b1.split() if word.lower() not in b2)
    b3 = WordNetLemmatizer()
    b4 = [b3.lemmatize(word.lower()) for word in b1.split()]
    return b4
def fonk2(b16):
    b5 = time.time()
    a1 = 0
    b6 = {}
    for filename in os.listdir(b16):
        b7 = os.path.join(b16, filename)
        with open(b7, "r", b8 = 'utf-8', errors='ignore') as file:
            b9 = fonk1(file.read())
            for word in b9:
                if not word.isdigit() and len(word) > 2:
                    b6[word] = b6.get(word, 0) + 1
            a1 += 1
            if a1 % b10 = = 0:
                print(f"Processed {a1} files")
    b11 = dict(sorted(b6.items(), key=operator.itemgetter(1), reverse=True))
    with open("wordslist.csv", "w", b12 = '') as csv_file:
        b13 = csv.b13(csv_file)
        b13.writerow(['word', 'count'])
        for word, count in b11.items():
            if count < b10:
                break
            b13.writerow([word, count])
    b14 = round(time.time() - b5, 2)
    print(f'Time taken to preprocess emails: {b14} seconds')
if b15 = = "__main__":
    b16 = "emails/"
    fonk2(b16)