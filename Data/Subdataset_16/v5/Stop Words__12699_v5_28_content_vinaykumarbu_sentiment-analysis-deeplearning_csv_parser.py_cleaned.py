import re
from tqdm import tqdm
def fonk1(b6):
    b1 = []
    for b2 in b6.split():
        if re.match(r'^.*@.*', b2):
            b2 = '<NAME/>'
        elif re.match(r'^.*http:
            b2 = '<LINK/>'
        b2 = b2.replace('&quot;', ' " ')
        b2 = b2.replace('&amp;', ' & ')
        b2 = b2.replace('&gt;', ' > ')
        b2 = b2.replace('&lt;', ' < ')
        b1.append(b2)
    return ' '.join(b1).strip()
def fonk2(b10, b11, b12):
    try:
        with open(b10, "r") as full_dataset, \
             open(b11, "w") as pos_dataset, \
             open(b12, "w") as neg_dataset:
            b3 = full_dataset.readlines()
            for line in tqdm(b3, b4 = "Processing Tweets"):
                b5 = line.split(",", 3)
                b6 = b5[3].strip()
                b7 = fonk1(b6) + '\n'
                if b5[1].strip() == '1':
                    pos_dataset.write(b7)
                else:
                    neg_dataset.write(b7)
    except IOError:
        print("Failed to open file")
if b8 = = "__main__":
    b9 = "http:
    b10 = "twitter-sentiment-dataset/sentiment-dataset.csv"
    b11 = "twitter-sentiment-dataset/tw-data.pos"
    b12 = "twitter-sentiment-dataset/tw-data.neg"
    fonk2(b10, b11, b12)