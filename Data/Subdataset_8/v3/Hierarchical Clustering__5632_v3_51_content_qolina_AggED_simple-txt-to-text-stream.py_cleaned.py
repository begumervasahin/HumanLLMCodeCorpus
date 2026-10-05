import codecs
from datetime import datetime, timedelta
import sys
import time
def parse_simple_text_tweet(line):
    arr = line.strip().split("\t")
    tid = arr[6]
    text = arr[8]
    if len(tid) != 18:
        return ['', '', '', [], [], []]
    date1 = arr[9][:arr[9].find("2012")+4]
    date_temp = datetime.strptime(date1, "%I:%M %p - %d %b %Y") + timedelta(hours=7)
    date2 = date_temp.strftime("%a %b %d %H:%M:%S %Y")
    nfollowers = 0
    nfriends = 0
    hashtags = []
    users = []
    urls = []
    for word in text.split():
        if word.startswith("@"):
            users.append(word[1:])
        elif word.startswith("
            hashtags.append(word[1:])
        elif word.startswith("http"):
            urls.append(word)
    media_urls = [None]
    return [date2, tid, text, hashtags, users, urls, media_urls, nfollowers, nfriends]
if __name__ == "__main__":
    with codecs.open(sys.argv[1], 'r', 'utf-8') as file_timeordered_json_tweets:
        with codecs.open(sys.argv[2], 'w', 'utf-8') as fout:
            tweet_ordered = {}
            for line in file_timeordered_json_tweets:
                try:
                    [tweet_gmttime, tweet_id, text, hashtags, users, urls, media_urls, nfollowers, nfriends] = parse_simple_text_tweet(line)
                    try:
                        c = time.strptime(tweet_gmttime.replace("+0000", ""), '%a %b %d %H:%M:%S %Y')
                    except Exception as e:
                        print("Problem with tweet_gmttime:", tweet_gmttime, line)
                        pass
                    tweet_unixtime = int(time.mktime(c))
                    if tweet_unixtime in tweet_ordered:
                        tweet_ordered[tweet_unixtime].append(str([tweet_unixtime, tweet_gmttime, tweet_id, text, hashtags, users, urls, media_urls, nfollowers, nfriends]))
                    else:
                        tweet_ordered[tweet_unixtime] = [str([tweet_unixtime, tweet_gmttime, tweet_id, text, hashtags, users, urls, media_urls, nfollowers, nfriends])]
                except Exception as e:
                    pass
            for item in sorted(tweet_ordered.items(), key=lambda a: a[0]):
                for sub_item in item[1]:
                    fout.write(sub_item + "\n")