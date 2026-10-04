import pandas as pd
import re
import string
from nltk.corpus import stopwords
import json
import numpy as np
class Preprocessing:
    def __init__(self):
        print("Initializing preprocessing...")
    def clean_text(self, text):
        words = text.split()
        for word in words:
            if '@' in word or 'http' in word or '\"' in word:
                print(f"Removing {word}")
                text = text.replace(word, '')
        return text.strip()
    def clean_csv(self, csv_file):
        data = pd.read_csv(csv_file).dropna()
        data['text'] = data['text'].apply(self.clean_text)
        data_cleaned = pd.DataFrame({'text': data['text']})
        data_cleaned.to_csv("data_cleaned.csv", header=False, index=True, encoding="utf-8")
    def process_tweet(self, tweet):
        tweet = re.sub(r'\&\w*;', '', tweet)
        tweet = re.sub(r'@[^\s]+', '', tweet)
        tweet = re.sub(r'\$\w*', '', tweet)
        tweet = tweet.lower()
        tweet = re.sub(r'https?:\/\/.*\/\w*', '', tweet)
        tweet = re.sub(r'[' + string.punctuation.replace('@', '') + ']+', ' ', tweet)
        tweet = re.sub(r'\b\w{1,2}\b', '', tweet)
        tweet = re.sub(r'\s\s+', ' ', tweet)
        tweet = tweet.lstrip(' ')
        tweet = ''.join(c for c in tweet if c <= '\uFFFF')
        return tweet
    def text_process(self, raw_text):
        nopunc = ''.join([char for char in raw_text if char not in string.punctuation])
        words = [word for word in nopunc.lower().split() if word.lower() not in stopwords.words('english')]
        return words
    def geo_mean(self, x):
        coords = np.asarray(json.loads(x))
        mean_geoloc = np.mean(coords[:, 0:2], axis=1).mean()
        mean_geoloc = np.around(mean_geoloc, decimals=6)
        print("Geometric mean:", mean_geoloc)
        return mean_geoloc
    def find_centroid(self, row):
        try:
            coords = eval(row)
            longitudes = [coord[0] for coord in coords]
            latitudes = [coord[1] for coord in coords]
            centroid = (np.mean(latitudes), np.mean(longitudes))
            print("Centroid:", centroid)
            return centroid
        except Exception as e:
            print("Error:", e)
            return None
