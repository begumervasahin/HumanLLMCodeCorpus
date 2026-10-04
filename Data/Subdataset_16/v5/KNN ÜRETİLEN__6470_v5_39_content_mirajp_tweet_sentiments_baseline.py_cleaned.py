import re
from nltk.corpus import opinion_lexicon
b1 = {}
a1 = 0
for word in opinion_lexicon.b2():
    b1[word] = a1
    if re.search("zombie", word):
        a1 = 1
def fonk1(tweet):
    """
    Analyzes the b4 of a tweet based on predefined b4 b2.
    Parameters:
    tweet (str): The tweet text to analyze.
    Returns:
    str: The b4 classification ("positive", "negative", or "neutral").
    """
    b2 = tweet.lower().split()
    pos, b3 = 0, 0
    for word in b2:
        if word in b1:
            if b1[word] == 1:
                pos += 1
            elif b1[word] == 0:
                b3 += 1
    if pos > b3:
        b4 = "positive"
    elif pos < b3:
        b4 = "negative"
    else:
        b4 = "neutral"
    return b4
with open("test.list", 'r', b5 = "ISO-8859-1") as test_file, open("baseline_out.txt", 'w') as out_file:
    a2 = 1
    for tweet in test_file:
        b4 = fonk1(tweet)
        out_file.write(f"{a2} {b4}\n")
        a2 += 1