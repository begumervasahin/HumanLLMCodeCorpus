import codecs
from datetime import datetime, timedelta
import sys
import time
def parse_tweet(line):
    fields = line.strip().split("\t")
    if len(fields) <= 9 or len(fields[6]) != 18:
        return ['', '', '', [], [], [], [], 0, 0]
    tweet_id = fields[6]
    text = fields[8]
    date_str = fields[9][:fields[9].find("2012") + 4]
    try:
        parsed_date = datetime.strptime(date_str, "%I:%M %p - %d %b %Y")
        adjusted_date = parsed_date + timedelta(hours=7)
        formatted_date = adjusted_date.strftime("%a %b %d %H:%M:%S %Y")
    except ValueError:
        return ['', '', '', [], [], [], [], 0, 0]
    hashtags, users, urls = [], [], []
    for word in text.split():
        if word.startswith("@"):
            users.append(word[1:])
        elif word.startswith("
            hashtags.append(word[1:])
        elif word.startswith("http"):
            urls.append(word)
    media_urls = [None]
    nfollowers, nfriends = 0, 0
    return [formatted_date, tweet_id, text, hashtags, users, urls, media_urls, nfollowers, nfriends]
def process_tweets(input_file, output_file):
    tweets_by_time = {}
    with codecs.open(input_file, 'r', 'utf-8') as file_in:
        for line in file_in:
            tweet_data = parse_tweet(line)
            if not tweet_data[0]:
                continue
            tweet_gmttime = tweet_data[0]
            try:
                time_struct = time.strptime(tweet_gmttime, '%a %b %d %H:%M:%S %Y')
                tweet_unixtime = int(time.mktime(time_struct))
            except Exception as e:
                print(f"Error parsing time: {tweet_gmttime} | Line: {line.strip()}\n{e}")
                continue
            tweet_record = str([tweet_unixtime] + tweet_data)
            if tweet_unixtime in tweets_by_time:
                tweets_by_time[tweet_unixtime].append(tweet_record)
            else:
                tweets_by_time[tweet_unixtime] = [tweet_record]
    with codecs.open(output_file, 'w', 'utf-8') as file_out:
        for timestamp, tweet_list in sorted(tweets_by_time.items()):
            for tweet in tweet_list:
                file_out.write(tweet + "\n")
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    process_tweets(input_file, output_file)