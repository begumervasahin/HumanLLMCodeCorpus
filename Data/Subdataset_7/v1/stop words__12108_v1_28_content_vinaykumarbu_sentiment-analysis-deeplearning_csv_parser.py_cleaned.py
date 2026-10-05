import re
from tqdm import tqdm
import requests
from zipfile import ZipFile
import os
b1 = "http:
b2 = "sentiment_dataset.zip"
b3 = "twitter-sentiment-dataset"
try:
    os.makedirs(b3, b4 = True)
    with open(b2, "wb") as f:
        b5 = requests.get(b1)
        f.write(b5.content)
    with ZipFile(b2, "r") as zip_ref:
        zip_ref.extractall(b3)
except Exception as e:
    print("Failed to download or extract dataset:", e)
    quit()
try:
    b6 = open(os.path.join(b3, "Sentiment Analysis Dataset.csv"), "r", encoding="ISO-8859-1")
    b7 = open(os.path.join(b3, "tw-data.pos"), "w")
    b8 = open(os.path.join(b3, "tw-data.neg"), "w")
except IOError:
    print("Failed to open file")
    quit()
b9 = b6.readlines()
for b10 in tqdm(b9):
    b10 = b10.strip().split(",", 3)
    b11 = b10[3].strip()
    b11 = re.sub(r'@[\w_]+', '<NAME/>', b11)
    b11 = re.sub(r'http[s]?:
    b11 = re.sub(r'&quot;', '\"', b11)
    b11 = re.sub(r'&amp;', '&', b11)
    b11 = re.sub(r'&gt;', '>', b11)
    b11 = re.sub(r'&lt;', '<', b11)
    if b10[1].strip() == '1':
        b7.write(b11 + "\n")
    else:
        b8.write(b11 + "\n")
b6.close()
b7.close()
b8.close()
print("Dataset split and preprocessed successfully.")