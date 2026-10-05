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
def parse_file(file_path):
    with open(file_path, 'r') as data_file:
        content = data_file.readlines()
    stop = stopwords.words('english')
    punct_stopwords = list(string.punctuation) + ['i', '\x89', '_CA', '_TX', '_IL', '_NY', '_PA', '_GA', '_Ontario', '_MA', '_FL', '_DC', '__', '___'] + stop
    stemmer = SnowballStemmer("english")
    tokenized_lines = [word_tokenize(line) for line in content]
    filtered_words = [
        [stemmer.stem(w) for w in item if w not in punct_stopwords]
        for item in tokenized_lines if len(item) > 1
    ]
    return [word for word in filtered_words if len(word) > 1 and word[0] in city]
def create_training_dataframe(train_data):
    word_list = set([w for word in train_data for w in word])
    data = pd.DataFrame(0, index=word_list, columns=city)
    for word in train_data:
        current_city = word[0]
        for w in word[1:]:
            data.at[w, current_city] += 1
    return data
def create_testing_dictionary(file_path):
    with open(file_path, 'r') as data_file:
        content = data_file.readlines()
    test_dict = {}
    stop = stopwords.words('english')
    punct_stopwords = list(string.punctuation) + ['i', '\x89', '_CA', '_TX', '_IL', '_NY', '_PA', '_GA', '_Ontario', '_MA', '_FL', '_DC', '__', '___'] + stop
    stemmer = SnowballStemmer("english")
    for line in content:
        words = word_tokenize(line)
        test_dict[line] = [stemmer.stem(w) for w in words if w not in punct_stopwords]
        if test_dict[line]:
            test_dict[line].pop(0)
    return test_dict
def calculate_city_probabilities(words):
    for word in words:
        city_prob[word[0]] += 1
    total = sum(city_prob.values())
    for i in city_prob:
        city_prob[i] = float(city_prob[i] / total)
def apply_bayes(train_df, test_dict, output_file):
    with open(output_file, 'w') as f:
        for tweet in test_dict:
            label = ''
            words = test_dict[tweet]
            if not words:
                continue
            else:
                wpost = [
                    [
                        (train_df.at[w, city[i]] / sum(train_df.loc[:, city[i]]) * city_prob[city[i]])
                        if w in train_df.index else 0.00001 * city_prob[city[i]]
                        for i in range(0, 12)
                    ]
                    for w in words
                ]
                p = wpost[0]
                for i in range(1, len(wpost)):
                    p = np.multiply(p, wpost[i])
                p = list(p)
                label = old_city[p.index(max(p))]
                f.write(label + " " + tweet)
    print("Output written to", output_file)
f1 = str(sys.argv[1])
f2 = str(sys.argv[2])
f3 = str(sys.argv[3])
old_city = ['Los_Angeles,_CA', 'San_Francisco,_CA', 'San_Diego,_CA', 'Houston,_TX', 'Chicago,_IL', 'Philadelphia,_PA',
            'Toronto,_Ontario', 'Atlanta,_GA', 'Boston,_MA', 'Orlando,_FL', 'Washington,_DC', 'Manhattan,_NY']
city = ["los_angel", "san_francisco", "san_diego", "houston", "chicago", "philadelphia", "toronto", "atlanta", "boston",
        "orlando", "washington", "manhattan"]
city_prob = dict.fromkeys(city, 0)
train_data = parse_file(f1)
train_df = create_training_dataframe(train_data)
test_data = create_testing_dictionary(f2)
calculate_city_probabilities(train_data)
train_df = train_df + 0.00001
apply_bayes(train_df, test_data, f3)
print('Top five words for each city:')
for c in city:
    print(old_city[city.index(c)], train_df.nlargest(5, c).index.tolist())