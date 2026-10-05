import re
import requests
import os
from zipfile import ZipFile
from tqdm import tqdm
dataset_url = "http:
zip_file_path = "sentiment_dataset.zip"
data_folder = "twitter-sentiment-dataset"
try:
    os.makedirs(data_folder, exist_ok=True)
    with open(zip_file_path, "wb") as zip_file:
        response = requests.get(dataset_url)
        zip_file.write(response.content)
    with ZipFile(zip_file_path, "r") as zip_ref:
        zip_ref.extractall(data_folder)
except Exception as e:
    print("Failed to download or extract the dataset:", e)
    quit()
try:
    full_dataset_file = open(os.path.join(data_folder, "Sentiment Analysis Dataset.csv"), "r", encoding="ISO-8859-1")
    positive_dataset_file = open(os.path.join(data_folder, "tw-data.pos"), "w")
    negative_dataset_file = open(os.path.join(data_folder, "tw-data.neg"), "w")
except IOError:
    print("Failed to open files")
    quit()
csv_lines = full_dataset_file.readlines()
for line in tqdm(csv_lines):
    columns = line.strip().split(",", 3)
    tweet_text = columns[3].strip()
    tweet_text = re.sub(r'@[\w_]+', '<NAME/>', tweet_text)
    tweet_text = re.sub(r'http[s]?:
    tweet_text = re.sub(r'&quot;', '\"', tweet_text)
    tweet_text = re.sub(r'&amp;', '&', tweet_text)
    tweet_text = re.sub(r'&gt;', '>', tweet_text)
    tweet_text = re.sub(r'&lt;', '<', tweet_text)
    if columns[1].strip() == '1':
        positive_dataset_file.write(tweet_text + "\n")
    else:
        negative_dataset_file.write(tweet_text + "\n")
full_dataset_file.close()
positive_dataset_file.close()
negative_dataset_file.close()
print("Dataset split and preprocessed successfully.")