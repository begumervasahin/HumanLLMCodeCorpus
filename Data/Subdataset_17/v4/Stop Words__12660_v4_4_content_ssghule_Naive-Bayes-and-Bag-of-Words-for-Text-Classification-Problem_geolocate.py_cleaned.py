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
OLD_CITY = [
    'Los_Angeles,_CA', 'San_Francisco,_CA', 'San_Diego,_CA', 'Houston,_TX',
    'Chicago,_IL', 'Philadelphia,_PA', 'Toronto,_Ontario', 'Atlanta,_GA',
    'Boston,_MA', 'Orlando,_FL', 'Washington,_DC', 'Manhattan,_NY'
]
CITY = [
    "los_angel", "san_francisco", "san_diego", "houston", "chicago",
    "philadelphia", "toronto", "atlanta", "boston", "orlando", "washington", "manhattan"
]
CITY_PROB = dict.fromkeys(CITY, 0)
def parse_file(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()
    words = [word_tokenize(line) for line in content]
    stop_words = stopwords.words('english')
    punct_stopwords = list(string.punctuation) + ['i', '\x89', '_CA', '_TX', '_IL', '_NY', '_PA', '_GA', '_Ontario', '_MA', '_FL', '_DC', '__', '___'] + stop_words
    stemmer = SnowballStemmer("english")
    processed_words = [
        [stemmer.stem(w) for w in item if w not in punct_stopwords]
        for item in words if len(item) > 1
    ]
    return [word for word in processed_words if len(word) > 1 and word[0] in CITY]
def train_df(training_data):
    word_list = set([w for word in training_data for w in word])
    data = pd.DataFrame(0, index=word_list, columns=CITY)
    for word in training_data:
        current_city = word[0]
        for w in word[1:]:
            data.at[w, current_city] += 1
    return data
def test_dict(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()
    stop_words = stopwords.words('english')
    punct_stopwords = list(string.punctuation) + ['i', '\x89', '_CA', '_TX', '_IL', '_NY', '_PA', '_GA', '_Ontario', '_MA', '_FL', '_DC', '__', '___'] + stop_words
    stemmer = SnowballStemmer("english")
    test_data = {}
    for line in content:
        words = word_tokenize(line)
        test_data[line] = [stemmer.stem(w) for w in words if w not in punct_stopwords]
        if test_data[line]:
            test_data[line].pop(0)
    return test_data
def get_city_prob(words):
    for word in words:
        CITY_PROB[word[0]] += 1
    total = sum(CITY_PROB.values())
    for city in CITY_PROB:
        CITY_PROB[city] = float(CITY_PROB[city] / total)
def bayes(tdf, test_data, output_file):
    with open(output_file, 'w') as file:
        for tweet in test_data:
            words = test_data[tweet]
            if not words:
                continue
            wpost = [
                [
                    (tdf.at[w, city] / sum(tdf.loc[:, city]) * CITY_PROB[city]) if w in tdf.index else 0.00001 * CITY_PROB[city]
                    for city in CITY
                ]
                for w in words
            ]
            p = wpost[0]
            for i in range(1, len(wpost)):
                p = np.multiply(p, wpost[i])
            p = list(p)
            label = OLD_CITY[p.index(max(p))]
            file.write(label + " " + tweet)
    print("Output written to", output_file)
if __name__ == "__main__":
    f1, f2, f3 = sys.argv[1], sys.argv[2], sys.argv[3]
    train_data = parse_file(f1)
    tdf = train_df(train_data)
    test_data = test_dict(f2)
    get_city_prob(train_data)
    tdf += 0.00001
    bayes(tdf, test_data, f3)
    print('Top five words for each city:')
    for city in CITY:
        print(OLD_CITY[CITY.index(city)], tdf.nlargest(5, city).index.tolist())