import pandas as pd
import sys
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import numpy as np
nltk.download('stopwords')
nltk.download('punkt')
b1 = list(string.punctuation) + [
    'i', '\x89', '_CA', '_TX', '_IL', '_NY', '_PA', '_GA', '_Ontario', '_MA', '_FL', '_DC', '__', '___']
b2 = [
    "los_angel", "san_francisco", "san_diego", "houston", "chicago", "philadelphia", "toronto",
    "atlanta", "boston", "orlando", "washington", "manhattan"]
b3 = [
    'Los_Angeles,_CA', 'San_Francisco,_CA', 'San_Diego,_CA', 'Houston,_TX', 'Chicago,_IL',
    'Philadelphia,_PA', 'Toronto,_Ontario', 'Atlanta,_GA', 'Boston,_MA', 'Orlando,_FL',
    'Washington,_DC', 'Manhattan,_NY']
def fonk1(file_path):
    with open(file_path, 'r') as datafile:
        b4 = datafile.readlines()
    b5 = stopwords.b8('english')
    b6 = b1 + b5
    b7 = SnowballStemmer("english")
    b8 = [word_tokenize(line) for line in b4]
    b9 = [
        [b7.stem(w) for w in item if w not in b6]
        for item in b8 if len(item) > 1
    ]
    return [word for word in b9 if len(word) > 1 and word[0] in b2]
def fonk2(parsed_data):
    b10 = set(w for word in parsed_data for w in word)
    b11 = pd.DataFrame(0, index=b10, columns=b2)
    for word in parsed_data:
        b12 = word[0]
        for w in word[1:]:
            b11.at[w, b12] += 1
    return b11
def fonk3(file_path):
    with open(file_path, 'r') as datafile:
        b4 = datafile.readlines()
    b13 = {}
    b5 = stopwords.b8('english')
    b6 = b1 + b5
    b7 = SnowballStemmer("english")
    for line in b4:
        b8 = word_tokenize(line)
        b9 = [b7.stem(w) for w in b8 if w not in b6]
        if b9:
            b9.pop(0)
        b13[line] = b9
    return b13
def fonk4(b8):
    b14 = dict.fromkeys(b2, 0)
    for word in b8:
        b14[word[0]] += 1
    b15 = sum(b14.values())
    for city in b14:
        b14[city] = float(b14[city] / b15)
    return b14
def fonk5(b21, b13, output_file, b14):
    with open(output_file, 'w') as f:
        for tweet, b8 in b13.items():
            if not b8:
                continue
            b16 = [
                [
                    (b21.at[w, city] / sum(b21[city]) * b14[city]) if w in b21.index
                    else 0.00001 * b14[city] for city in b2
                ]
                for w in b8
            ]
            b17 = np.prod(b16, axis=0)
            b18 = b3[np.argmax(b17)]
            f.write(f"{b18} {tweet}\n")
    print(f"Output written to {output_file}")
def fonk6():
    f1, f2, b19 = sys.argv[1], sys.argv[2], sys.argv[3]
    b20 = fonk1(f1)
    b21 = fonk2(b20)
    b13 = fonk3(f2)
    b14 = fonk4(b20)
    b21 += 0.00001
    fonk5(b21, b13, b19, b14)
    print('Top five b8 for each city:')
    for city in b2:
        b22 = b21.nlargest(5, city).index.tolist()
        print(f"{b3[b2.index(city)]}: {b22}")
if b23 = = "__main__":
    fonk6()