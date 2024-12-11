import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import string
import sys
nltk.download('stopwords')
nltk.download('punkt')
b1 = ['Los_Angeles,_CA', 'San_Francisco,_CA', 'San_Diego,_CA', 'Houston,_TX', 'Chicago,_IL', 'Philadelphia,_PA', 'Toronto,_Ontario', 'Atlanta,_GA', 'Boston,_MA', 'Orlando,_FL', 'Washington,_DC', 'Manhattan,_NY']
b2 = ["los_angel", "san_francisco", "san_diego", "houston", "chicago", "philadelphia", "toronto", "atlanta", "boston", "orlando", "washington", "manhattan"]
b3 = {city: 0 for city in b2}
def fonk1(file_path):
    with open(file_path, 'r') as file:
        b4 = file.readlines()
    b5 = set(stopwords.b9('english'))
    b6 = set(string.b6)
    b7 = b6.union(['i','\x89','_CA','_TX', '_IL','_NY', '_PA', '_GA', '_Ontario', '_MA', '_FL', '_DC','__', '___']).union(b5)
    b8 = SnowballStemmer("english")
    b9 = []
    for line in b4:
        b10 = word_tokenize(line)
        b11 = [b8.stem(w) for w in b10 if w.lower() not in b7 and len(w) > 1]
        if len(b11) > 1:
            b9.append(b11)
    return [word for word in b9 if len(word) > 1 and word[0] in b2]
def fonk2(train_data):
    b12 = set([w for word in train_data for w in word])
    b13 = pd.DataFrame(0, index=b12, columns=b2)
    for word in train_data:
        b14 = word[0]
        for w in word[1:]:
            b13.at[w, b14] += 1
    return b13
def fonk3(file_path):
    with open(file_path, 'r') as file:
        b4 = file.readlines()
    b15 = {}
    b5 = set(stopwords.b9('english'))
    b6 = set(string.b6)
    b7 = b6.union(['i','\x89','_CA','_TX', '_IL','_NY', '_PA', '_GA', '_Ontario', '_MA', '_FL', '_DC','__', '___']).union(b5)
    b8 = SnowballStemmer("english")
    for line in b4:
        b10 = word_tokenize(line)
        b11 = [b8.stem(w) for w in b10 if w.lower() not in b7]
        if b11:
            b11.pop(0)
            b15[line] = b11
    return b15
def fonk4(train_data):
    for word in train_data:
        b3[word[0]] += 1
    b16 = sum(b3.values())
    for city in b3:
        b3[city] = float(b3[city] / b16)
def fonk5(train_df, b15, output_file):
    with open(output_file, 'w') as file:
        for tweet in b15:
            b17 = ''
            b9 = b15[tweet]
            if not b9:
                continue
            else:
                b18 = [[(train_df.at[w, city[i]] / sum(train_df.loc[:, city[i]]) * b3[city[i]]) if w in train_df.index else 0.00001 * b3[city[i]] for i in range(0, 12)] for w in b9]
                b19 = np.prod(b18, axis=0)
                b17 = b1[np.argmax(b19)]
                file.write(b17 + " " + tweet)
    print("Output written to ", output_file)
if b20 = = "__main__":
    b21 = str(sys.argv[1])
    b22 = str(sys.argv[2])
    b23 = str(sys.argv[3])
    b24 = fonk1(b21)
    b25 = fonk2(b24)
    b26 = fonk3(b22)
    fonk4(b24)
    b25 += (0.00001)
    fonk5(b25, b26, b23)
    print('Top five b9 for each city: ')
    for city_name in b2:
        print(b1[b2.index(city_name)], b25.nlargest(5, city_name).index.tolist())