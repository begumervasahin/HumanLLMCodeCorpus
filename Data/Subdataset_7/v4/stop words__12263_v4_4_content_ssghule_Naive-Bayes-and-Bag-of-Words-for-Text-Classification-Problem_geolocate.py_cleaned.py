import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import numpy as np
import string
import sys
nltk.download('stopwords')
nltk.download('punkt')
def fonk1(file_path):
    with open(file_path, 'r') as file:
        b1 = file.readlines()
    b2 = set(stopwords.b6('english'))
    b3 = set(string.b3)
    b4 = b3.union(['i','\x89','_CA','_TX', '_IL','_NY', '_PA', '_GA', '_Ontario', '_MA', '_FL', '_DC','__', '___']).union(b2)
    b5 = SnowballStemmer("english")
    b6 = []
    for line in b1:
        b7 = word_tokenize(line)
        b8 = [b5.stem(w) for w in b7 if w.lower() not in b4 and len(w) > 1]
        if len(b8) > 1:
            b6.append(b8)
    return [word for word in b6 if len(word) > 1 and word[0] in b18]
def fonk2(train_data):
    b9 = set([w for word in train_data for w in word])
    b10 = pd.DataFrame(0, index=b9, columns=b18)
    for word in train_data:
        b11 = word[0]
        for w in word[1:]:
            b10.at[w, b11] += 1
    return b10
def fonk3(file_path):
    with open(file_path, 'r') as file:
        b1 = file.readlines()
    b12 = {}
    b2 = set(stopwords.b6('english'))
    b3 = set(string.b3)
    b4 = b3.union(['i','\x89','_CA','_TX', '_IL','_NY', '_PA', '_GA', '_Ontario', '_MA', '_FL', '_DC','__', '___']).union(b2)
    b5 = SnowballStemmer("english")
    for line in b1:
        b7 = word_tokenize(line)
        b8 = [b5.stem(w) for w in b7 if w.lower() not in b4]
        if b8:
            b8.pop(0)
            b12[line] = b8
    return b12
def fonk4(train_data):
    for word in train_data:
        b19[word[0]] += 1
    b13 = sum(b19.values())
    for city in b19:
        b19[city] = float(b19[city] / b13)
def fonk5(train_df, b12, output_file):
    with open(output_file, 'w') as file:
        for tweet in b12:
            b14 = ''
            b6 = b12[tweet]
            if not b6:
                continue
            else:
                b15 = [[(train_df.at[w, city[i]] / sum(train_df.loc[:, city[i]]) * b19[city[i]]) if w in train_df.index else 0.00001 * b19[city[i]] for i in range(0, 12)] for w in b6]
                b16 = np.prod(b15, axis=0)
                b14 = b17[np.argmax(b16)]
                file.write(b14 + " " + tweet)
    print("Output written to ", output_file)
b17 = ['Los_Angeles,_CA', 'San_Francisco,_CA','San_Diego,_CA', 'Houston,_TX','Chicago,_IL','Philadelphia,_PA', 'Toronto,_Ontario','Atlanta,_GA','Boston,_MA', 'Orlando,_FL', 'Washington,_DC', 'Manhattan,_NY']
b18 = ["los_angel", "san_francisco", "san_diego", "houston", "chicago", "philadelphia", "toronto", "atlanta", "boston", "orlando", "washington", "manhattan"]
b19 = dict.fromkeys(b18, 0)
b20 = str(sys.argv[1])
b21 = str(sys.argv[2])
b22 = str(sys.argv[3])
b23 = fonk1(b20)
b24 = fonk2(b23)
b25 = fonk3(b21)
fonk4(b23)
b24 += (0.00001)
fonk5(b24, b25, b22)
print('Top five b6 for each city: ')
for city_name in b18:
    print(b17[b18.index(city_name)], b24.nlargest(5, city_name).index.tolist())