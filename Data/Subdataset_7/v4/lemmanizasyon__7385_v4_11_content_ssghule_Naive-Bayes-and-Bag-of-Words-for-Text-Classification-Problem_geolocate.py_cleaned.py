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
    b2 = stopwords.b5('english')
    b3 = list(string.punctuation) + ['i', '\x89', '_CA', '_TX', '_IL', '_NY', '_PA', '_GA', '_Ontario', '_MA', '_FL', '_DC', '__', '___'] + b2
    b4 = SnowballStemmer("english")
    b5 = [[b4.stem(w) for w in item if w not in b3] for item in [word_tokenize(line) for line in b1] if len(item) > 1]
    return [word for word in b5 if len(word) > 1 and word[0] in b18]
def fonk2(b20):
    b6 = set([w for word in b20 for w in word])
    b7 = pd.DataFrame(0, index=b6, columns=b18)
    for word in b20:
        b8 = word[0]
        for w in word[1:]:
            b7.at[w, b8] += 1
    return b7
def fonk3(file_path):
    with open(file_path, 'r') as data_file:
        b1 = data_file.readlines()
    b9 = {}
    b2 = stopwords.b5('english')
    b3 = list(string.punctuation) + ['i', '\x89', '_CA', '_TX', '_IL', '_NY', '_PA', '_GA', '_Ontario', '_MA', '_FL', '_DC', '__', '___'] + b2
    b4 = SnowballStemmer("english")
    for line in b1:
        b5 = word_tokenize(line)
        b9[line] = [b4.stem(w) for w in b5 if w not in b3]
        if b9[line]:
            b9[line].pop(0)
    return b9
def fonk4(b5):
    for word in b5:
        b19[word[0]] += 1
    b10 = sum(b19.values())
    for i in b19:
        b19[i] = float(b19[i] / b10)
def fonk5(b21, b9, output_file):
    with open(output_file, 'w') as f:
        for tweet in b9:
            b11 = ''
            b5 = b9[tweet]
            if not b5:
                continue
            else:
                b12 = [
                    [(b21.at[w, b18[i]] / sum(b21.loc[:, b18[i]]) * b19[b18[i]])
                     if w in b21.index else 0.00001 * b19[b18[i]] for i in range(0, 12)] for w in b5]
                b13 = b12[0]
                for i in range(1, len(b12)):
                    b13 = np.multiply(b13, b12[i])
                b13 = list(b13)
                b11 = b17[b13.index(max(b13))]
                f.write(b11 + " " + tweet)
    print("Output written to", output_file)
b14 = str(sys.argv[1])
b15 = str(sys.argv[2])
b16 = str(sys.argv[3])
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
for c in b18:
    print(b17[b18.index(c)], b21.nlargest(5, c).index.tolist())