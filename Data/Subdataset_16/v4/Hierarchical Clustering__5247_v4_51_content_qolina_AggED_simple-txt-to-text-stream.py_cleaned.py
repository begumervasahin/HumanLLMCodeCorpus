import codecs
from datetime import datetime, timedelta
import sys
import time
def fonk1(line):
    b1 = line.strip().split("\t")
    if len(b1) <= 9 or len(b1[6]) != 18:
        return ['', '', '', [], [], [], [], 0, 0]
    b2 = b1[6]
    b3 = b1[8]
    b4 = b1[9][:b1[9].find("2012") + 4]
    try:
        b5 = datetime.strptime(b4, "%I:%M %p - %d %b %Y")
        b6 = b5 + timedelta(hours=7)
        b7 = b6.strftime("%a %b %d %H:%M:%S %Y")
    except ValueError:
        return ['', '', '', [], [], [], [], 0, 0]
    hashtags, users, b8 = fonk2(b3)
    b9 = [None]
    nfollowers, b10 = 0, 0
    return [b7, b2, b3, hashtags, users, b8, b9, nfollowers, b10]
def fonk2(b3):
    hashtags, users, b8 = [], [], []
    for word in b3.split():
        if word.startswith("@"):
            users.append(word[1:])
        elif word.startswith("
            hashtags.append(word[1:])
        elif word.startswith("http"):
            b8.append(word)
    return hashtags, users, b8
def fonk3(b17, b18):
    b11 = {}
    with codecs.open(b17, 'r', 'utf-8') as file_in:
        for line in file_in:
            b12 = fonk1(line)
            if not b12[0]:
                continue
            try:
                b13 = fonk4(b12[0])
            except Exception as e:
                print(f"Error parsing time: {b12[0]} | Line: {line.strip()}\n{e}")
                continue
            b14 = str([b13] + b12)
            if b13 in b11:
                b11[b13].append(b14)
            else:
                b11[b13] = [b14]
    fonk5(b11, b18)
def fonk4(tweet_gmttime):
    b15 = time.strptime(tweet_gmttime, '%a %b %d %H:%M:%S %Y')
    return int(time.mktime(b15))
def fonk5(b11, b18):
    with codecs.open(b18, 'w', 'utf-8') as file_out:
        for timestamp, tweet_list in sorted(b11.items()):
            for tweet in tweet_list:
                file_out.write(tweet + "\n")
if b16 = = "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <b17> <b18>")
        sys.exit(1)
    b17 = sys.argv[1]
    b18 = sys.argv[2]
    fonk3(b17, b18)