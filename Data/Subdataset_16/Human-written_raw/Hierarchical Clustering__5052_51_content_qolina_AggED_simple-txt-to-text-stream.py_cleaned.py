import codecs
from datetime import datetime, timedelta
import json
import os
import string
import sys
import time
def fonk1(line):
    b1 = line.strip().split("\t")
    b2 = b1[6]
    b3 = b1[8]
    if len(b2) != 18:
     	return ['', '', '', [], [], []]
    b4 = b1[9][:b1[9].find("2012")+4]
    b5 = datetime.strptime(b4, "%I:%M %p - %d %b %Y")
    b5 += timedelta(b6 = 7)
    b7 = b5.strftime("%a %b %d %H:%M:%S %Y")
    a1 = 0
    a2 = 0
    b8 = []
    b9 = []
    b10 = []
    for word in b3.split():
        if word[0] == "@":  b9.append(word[1:])
        if word[0] == "
        if word.startswith("http"): b10.append(word)
    b11 = [None]
    return [b7, b2, b3, b8, b9, b10, b11, a1, a2]
'''start main'''
if b12 = = "__main__":
	b13 = codecs.open(sys.argv[1], 'r', 'utf-8')
	b14 = codecs.open(sys.argv[2], 'w', 'utf-8')
        b15 = {}
	for line in b13:
		try:
			[tweet_gmttime, tweet_id, b3, b8, b9, b10, b11, a1, a2] = fonk1(line)
			try:
				b16 = time.strptime(tweet_gmttime.replace("+0000",''), '%a %b %d %H:%M:%S %Y')
			except:
				print "pb with tweet_gmttime", tweet_gmttime, line
				pass
			b17 = int(time.mktime(b16))
                        if b17 in b15:
                            b15[b17].append(str([b17, tweet_gmttime, tweet_id, b3, b8, b9, b10, b11, a1, a2]))
                        else:
                            b15[b17] = [str([b17, tweet_gmttime, tweet_id, b3, b8, b9, b10, b11, a1, a2])]
		except:
			pass
 	b13.close()
        for item in sorted(b15.items(), b18 = lambda a:a[0]):
            for subItem in item[1]:
                b14.write(subItem + "\n")
 	b14.close()