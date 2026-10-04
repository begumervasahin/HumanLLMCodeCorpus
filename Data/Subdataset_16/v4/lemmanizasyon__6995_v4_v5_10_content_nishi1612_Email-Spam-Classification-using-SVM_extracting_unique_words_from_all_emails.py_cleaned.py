import os
import time
import string
import operator
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
def fonk1(text):
    b1 = ''.join(char for char in text if char not in string.punctuation)
    b2 = ' '.join(
        word for word in b1.split()
        if word.lower() not in stopwords.b12('english')
    )
    b3 = [word.lower() for word in b2.split()]
    return b3
def fonk2():
    b4 = time.time()
    b5 = WordNetLemmatizer()
    a1 = 0
    b6 = {}
    b7 = "emails/"
    b8 = os.fsencode(b7)
    for file in os.listdir(b8):
        b9 = file.decode("utf-8")
        b10 = os.path.join(b7, b9)
        with open(b10, "r", b11 = 'utf-8', errors='ignore') as file_reader:
            b12 = fonk1(file_reader.read())
            for word in b12:
                if not word.isdigit() and len(word) > 2:
                    b13 = b5.lemmatize(word)
                    b6[b13] = b6.get(b13, 0) + 1
            a1 += 1
            if a1 % b14 = = 0:
                print(f"Processed {a1} files")
    b15 = dict(sorted(b6.items(), key=operator.itemgetter(1), reverse=True))
    with open("wordslist.csv", "w", b16 = '', b11='utf-8') as csv_file:
        csv_file.write('word,count\n')
        for word, count in b15.items():
            if count < b14:
                break
            csv_file.write(f"{word},{count}\n")
    print(f'Time taken to preprocess emails: {round(time.time() - b4, 2)} seconds')
if b17 = = "__main__":
    fonk2()