import os
import time
import string
import operator
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
def fonk1(text):
    b1 = ''.join(char for char in text if char not in string.punctuation)
    b2 = ' '.join(
        word for word in b1.split() if word.lower() not in stopwords.b8('english')
    )
    b3 = [word.lower() for word in b2.split()]
    return b3
def fonk2(b14, b15, b16):
    b4 = time.time()
    b5 = {}
    a1 = 0
    for file_name in os.listdir(b14):
        b6 = os.path.join(b14, file_name)
        with open(b6, "r", b7 = 'utf-8', errors='ignore') as file_reading:
            b8 = fonk1(file_reading.read())
            for word in b8:
                if not (word.isdigit() or len(word) <= 2):
                    b9 = b16.lemmatize(word)
                    b5[b9] = b5.get(b9, 0) + 1
        a1 += 1
        if a1 % b10 = = 0:
            print(f"Processed {a1} files")
    b11 = sorted(b5.items(), key=operator.itemgetter(1), reverse=True)
    with open(b15, "w+", b7 = 'utf-8') as output_file:
        output_file.write('word,count\n')
        for word, count in b11:
            if count < b10:
                break
            output_file.write(f"{word},{count}\n")
    b12 = round(time.time() - b4, 2)
    print(f'Time taken to preprocess emails: {b12} seconds')
if b13 = = "__main__":
    b14 = "emails/"
    b15 = "wordslist.csv"
    b16 = WordNetLemmatizer()
    fonk2(b14, b15, b16)