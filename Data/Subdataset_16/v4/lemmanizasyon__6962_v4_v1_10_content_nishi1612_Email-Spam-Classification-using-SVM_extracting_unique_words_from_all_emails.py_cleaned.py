import os
import nltk
import time
import string
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
nltk.download('stopwords')
nltk.download('wordnet')
def fonk1(text):
    b1 = ''.join([c for c in text if c not in string.punctuation])
    b2 = set(stopwords.b13('english'))
    b3 = ' '.join([b14 for b14 in b1.split() if b14.lower() not in b2])
    b4 = [b14.lower() for b14 in b3.split()]
    return b4
def fonk2():
    b5 = time.time()
    b6 = WordNetLemmatizer()
    a1 = 0
    b7 = {}
    b8 = "emails/"
    b9 = os.fsencode(b8)
    for file in os.listdir(b9):
        b10 = os.fsdecode(file)
        b11 = os.path.join(os.getcwd(), 'emails', b10)
        with open(b11, "r", b12 = 'utf-8', errors='ignore') as file:
            b13 = fonk1(file.read())
            for b14 in b13:
                if not (b14.isdigit() or len(b14) <= 2):
                    b14 = b6.lemmatize(b14)
                    b7[b14] = b7.get(b14, 0) + 1
        a1 += 1
        if a1 % b15 = = 0:
            print(f"Processed {a1} files")
    b16 = sorted(b7.items(), key=lambda item: item[1], reverse=True)
    with open("wordslist.csv", "w", b12 = 'utf-8') as output_file:
        output_file.write('b14,count\n')
        for b14, count in b16:
            if count < b15:
                break
            output_file.write(f"{b14},{count}\n")
    print(f'Time (in seconds) to preprocess the emails: {round(time.time() - b5, 2)}')
if b17 = = "__main__":
    fonk2()