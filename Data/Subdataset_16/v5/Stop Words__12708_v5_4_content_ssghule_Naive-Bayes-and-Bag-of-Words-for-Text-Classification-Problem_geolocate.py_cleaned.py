import pandas as pd
import sys
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import numpy as np
import string
nltk.download('stopwords')
nltk.download('punkt')
b1 = [
    'Los_Angeles,_CA', 'San_Francisco,_CA', 'San_Diego,_CA', 'Houston,_TX',
    'Chicago,_IL', 'Philadelphia,_PA', 'Toronto,_Ontario', 'Atlanta,_GA',
    'Boston,_MA', 'Orlando,_FL', 'Washington,_DC', 'Manhattan,_NY'
]
b2 = [
    "los_angel", "san_francisco", "san_diego", "houston", "chicago",
    "philadelphia", "toronto", "atlanta", "boston", "orlando", "washington", "manhattan"
]
b3 = dict.fromkeys(b2, 0)
def fonk1(file_path):
    with open(file_path, 'r') as file:
        b4 = file.readlines()
    b5 = [word_tokenize(line) for line in b4]
    b6 = stopwords.b5('english')
    b7 = list(string.punctuation) + [
        'i', '\x89', '_CA', '_TX', '_IL', '_NY', '_PA', '_GA', '_Ontario',
        '_MA', '_FL', '_DC', '__', '___'
    ] + b6
    b8 = SnowballStemmer("english")
    b9 = [
        [b8.stem(w) for w in item if w not in b7]
        for item in b5 if len(item) > 1
    ]
    return [word for word in b9 if len(word) > 1 and word[0] in b2]
def fonk2(b20):
    b10 = set([w for word in b20 for w in word])
    b11 = pd.DataFrame(0, index=b10, columns=b2)
    for word in b20:
        b12 = word[0]
        for w in word[1:]:
            b11.at[w, b12] += 1
    return b11
def fonk3(file_path):
    with open(file_path, 'r') as file:
        b4 = file.readlines()
    b6 = stopwords.b5('english')
    b7 = list(string.punctuation) + [
        'i', '\x89', '_CA', '_TX', '_IL', '_NY', '_PA', '_GA', '_Ontario',
        '_MA', '_FL', '_DC', '__', '___'
    ] + b6
    b8 = SnowballStemmer("english")
    b13 = {}
    for line in b4:
        b5 = word_tokenize(line)
        b13[line] = [b8.stem(w) for w in b5 if w not in b7]
        if b13[line]:
            b13[line].pop(0)
    return b13
def fonk4(b5):
    for word in b5:
        b3[word[0]] += 1
    b14 = sum(b3.values())
    for city in b3:
        b3[city] = float(b3[city] / b14)
def fonk5(tdf, b13, b19):
    with open(b19, 'w') as file:
        for tweet in b13:
            b5 = b13[tweet]
            if not b5:
                continue
            b15 = [
                [
                    (tdf.at[w, city] / sum(tdf.loc[:, city]) * b3[city]) if w in tdf.index else 0.00001 * b3[city]
                    for city in b2
                ]
                for w in b5
            ]
            b16 = b15[0]
            for i in range(1, len(b15)):
                b16 = np.multiply(b16, b15[i])
            b17 = b1[b16.tolist().index(max(b16))]
            file.write(b17 + " " + tweet)
    print("Output written to", b19)
if b18 = = "__main__":
    training_file, test_file, b19 = sys.argv[1], sys.argv[2], sys.argv[3]
    b20 = fonk1(training_file)
    b21 = fonk2(b20)
    b13 = fonk3(test_file)
    fonk4(b20)
    b21 += 0.00001
    fonk5(b21, b13, b19)
    print('Top five b5 for each city:')
    for city in b2:
        print(b1[b2.index(city)], b21.nlargest(5, city).index.tolist())