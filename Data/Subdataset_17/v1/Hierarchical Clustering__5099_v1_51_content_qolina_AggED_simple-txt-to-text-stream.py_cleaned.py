import codecs
from datetime import datetime, timedelta
import sys
import time
def parse_simple_text_tweet(line):
    arr = line.strip().split("\t")
    tid = arr[6]
    text = arr[8]
    if len(tid) != 18:
        return ['', '', '', [], [], [], [], 0, 0]
    date_str = arr[9][:arr[9].find("2012") + 4]
    try:
        date_temp = datetime.strptime(date_str, "%I:%M %p - %d %b %Y")
        date_temp += timedelta(hours=7)
        tweet_date = date_temp.strftime("%a %b %d %H:%M:%S %Y")
    except ValueError:
        return ['', '', '', [], [], [], [], 0, 0]
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
    nfollowers = 0
    nfriends = 0
    return [tweet_date, tid, text, hashtags, users, urls, media_urls, nfollowers, nfriends]
def main(input_file, output_file):
    tweet_ordered = {}
    with codecs.open(input_file, 'r', 'utf-8') as file_in:
        for line in file_in:
            tweet_data = parse_simple_text_tweet(line)
            if not tweet_data[0]:
                continue
            try:
                tweet_gmttime = tweet_data[0]
                c = time.strptime(tweet_gmttime, '%a %b %d %H:%M:%S %Y')
                tweet_unixtime = int(time.mktime(c))
                tweet_record = str([tweet_unixtime] + tweet_data)
                if tweet_unixtime in tweet_ordered:
                    tweet_ordered[tweet_unixtime].append(tweet_record)
                else:
                    tweet_ordered[tweet_unixtime] = [tweet_record]
            except Exception as e:
                print(f"Problem with tweet_gmttime: {tweet_gmttime}, line: {line.strip()}")
                print(e)
    with codecs.open(output_file, 'w', 'utf-8') as file_out:
        for item in sorted(tweet_ordered.items(), key=lambda a: a[0]):
            for sub_item in item[1]:
                file_out.write(sub_item + "\n")
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)