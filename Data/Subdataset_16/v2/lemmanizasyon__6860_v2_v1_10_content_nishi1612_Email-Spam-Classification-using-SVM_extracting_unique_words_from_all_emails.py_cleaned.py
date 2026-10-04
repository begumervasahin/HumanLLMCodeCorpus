import os
import nltk
import time
import string
import operator
import csv
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
nltk.download('stopwords')
nltk.download('wordnet')
def fonk1(text):
    b1 = ''.join([c for c in text if c not in string.punctuation])
    b2 = ' '.join([word for word in b1.split()
                                       if word.lower() not in stopwords.b10('english')])
    b3 = [word.lower() for word in b2.split()]
    return b3
def fonk2():
    b4 = time.time()
    b5 = WordNetLemmatizer()
    b6 = {}
    a1 = 0
    b7 = "emails/"
    for file in os.listdir(b7):
        b8 = os.path.join(os.getcwd(), b7, file)
        with open(b8, "r", b9 = 'utf-8', errors='ignore') as f:
            b10 = fonk1(f.read())
            for word in b10:
                if not word.isdigit() and len(word) > 2:
                    b11 = b5.lemmatize(word)
                    b6[b11] = b6.get(b11, 0) + 1
        a1 += 1
        if a1 % b12 = = 0:
            print(f"Processed {a1} files")
    b13 = sorted(b6.items(), key=operator.itemgetter(1), reverse=True)
    with open("wordslist.csv", "w+", b14 = '') as csvfile:
        b15 = csv.b15(csvfile)
        b15.writerow(['word', 'count'])
        for word, count in b13:
            if count < b12:
                break
            b15.writerow([word, count])
    b16 = round(time.time() - b4, 2)
    print(f'Time (in seconds) to preprocess the emails: {b16}')
if b17 = = "__main__":
    fonk2()