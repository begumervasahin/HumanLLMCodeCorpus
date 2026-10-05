import re
from tqdm import tqdm
try:
    b1 = open("twitter-sentiment-dataset/sentiment-dataset.csv", "r")
    b2 = open("twitter-sentiment-dataset/tw-data.pos", "w")
    b3 = open("twitter-sentiment-dataset/tw-data.neg", "w")
except IOError:
    print("Failed to open file")
    quit()
b4 = b1.readlines()
a1 = 0.0
for b5 in tqdm(b4):
    a1 += 1.0
    b5 = b5.split(",", 3)
    b6 = b5[3].strip()
    b7 = ''
    for b8 in b6.split():
        if re.match('^.*@.*', b8):
            b8 = '<NAME/>'
        if re.match('^.*http:
            b8 = '<LINK/>'
        b8 = b8.replace('&quot;', '\"')
        b8 = b8.replace('&amp;', '&')
        b8 = b8.replace('&gt;', '>')
        b8 = b8.replace('&lt;', '<')
        b7 = ' '.join([b7, b8])
    b6 = b7.strip() + '\n'
    if b5[1].strip() == '1':
        b2.write(b6)
    else:
        b3.write(b6)
b1.close()
b2.close()
b3.close()