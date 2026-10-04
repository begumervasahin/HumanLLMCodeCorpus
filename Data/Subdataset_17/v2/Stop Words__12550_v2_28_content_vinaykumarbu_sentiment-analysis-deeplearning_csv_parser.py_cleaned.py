import csv
import re
from tqdm import tqdm
import requests
import zipfile
import os
dataset_url = "http:
zip_filename = "Sentiment-Analysis-Dataset.zip"
csv_filename = "Sentiment-Analysis-Dataset.csv"
data_directory = "twitter-sentiment-dataset"
response = requests.get(dataset_url)
with open(zip_filename, 'wb') as zip_file:
    zip_file.write(response.content)
with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
    zip_ref.extractall(data_directory)
csv_filepath = os.path.join(data_directory, csv_filename)
pos_filepath = os.path.join(data_directory, "tw-data.pos")
neg_filepath = os.path.join(data_directory, "tw-data.neg")
try:
    with open(csv_filepath, "r", encoding='ISO-8859-1') as csv_file, \
         open(pos_filepath, "w", encoding='ISO-8859-1') as pos_file, \
         open(neg_filepath, "w", encoding='ISO-8859-1') as neg_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in tqdm(csv_reader, desc="Processing tweets"):
            tweet = line[3].strip()
            new_tweet = []
            for word in tweet.split():
                if re.match(r'^.*@.*', word):
                    word = '<NAME/>'
                elif re.match(r'^.*http:
                    word = '<LINK/>'
                word = word.replace('&quot;', ' " ')
                word = word.replace('&amp;', ' & ')
                word = word.replace('&gt;', ' > ')
                word = word.replace('&lt;', ' < ')
                new_tweet.append(word)
            processed_tweet = ' '.join(new_tweet).strip() + '\n'
            if line[1].strip() == '1':
                pos_file.write(processed_tweet)
            else:
                neg_file.write(processed_tweet)
except IOError as e:
    print(f"Failed to open file: {e}")