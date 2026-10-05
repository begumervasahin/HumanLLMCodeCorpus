import codecs
from datetime import datetime, timedelta
import sys
import time
def parse_simple_text_tweet(line):
    arr = line.strip().split("\t")
    tweet_id = arr[6]
    text = arr[8]
    if len(tweet_id) != 18:
        return ['', '', '', [], [], []]
    tweet_time_str = arr[9][:arr[9].find("2012")+4]
    tweet_time_utc = datetime.strptime(tweet_time_str, "%I:%M %p - %d %b %Y") + timedelta(hours=7)
    tweet_time = tweet_time_utc.strftime("%a %b %d %H:%M:%S %Y")
    nfollowers = 0
    nfriends = 0
    hashtags = []
    users = []
    urls = []
    for word in text.split():
        if word.startswith("@"):
            users.append(word[1:])
        elif word.startswith("http"):
            urls.append(word)
    media_urls = [None]
    return [tweet_time, tweet_id, text, hashtags, users, urls, media_urls, nfollowers, nfriends]
if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    with codecs.open(input_file, 'r', 'utf-8') as file_timeordered_json_tweets:
        with codecs.open(output_file, 'w', 'utf-8') as fout:
            tweet_ordered = {}
            for line in file_timeordered_json_tweets:
                try:
                    [tweet_gmttime, tweet_id, text, hashtags, users, urls, media_urls, nfollowers, nfriends] = parse_simple_text_tweet(line)
                    try:
                        tweet_time_struct = time.strptime(tweet_gmttime.replace("+0000", ""), '%a %b %d %H:%M:%S %Y')
                    except Exception as e:
                        print("Error parsing tweet time:", tweet_gmttime, line)
                        pass
                    tweet_unixtime = int(time.mktime(tweet_time_struct))
                    if tweet_unixtime in tweet_ordered:
                        tweet_ordered[tweet_unixtime].append(str([tweet_unixtime, tweet_gmttime, tweet_id, text, hashtags, users, urls, media_urls, nfollowers, nfriends]))
                    else:
                        tweet_ordered[tweet_unixtime] = [str([tweet_unixtime, tweet_gmttime, tweet_id, text, hashtags, users, urls, media_urls, nfollowers, nfriends])]
                except Exception as e:
                    pass
            for timestamp, tweets in sorted(tweet_ordered.items()):
                for tweet in tweets:
                    fout.write(tweet + "\n")