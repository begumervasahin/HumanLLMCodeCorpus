import codecs
from datetime import datetime, timedelta
import sys
import time
def fonk1(line):
    b1 = line.strip().split("\t")
    b2 = b1[6]
    b3 = b1[8]
    if len(b2) != 18:
        return ['', '', '', [], [], []]
    b4 = b1[9][:b1[9].find("2012")+4]
    b5 = datetime.strptime(b4, "%I:%M %p - %d %b %Y") + timedelta(hours=7)
    b6 = b5.strftime("%a %b %d %H:%M:%S %Y")
    a1 = 0
    a2 = 0
    b7 = []
    b8 = []
    b9 = []
    for word in b3.split():
        if word[0] == "@":
            b8.append(word[1:])
        elif word.startswith("http"):
            b9.append(word)
    b10 = [None]
    return [b6, b2, b3, b7, b8, b9, b10, a1, a2]
if b11 = = "__main__":
    b12 = sys.argv[1]
    b13 = sys.argv[2]
    with codecs.open(b12, 'r', 'utf-8') as file_timeordered_json_tweets:
        with codecs.open(b13, 'w', 'utf-8') as fout:
            b14 = {}
            for line in file_timeordered_json_tweets:
                try:
                    [tweet_gmttime, tweet_id, b3, b7, b8, b9, b10, a1, a2] = fonk1(line)
                    try:
                        b15 = time.strptime(tweet_gmttime.replace("+0000", ""), '%a %b %d %H:%M:%S %Y')
                    except Exception as e:
                        print("Problem with tweet_gmttime:", tweet_gmttime, line)
                        pass
                    b16 = int(time.mktime(b15))
                    if b16 in b14:
                        b14[b16].append(str([b16, tweet_gmttime, tweet_id, b3, b7, b8, b9, b10, a1, a2]))
                    else:
                        b14[b16] = [str([b16, tweet_gmttime, tweet_id, b3, b7, b8, b9, b10, a1, a2])]
                except Exception as e:
                    pass
            for item in sorted(b14.items(), b17 = lambda a: a[0]):
                for sub_item in item[1]:
                    fout.write(sub_item + "\n")