import pandas as pd
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import sys
nltk.download('stopwords')
nltk.download('punkt')
def parse_file(f1, city):
    with open(f1, 'r') as datafile:
        content = datafile.readlines()
    words = [word_tokenize(line) for line in content]
    stop = stopwords.words('english')
    punct_stopwords = list(string.punctuation) + ['i', '\x89', '_CA', '_TX', '_IL', '_NY', '_PA', '_GA', '_Ontario', '_MA', '_FL', '_DC', '__', '___'] + stop
    stemmer = SnowballStemmer("english")
    words = [[stemmer.stem(w) for w in item if w not in punct_stopwords] for item in words if len(item) > 1]
    return [word for word in words if len(word) > 1 and word[0] in city]
def train_df(t, city):
    word_list = set([w for word in t for w in word])
    data = pd.DataFrame(0, index=word_list, columns=city)
    for word in t[:]:
        current_city = word[0]
        for w in word[1:]:
            data.at[w, current_city] += 1
    return data
def test_dict(f2):
    with open(f2, 'r') as datafile:
        content = datafile.readlines()
    td = {}
    stop = stopwords.words('english')
    punct_stopwords = list(string.punctuation) + ['i', '\x89', '_CA', '_TX', '_IL', '_NY', '_PA', '_GA', '_Ontario', '_MA', '_FL', '_DC', '__', '___'] + stop
    stemmer = SnowballStemmer("english")
    for line in content:
        words = word_tokenize(line)
        td[line] = [stemmer.stem(w) for w in words if w not in punct_stopwords]
        if td[line]:
            td[line].pop(0)
    return td
def get_city_prob(words, city_prob):
    for word in words:
        city_prob[word[0]] += 1
    total = sum(city_prob.values())
    for i in city_prob:
        city_prob[i] = float(city_prob[i] / total)
def bayes(tdf, test, f3, city_prob, old_city, city):
    with open(f3, 'w') as f:
        for tweet in test:
            label = ''
            words = test[tweet]
            if not words:
                continue
            else:
                wpost = [[(tdf.at[w, city[i]] / sum(tdf.loc[:, city[i]]) * city_prob[city[i]]) if w in tdf.index else 0.00001 * city_prob[city[i]] for i in range(0, 12)] for w in words]
            p = wpost[0]
            for i in range(1, len(wpost)):
                p = [x * y for x, y in zip(p, wpost[i])]
            label = old_city[p.index(max(p))]
            f.write(label + " " + tweet)
    print("Output written to ", f3)
if __name__ == "__main__":
    f1 = str(sys.argv[1])
    f2 = str(sys.argv[2])
    f3 = str(sys.argv[3])
    old_city = ['Los_Angeles,_CA', 'San_Francisco,_CA', 'San_Diego,_CA', 'Houston,_TX', 'Chicago,_IL', 'Philadelphia,_PA', 'Toronto,_Ontario', 'Atlanta,_GA', 'Boston,_MA', 'Orlando,_FL', 'Washington,_DC', 'Manhattan,_NY']
    city = ["los_angel", "san_francisco", "san_diego", "houston", "chicago", "philadelphia", "toronto", "atlanta", "boston", "orlando", "washington", "manhattan"]
    city_prob = dict.fromkeys(city, 0)
    train = parse_file(f1, city)
    tdf = train_df(train, city)
    test = test_dict(f2)
    get_city_prob(train, city_prob)
    tdf += (0.00001)
    bayes(tdf, test, f3, city_prob, old_city, city)
    print('Top five words for each city: ')
    for c in city:
        print(old_city[city.index(c)], tdf.nlargest(5, c).index.tolist())