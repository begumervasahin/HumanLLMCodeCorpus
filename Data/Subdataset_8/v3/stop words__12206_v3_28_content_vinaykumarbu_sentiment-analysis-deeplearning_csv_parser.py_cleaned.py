import re
import requests
import os
from zipfile import ZipFile
from tqdm import tqdm
def download_and_extract_dataset(url, zip_file_path, data_folder):
    try:
        os.makedirs(data_folder, exist_ok=True)
        with open(zip_file_path, "wb") as zip_file:
            response = requests.get(url)
            zip_file.write(response.content)
        with ZipFile(zip_file_path, "r") as zip_ref:
            zip_ref.extractall(data_folder)
    except Exception as e:
        print("Failed to download or extract the dataset:", e)
        quit()
def preprocess_tweet(tweet):
    tweet = re.sub(r'@[\w_]+', '<NAME/>', tweet)
    tweet = re.sub(r'http[s]?:
    tweet = re.sub(r'&quot;', '\"', tweet)
    tweet = re.sub(r'&amp;', '&', tweet)
    tweet = re.sub(r'&gt;', '>', tweet)
    tweet = re.sub(r'&lt;', '<', tweet)
    return tweet
def split_and_preprocess_dataset(input_file_path, positive_output_file_path, negative_output_file_path):
    try:
        with open(input_file_path, "r", encoding="ISO-8859-1") as input_file, \
             open(positive_output_file_path, "w") as positive_output_file, \
             open(negative_output_file_path, "w") as negative_output_file:
            csv_lines = input_file.readlines()
            for line in tqdm(csv_lines):
                columns = line.strip().split(",", 3)
                tweet_text = columns[3].strip()
                tweet_text = preprocess_tweet(tweet_text)
                if columns[1].strip() == '1':
                    positive_output_file.write(tweet_text + "\n")
                else:
                    negative_output_file.write(tweet_text + "\n")
    except IOError:
        print("Failed to open files")
        quit()
def main():
    dataset_url = "http:
    zip_file_path = "sentiment_dataset.zip"
    data_folder = "twitter-sentiment-dataset"
    input_file_path = os.path.join(data_folder, "Sentiment Analysis Dataset.csv")
    positive_output_file_path = os.path.join(data_folder, "tw-data.pos")
    negative_output_file_path = os.path.join(data_folder, "tw-data.neg")
    download_and_extract_dataset(dataset_url, zip_file_path, data_folder)
    split_and_preprocess_dataset(input_file_path, positive_output_file_path, negative_output_file_path)
    print("Dataset split and preprocessed successfully.")
if __name__ == "__main__":
    main()