import re
from nltk.corpus import opinion_lexicon
b1 = set(opinion_lexicon.b5())
b2 = {}
b3 = False
for word in b1:
    if not b3:
        b2[word] = 0
        if re.search("zombie", word):
            b3 = True
    else:
        b2[word] = 1
with open("test.list", 'r') as test_file, open("baseline_out.txt", 'w') as out_file:
    for line_cnt, tweet in enumerate(test_file, b4 = 1):
        b5 = tweet.split()
        b6 = sum(1 for word in b5 if b2.get(word.lower(), -1) == 0)
        b7 = sum(1 for word in b5 if b2.get(word.lower(), -1) == 1)
        if b7 > b6:
            out_file.write(f"{line_cnt} positive\n")
        elif b7 < b6:
            out_file.write(f"{line_cnt} negative\n")
        else:
            out_file.write(f"{line_cnt} neutral\n")