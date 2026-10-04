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
with open(b2, 'wb') as f:
    f.write(b5.content)
with zipfile.ZipFile(b2, 'r') as zip_ref:
    zip_ref.extractall(b4)
b6 = os.path.join(b4, b3)
b7 = os.path.join(b4, "tw-data.pos")
b8 = os.path.join(b4, "tw-data.neg")
try:
    with open(b6, "r", b9 = 'ISO-8859-1') as full_dataset, \
         open(b7, "w", b9 = 'ISO-8859-1') as pos_dataset, \
         open(b8, "w", b9 = 'ISO-8859-1'):
        b10 = csv.reader(full_dataset)
        next(b10)
        for line in tqdm(b10):
            b11 = line[3].strip()
            b12 = ''
            for b13 in b11.split():
                if re.match('^.*@.*', b13):
                    b13 = '<NAME/>'
                if re.match('^.*http:
                    b13 = '<LINK/>'
                b13 = b13.replace('&quot;', ' \" ')
                b13 = b13.replace('&amp;', ' & ')
                b13 = b13.replace('&gt;', ' > ')
                b13 = b13.replace('&lt;', ' < ')
                b12 = ' '.join([b12, b13])
            b11 = b12.strip() + '\n'
            if line[1].strip() == '1':
                pos_dataset.write(b11)
            else:
                neg_dataset.write(b11)
except IOError as e:
    print(f"Failed to open file: {e}")