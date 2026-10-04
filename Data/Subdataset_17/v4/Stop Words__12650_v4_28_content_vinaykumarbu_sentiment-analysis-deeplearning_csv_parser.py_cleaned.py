import re
from tqdm import tqdm
dataset_url = "http:
input_file = "twitter-sentiment-dataset/sentiment-dataset.csv"
pos_output_file = "twitter-sentiment-dataset/tw-data.pos"
neg_output_file = "twitter-sentiment-dataset/tw-data.neg"
try:
    with open(input_file, "r") as full_dataset, \
         open(pos_output_file, "w") as pos_dataset, \
         open(neg_output_file, "w") as neg_dataset:
        csv_lines = full_dataset.readlines()
        for line in tqdm(csv_lines):
            line_parts = line.split(",", 3)
            tweet = line_parts[3].strip()
            new_tweet = []
            for word in tweet.split():
                if re.match(r'^.*@.*', word):
                    word = '<NAME/>'
                elif re.match(r'^.*http:
                    word = '<LINK/>'
                word = word.replace('&quot;', ' " ')
                word = word.replace('&amp;', ' & ')
                word = word.replace('&gt;', ' > ')
                word = word.replace('&lt;', ' < ')
                new_tweet.append(word)
            processed_tweet = ' '.join(new_tweet).strip() + '\n'
            if line_parts[1].strip() == '1':
                pos_dataset.write(processed_tweet)
            else:
                neg_dataset.write(processed_tweet)
except IOError:
    print("Failed to open file")