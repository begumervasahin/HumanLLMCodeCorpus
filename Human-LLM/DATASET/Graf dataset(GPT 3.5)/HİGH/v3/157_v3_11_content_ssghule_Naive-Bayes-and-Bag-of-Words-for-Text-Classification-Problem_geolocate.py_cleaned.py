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
def fonk1(file_path):
    with open(file_path, 'r') as file:
        b1 = file.readlines()
    b2 = stopwords.b5('english')
    b3 = list(string.punctuation) + ['i', '\x89', '_CA', '_TX', '_IL', '_NY', '_PA', '_GA', '_Ontario',
                                                   '_MA', '_FL', '_DC', '__', '___'] + b2
    b4 = SnowballStemmer("english")
    b5 = [
        [b4.stem(word) for word in word_tokenize(line) if word not in b3]
        for line in b1 if len(word_tokenize(line)) > 1
    ]
    return [word for word in b5 if len(word) > 1 and word[0] in b18]
def fonk2(b20):
    b6 = set([word for item in b20 for word in item])
    b7 = pd.DataFrame(0, index=b6, columns=b18)
    for item in b20:
        b8 = item[0]
        for word in item[1:]:
            b7.at[word, b8] += 1
    return b7
def fonk3(file_path):
    with open(file_path, 'r') as file:
        b1 = file.readlines()
    b2 = stopwords.b5('english')
    b3 = list(string.punctuation) + ['i', '\x89', '_CA', '_TX', '_IL', '_NY', '_PA', '_GA', '_Ontario',
                                                   '_MA', '_FL', '_DC', '__', '___'] + b2
    b4 = SnowballStemmer("english")
    b9 = {}
    for line in b1:
        b5 = [b4.stem(word) for word in word_tokenize(line) if word not in b3]
        if b5:
            b5.pop(0)
            b9[line] = b5
    return b9
def fonk4(b20):
    for item in b20:
        b19[item[0]] += 1
    b10 = sum(b19.values())
    for city_name in b19:
        b19[city_name] = float(b19[city_name] / b10)
def fonk5(b21, b22, output_file):
    with open(output_file, 'w') as file:
        for tweet, b5 in b22.items():
            if not b5:
                continue
            b11 = [
                [
                    (b21.at[word, b18[i]] / sum(b21.loc[:, b18[i]]) * b19[b18[i]])
                    if word in b21.index else 0.00001 * b19[b18[i]]
                    for i in range(12)
                ] for word in b5
            ]
            b12 = np.prod(b11, axis=0)
            b13 = b17[np.argmax(b12)]
            file.write(b13 + " " + tweet)
    print("Output written to", output_file)
b14 = "path_to_train_file.txt"
b15 = "path_to_test_file.txt"
b16 = "output_file.txt"
b17 = ['Los_Angeles,_CA', 'San_Francisco,_CA', 'San_Diego,_CA', 'Houston,_TX', 'Chicago,_IL', 'Philadelphia,_PA',
            'Toronto,_Ontario', 'Atlanta,_GA', 'Boston,_MA', 'Orlando,_FL', 'Washington,_DC', 'Manhattan,_NY']
b18 = ["los_angel", "san_francisco", "san_diego", "houston", "chicago", "philadelphia", "toronto", "atlanta", "boston",
        "orlando", "washington", "manhattan"]
b19 = dict.fromkeys(b18, 0)
b20 = fonk1(b14)
b21 = fonk2(b20)
b22 = fonk3(b15)
fonk4(b20)
b21 = b21 + (0.00001)
fonk5(b21, b22, b16)
print('Top five b5 for each b18:')
for city_name in b18:
    print(b17[b18.index(city_name)], b21.nlargest(5, city_name).index.tolist())