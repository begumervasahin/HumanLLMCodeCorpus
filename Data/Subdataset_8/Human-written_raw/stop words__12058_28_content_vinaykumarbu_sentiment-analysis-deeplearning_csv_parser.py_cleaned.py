import re
from tqdm import tqdm
try:
    full_dataset = open("twitter-sentiment-dataset/sentiment-dataset.csv", "r")
    pos_dataset = open("twitter-sentiment-dataset/tw-data.pos", "w")
    neg_dataset = open("twitter-sentiment-dataset/tw-data.neg", "w")
except IOError:
    print "Failed to open file"
    quit()
csv_lines = full_dataset.readlines()
i = 0.0
for line in tqdm(csv_lines):
    i += 1.0
    line = line.split(",", 3)
    tweet = line[3].strip()
    new_tweet = ''
    for word in tweet.split():
        if re.match('^.*@.*', word):
            word = '<NAME/>'
        if re.match('^.*http:
            word = '<LINK/>'
        word = word.replace('
        word = word.replace('&quot;', ' \" ')
        word = word.replace('&amp;', ' & ')
        word = word.replace('&gt;', ' > ')
        word = word.replace('&lt;', ' < ')
        new_tweet = ' '.join([new_tweet, word])
    tweet = new_tweet.strip() + '\n'
    if line[1].strip() == '1':
        pos_dataset.write(tweet)
    else:
        neg_dataset.write(tweet)