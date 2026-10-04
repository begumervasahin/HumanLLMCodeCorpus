import re
from tqdm import tqdm
b1 = "http:
b2 = "twitter-sentiment-dataset/sentiment-dataset.csv"
b3 = "twitter-sentiment-dataset/tw-data.pos"
b4 = "twitter-sentiment-dataset/tw-data.neg"
try:
    with open(b2, "r") as full_dataset, \
         open(b3, "w") as pos_dataset, \
         open(b4, "w") as neg_dataset:
        b5 = full_dataset.readlines()
        for line in tqdm(b5):
            b6 = line.split(",", 3)
            b7 = b6[3].strip()
            b8 = []
            for b9 in b7.split():
                if re.match(r'^.*@.*', b9):
                    b9 = '<NAME/>'
                elif re.match(r'^.*http:
                    b9 = '<LINK/>'
                b9 = b9.replace('&quot;', ' " ')
                b9 = b9.replace('&amp;', ' & ')
                b9 = b9.replace('&gt;', ' > ')
                b9 = b9.replace('&lt;', ' < ')
                b8.append(b9)
            b10 = ' '.join(b8).strip() + '\n'
            if b6[1].strip() == '1':
                pos_dataset.write(b10)
            else:
                neg_dataset.write(b10)
except IOError:
    print("Failed to open file")