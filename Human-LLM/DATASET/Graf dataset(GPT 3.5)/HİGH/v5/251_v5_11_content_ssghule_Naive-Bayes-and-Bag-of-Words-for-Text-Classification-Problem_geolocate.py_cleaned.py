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
    with open(file_path, 'r') as data_file:
        b1 = data_file.readlines()
    b2 = stopwords.b11('english')
    b3 = list(string.punctuation) + ['i', '\x89', '_CA', '_TX', '_IL', '_NY', '_PA', '_GA', '_Ontario', '_MA', '_FL', '_DC', '__', '___'] + b2
    b4 = SnowballStemmer("english")
    b5 = [word_tokenize(line) for line in b1]
    b6 = [
        [b4.stem(w) for w in item if w not in b3]
        for item in b5 if len(item) > 1
    ]
    return [word for word in b6 if len(word) > 1 and word[0] in b20]
def fonk2(b22):
    b7 = set([w for word in b22 for w in word])
    b8 = pd.DataFrame(0, index=b7, columns=b20)
    for word in b22:
        b9 = word[0]
        for w in word[1:]:
            b8.at[w, b9] += 1
    return b8
def fonk3(file_path):
    with open(file_path, 'r') as data_file:
        b1 = data_file.readlines()
    b10 = {}
    b2 = stopwords.b11('english')
    b3 = list(string.punctuation) + ['i', '\x89', '_CA', '_TX', '_IL', '_NY', '_PA', '_GA', '_Ontario', '_MA', '_FL', '_DC', '__', '___'] + b2
    b4 = SnowballStemmer("english")
    for line in b1:
        b11 = word_tokenize(line)
        b10[line] = [b4.stem(w) for w in b11 if w not in b3]
        if b10[line]:
            b10[line].pop(0)
    return b10
def fonk4(b11):
    for word in b11:
        b21[word[0]] += 1
    b12 = sum(b21.values())
    for i in b21:
        b21[i] = float(b21[i] / b12)
def fonk5(b23, b10, output_file):
    with open(output_file, 'w') as f:
        for tweet in b10:
            b13 = ''
            b11 = b10[tweet]
            if not b11:
                continue
            else:
                b14 = [
                    [
                        (b23.at[w, b20[i]] / sum(b23.loc[:, b20[i]]) * b21[b20[i]])
                        if w in b23.index else 0.00001 * b21[b20[i]]
                        for i in range(0, 12)
                    ]
                    for w in b11
                ]
                b15 = b14[0]
                for i in range(1, len(b14)):
                    b15 = np.multiply(b15, b14[i])
                b15 = list(b15)
                b13 = b19[b15.index(max(b15))]
                f.write(b13 + " " + tweet)
    print("Output written to", output_file)
b16 = str(sys.argv[1])
b17 = str(sys.argv[2])
b18 = str(sys.argv[3])
b19 = ['Los_Angeles,_CA', 'San_Francisco,_CA', 'San_Diego,_CA', 'Houston,_TX', 'Chicago,_IL', 'Philadelphia,_PA',
            'Toronto,_Ontario', 'Atlanta,_GA', 'Boston,_MA', 'Orlando,_FL', 'Washington,_DC', 'Manhattan,_NY']
b20 = ["los_angel", "san_francisco", "san_diego", "houston", "chicago", "philadelphia", "toronto", "atlanta", "boston",
        "orlando", "washington", "manhattan"]
b21 = dict.fromkeys(b20, 0)
b22 = fonk1(b16)
b23 = fonk2(b22)
b24 = fonk3(b17)
fonk4(b22)
b23 = b23 + 0.00001
fonk5(b23, b24, b18)
print('Top five b11 for each b20:')
for c in b20:
    print(b19[b20.index(c)], b23.nlargest(5, c).index.tolist())