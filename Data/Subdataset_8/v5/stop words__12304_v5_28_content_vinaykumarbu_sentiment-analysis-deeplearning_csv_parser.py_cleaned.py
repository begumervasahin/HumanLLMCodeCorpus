import re
from tqdm import tqdm
input_file_path = "twitter-sentiment-dataset/sentiment-dataset.csv"
positive_output_file_path = "twitter-sentiment-dataset/tw-data.pos"
negative_output_file_path = "twitter-sentiment-dataset/tw-data.neg"
try:
    input_file = open(input_file_path, "r")
    positive_output_file = open(positive_output_file_path, "w")
    negative_output_file = open(negative_output_file_path, "w")
except IOError:
    print("Failed to open file")
    quit()
csv_lines = input_file.readlines()
for line in tqdm(csv_lines):
    parts = line.split(",", 3)
    tweet = parts[3].strip()
    processed_tweet = ''
    for word in tweet.split():
        if re.match('^.*@.*', word):
            word = '<NAME/>'
        if re.match('^.*http:
            word = '<LINK/>'
        word = word.replace('&quot;', '\"').replace('&amp;', '&').replace('&gt;', '>').replace('&lt;', '<')
        processed_tweet = ' '.join([processed_tweet, word])
    processed_tweet = processed_tweet.strip() + '\n'
    if parts[1].strip() == '1':
        positive_output_file.write(processed_tweet)
    else:
        negative_output_file.write(processed_tweet)
input_file.close()
positive_output_file.close()
negative_output_file.close()