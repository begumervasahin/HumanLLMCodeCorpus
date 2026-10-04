b1 = "Clyde D'Cruz"
b2 = "GPL"
import sys
import json
from nltk.stem import WordNetLemmatizer
b3 = {
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
    "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers",
    "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves",
    "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is",
    "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
    "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or",
    "because", "as", "until", "while", "of", "at", "by", "for", "with", "about",
    "against", "between", "into", "through", "during", "before", "after", "above",
    "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under",
    "again", "further", "then", "once", "here", "there", "when", "where", "why",
    "how", "all", "any", "both", "each", "few", "more", "most", "other", "some",
    "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very",
    "s", "t", "can", "will", "just", "don", "should", "now"
}
def fonk1(wordlist):
    return [word for word in wordlist if word not in b3]
def fonk2(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
def fonk3(word, b10):
    return b10.lemmatize(word)
def fonk4(sets):
    if not sets:
        return set()
    b4 = sets[0]
    for s in sets[1:]:
        b4 &= s
    return b4
def fonk5(b8, b9, b10):
    b5 = []
    for term in b8:
        if term in b3:
            continue
        b6 = fonk3(term, b10)
        try:
            b5.append(set(b9[b6]['postings']))
        except KeyError:
            print(f"No documents found matching query: {' '.join(b8)}")
            return
    b7 = fonk4(b5)
    if b7:
        print('\n'.join(b7))
    else:
        print(f"No documents found matching query: {' '.join(b8)}")
def fonk6():
    if len(sys.argv) < 2:
        print("Usage: python script.py <b8>")
        return
    b8 = sys.argv[1:]
    b9 = fonk2("INDEX_FILE.INDEX")
    b10 = WordNetLemmatizer()
    print('_' * 50 + "\nQuery Result\n" + '_' * 50)
    fonk5(b8, b9, b10)
if b11 = = "__main__":
    fonk6()