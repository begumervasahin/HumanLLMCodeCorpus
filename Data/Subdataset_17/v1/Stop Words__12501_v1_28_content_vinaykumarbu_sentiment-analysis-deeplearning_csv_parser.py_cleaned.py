import csv
import re
from tqdm import tqdm
import requests
import zipfile
import os
url = "http:
zip_file = "Sentiment-Analysis-Dataset.zip"
csv_file = "Sentiment-Analysis-Dataset.csv"
data_folder = "twitter-sentiment-dataset"
response = requests.get(url)
with open(zip_file, 'wb') as f:
    f.write(response.content)
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(data_folder)
csv_path = os.path.join(data_folder, csv_file)
pos_path = os.path.join(data_folder, "tw-data.pos")
neg_path = os.path.join(data_folder, "tw-data.neg")
try:
    with open(csv_path, "r", encoding='ISO-8859-1') as full_dataset, \
         open(pos_path, "w", encoding='ISO-8859-1') as pos_dataset, \
         open(neg_path, "w", encoding='ISO-8859-1'):
        csv_reader = csv.reader(full_dataset)
        next(csv_reader)
        for line in tqdm(csv_reader):
            tweet = line[3].strip()
            new_tweet = ''
            for word in tweet.split():
                if re.match('^.*@.*', word):
                    word = '<NAME/>'
                if re.match('^.*http:
                    word = '<LINK/>'
                word = word.replace('&quot;', ' \" ')
                word = word.replace('&amp;', ' & ')
                word = word.replace('&gt;', ' > ')
                word = word.replace('&lt;', ' < ')
                new_tweet = ' '.join([new_tweet, word])
            tweet = new_tweet.strip() + '\n'
            if line[1].strip() == '1':
                pos_dataset.write(tweet)
            else:
                neg_dataset.write(tweet)
except IOError as e:
    print(f"Failed to open file: {e}")