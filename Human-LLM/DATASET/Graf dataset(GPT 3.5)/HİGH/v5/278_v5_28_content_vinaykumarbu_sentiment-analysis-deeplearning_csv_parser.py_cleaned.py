import re
from tqdm import tqdm
b1 = "twitter-sentiment-dataset/sentiment-dataset.csv"
b2 = "twitter-sentiment-dataset/tw-data.pos"
b3 = "twitter-sentiment-dataset/tw-data.neg"
try:
    b4 = open(b1, "r")
    b5 = open(b2, "w")
    b6 = open(b3, "w")
except IOError:
    print("Failed to open file")
    quit()
b7 = b4.readlines()
for line in tqdm(b7):
    b8 = line.split(",", 3)
    b9 = b8[3].strip()
    b10 = ''
    for b11 in b9.split():
        if re.match('^.*@.*', b11):
            b11 = '<NAME/>'
        if re.match('^.*http:
            b11 = '<LINK/>'
        b11 = b11.replace('&quot;', '\"').replace('&amp;', '&').replace('&gt;', '>').replace('&lt;', '<')
        b10 = ' '.join([b10, b11])
    b10 = b10.strip() + '\n'
    if b8[1].strip() == '1':
        b5.write(b10)
    else:
        b6.write(b10)
b4.close()
b5.close()
b6.close()