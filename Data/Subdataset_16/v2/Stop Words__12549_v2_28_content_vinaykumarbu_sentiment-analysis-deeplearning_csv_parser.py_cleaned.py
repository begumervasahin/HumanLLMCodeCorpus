import csv
import re
from tqdm import tqdm
import requests
import zipfile
import os
b1 = "http:
b2 = "Sentiment-Analysis-Dataset.zip"
b3 = "Sentiment-Analysis-Dataset.csv"
b4 = "twitter-sentiment-dataset"
b5 = requests.get(b1)
with open(b2, 'wb') as zip_file:
    zip_file.write(b5.content)
with zipfile.ZipFile(b2, 'r') as zip_ref:
    zip_ref.extractall(b4)
b6 = os.path.join(b4, b3)
b7 = os.path.join(b4, "tw-data.pos")
b8 = os.path.join(b4, "tw-data.neg")
try:
    with open(b6, "r", b9 = 'ISO-8859-1') as csv_file, \
         open(b7, "w", b9 = 'ISO-8859-1') as pos_file, \
         open(b8, "w", b9 = 'ISO-8859-1') as neg_file:
        b10 = csv.reader(csv_file)
        next(b10)
        for line in tqdm(b10, b11 = "Processing tweets"):
            b12 = line[3].strip()
            b13 = []
            for b14 in b12.split():
                if re.match(r'^.*@.*', b14):
                    b14 = '<NAME/>'
                elif re.match(r'^.*http:
                    b14 = '<LINK/>'
                b14 = b14.replace('&quot;', ' " ')
                b14 = b14.replace('&amp;', ' & ')
                b14 = b14.replace('&gt;', ' > ')
                b14 = b14.replace('&lt;', ' < ')
                b13.append(b14)
            b15 = ' '.join(b13).strip() + '\n'
            if line[1].strip() == '1':
                pos_file.write(b15)
            else:
                neg_file.write(b15)
except IOError as e:
    print(f"Failed to open file: {e}")