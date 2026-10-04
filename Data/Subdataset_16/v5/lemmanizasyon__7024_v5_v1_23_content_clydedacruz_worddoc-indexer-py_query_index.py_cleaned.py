import sys
import json
from nltk.stem import WordNetLemmatizer
b1 = "Clyde D'Cruz"
b2 = "GPL"
b3 = set([
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves",
    "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their",
    "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are",
    "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an",
    "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about",
    "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up",
    "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when",
    "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no",
    "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don",
    "should", "now"
])
def fonk1(wordlist):
    return [word for word in wordlist if word not in b3]
def fonk2(file_path):
    with open(file_path, 'r') as b9:
        return json.load(b9)
def fonk3(set_list):
    if not set_list:
        return set()
    b4 = set_list[0]
    for s in set_list[1:]:
        b4 &= s
    return b4
def fonk4(b12, b10, b11):
    b5 = fonk1(b12)
    b6 = []
    for word in b5:
        b7 = b11.lemmatize(word)
        try:
            b6.append(set(b10[b7]['postings']))
        except KeyError:
            return f"No documents found matching query: {' '.join(b12)}"
    b8 = fonk3(b6)
    if b8:
        return '\n'.join(b8)
    else:
        return "No matching documents found."
def fonk5():
    b9 = "INDEX_FILE.INDEX"
    b10 = fonk2(b9)
    b11 = WordNetLemmatizer()
    b12 = sys.argv[1:]
    print('_' * 50 + "\nQuery Result \n" + '_' * 50)
    b4 = fonk4(b12, b10, b11)
    print(b4)
if b13 = = "__main__":
    fonk5()