import pandas as pd
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import sys
nltk.download('stopwords')
nltk.download('punkt')
def fonk1(file_path, city_list):
    with open(file_path, 'r') as file:
        b1 = file.readlines()
    b2 = [word_tokenize(line) for line in b1]
    b3 = stopwords.b2('english')
    b4 = list(string.punctuation) + ['i', '\x89', '_CA', '_TX', '_IL', '_NY', '_PA', '_GA', '_Ontario', '_MA', '_FL', '_DC', '__', '___'] + b3
    b5 = SnowballStemmer("english")
    b6 = [[b5.stem(w) for w in item if w not in b4] for item in b2 if len(item) > 1]
    return [word for word in b6 if len(word) > 1 and word[0] in city_list]
def fonk2(parsed_data, city_list):
    b7 = set([w for word in parsed_data for w in word])
    b8 = pd.DataFrame(0, index=b7, columns=city_list)
    for word in parsed_data:
        b9 = word[0]
        for w in word[1:]:
            b8.at[w, b9] += 1
    return b8
def fonk3(file_path):
    with open(file_path, 'r') as file:
        b1 = file.readlines()
    b10 = {}
    b3 = stopwords.b2('english')
    b4 = list(string.punctuation) + ['i', '\x89', '_CA', '_TX', '_IL', '_NY', '_PA', '_GA', '_Ontario', '_MA', '_FL', '_DC', '__', '___'] + b3
    b5 = SnowballStemmer("english")
    for line in b1:
        b2 = word_tokenize(line)
        b11 = [b5.stem(w) for w in b2 if w not in b4]
        if b11:
            b11.pop(0)
        b10[line] = b11
    return b10
def fonk4(parsed_data, city_prob):
    for word in parsed_data:
        city_prob[word[0]] += 1
    b12 = sum(city_prob.values())
    for city in city_prob:
        city_prob[city] = float(city_prob[city] / b12)
def fonk5(tdf, b25, b19, b22, b20, b21):
    with open(b19, 'w') as file:
        for tweet, b2 in b25.items():
            if not b2:
                continue
            else:
                b13 = [[(tdf.at[word, city] / sum(tdf.loc[:, city]) * b22[city]) if word in tdf.index else 0.00001 * b22[city] for city in b21] for word in b2]
                b14 = b13[0]
                for i in range(1, len(b13)):
                    b14 = [x * y for x, y in zip(b14, b13[i])]
                b15 = b20[b14.index(max(b14))]
                file.write(b15 + " " + tweet)
    print("Output written to ", b19)
if b16 = = "__main__":
    b17 = str(sys.argv[1])
    b18 = str(sys.argv[2])
    b19 = str(sys.argv[3])
    b20 = ['Los_Angeles,_CA', 'San_Francisco,_CA', 'San_Diego,_CA', 'Houston,_TX', 'Chicago,_IL', 'Philadelphia,_PA', 'Toronto,_Ontario', 'Atlanta,_GA', 'Boston,_MA', 'Orlando,_FL', 'Washington,_DC', 'Manhattan,_NY']
    b21 = ["los_angel", "san_francisco", "san_diego", "houston", "chicago", "philadelphia", "toronto", "atlanta", "boston", "orlando", "washington", "manhattan"]
    b22 = dict.fromkeys(b21, 0)
    b23 = fonk1(b17, b21)
    b24 = fonk2(b23, b21)
    b25 = fonk3(b18)
    fonk4(b23, b22)
    fonk5(b24, b25, b19, b22, b20, b21)
    print('Top five b2 for each city: ')
    for city in b21:
        print(b20[b21.index(city)], b24.nlargest(5, city).index.tolist())