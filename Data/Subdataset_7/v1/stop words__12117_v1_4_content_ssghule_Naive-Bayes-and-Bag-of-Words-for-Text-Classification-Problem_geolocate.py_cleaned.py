import pandas as pd
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import sys
nltk.download('stopwords')
nltk.download('punkt')
def fonk1(b15, b19):
    with open(b15, 'r') as datafile:
        b1 = datafile.readlines()
    b2 = [word_tokenize(line) for line in b1]
    b3 = stopwords.b2('english')
    b4 = list(string.punctuation) + ['i', '\x89', '_CA', '_TX', '_IL', '_NY', '_PA', '_GA', '_Ontario', '_MA', '_FL', '_DC', '__', '___'] + b3
    b5 = SnowballStemmer("english")
    b2 = [[b5.stem(w) for w in item if w not in b4] for item in b2 if len(item) > 1]
    return [word for word in b2 if len(word) > 1 and word[0] in b19]
def fonk2(t, b19):
    b6 = set([w for word in t for w in word])
    b7 = pd.DataFrame(0, index=b6, columns=b19)
    for word in t[:]:
        b8 = word[0]
        for w in word[1:]:
            b7.at[w, b8] += 1
    return b7
def fonk3(b16):
    with open(b16, 'r') as datafile:
        b1 = datafile.readlines()
    b9 = {}
    b3 = stopwords.b2('english')
    b4 = list(string.punctuation) + ['i', '\x89', '_CA', '_TX', '_IL', '_NY', '_PA', '_GA', '_Ontario', '_MA', '_FL', '_DC', '__', '___'] + b3
    b5 = SnowballStemmer("english")
    for line in b1:
        b2 = word_tokenize(line)
        b9[line] = [b5.stem(w) for w in b2 if w not in b4]
        if b9[line]:
            b9[line].pop(0)
    return b9
def fonk4(b2, b20):
    for word in b2:
        b20[word[0]] += 1
    b10 = sum(b20.values())
    for i in b20:
        b20[i] = float(b20[i] / b10)
def fonk5(b22, b23, b17, b20, b18, b19):
    with open(b17, 'w') as f:
        for tweet in b23:
            b11 = ''
            b2 = b23[tweet]
            if not b2:
                continue
            else:
                b12 = [[(b22.at[w, b19[i]] / sum(b22.loc[:, b19[i]]) * b20[b19[i]]) if w in b22.index else 0.00001 * b20[b19[i]] for i in range(0, 12)] for w in b2]
            b13 = b12[0]
            for i in range(1, len(b12)):
                b13 = [x * y for x, y in zip(b13, b12[i])]
            b11 = b18[b13.index(max(b13))]
            f.write(b11 + " " + tweet)
    print("Output written to ", b17)
if b14 = = "__main__":
    b15 = str(sys.argv[1])
    b16 = str(sys.argv[2])
    b17 = str(sys.argv[3])
    b18 = ['Los_Angeles,_CA', 'San_Francisco,_CA', 'San_Diego,_CA', 'Houston,_TX', 'Chicago,_IL', 'Philadelphia,_PA', 'Toronto,_Ontario', 'Atlanta,_GA', 'Boston,_MA', 'Orlando,_FL', 'Washington,_DC', 'Manhattan,_NY']
    b19 = ["los_angel", "san_francisco", "san_diego", "houston", "chicago", "philadelphia", "toronto", "atlanta", "boston", "orlando", "washington", "manhattan"]
    b20 = dict.fromkeys(b19, 0)
    b21 = fonk1(b15, b19)
    b22 = fonk2(b21, b19)
    b23 = fonk3(b16)
    fonk4(b21, b20)
    b22 += (0.00001)
    fonk5(b22, b23, b17, b20, b18, b19)
    print('Top five b2 for each b19: ')
    for c in b19:
        print(b18[b19.index(c)], b22.nlargest(5, c).index.tolist())