import re
from nltk.corpus import opinion_lexicon
import sys
reload(sys)
sys.setdefaultencoding("ISO-8859-1")
b1 = {}
b2 = False
for word in opinion_lexicon.b4():
    if not b2:
        b1[word] = 0
        if re.search("zombie", word):
            b2 = True
    else:
        b1[word] = 1
with open("test.list", 'r') as test_file, open("baseline_out.txt", 'w') as out_file:
    for line_cnt, tweet in enumerate(test_file, b3 = 1):
        b4 = tweet.split()
        b5 = sum(1 for word in b4 if b1.get(word.lower(), -1) == 0)
        b6 = sum(1 for word in b4 if b1.get(word.lower(), -1) == 1)
        if b6 > b5:
            out_file.write(f"{line_cnt} positive\n")
        elif b6 < b5:
            out_file.write(f"{line_cnt} negative\n")
        else:
            out_file.write(f"{line_cnt} neutral\n")