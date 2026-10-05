
from nltk.stem import WordNetLemmatizer
import sys
import json
b1 = {
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your",
    "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she",
    "her", "hers", "herself", "it", "its", "itself", "they", "them", "their",
    "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
    "these", "those", "am", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an",
    "the", "and", "but", "if", "or", "because", "as", "until", "while", "of",
    "at", "by", "for", "with", "about", "against", "between", "into", "through",
    "during", "before", "after", "above", "below", "to", "from", "up", "down",
    "in", "out", "on", "off", "over", "under", "again", "further", "then",
    "once", "here", "there", "when", "where", "why", "how", "all", "any",
    "both", "each", "few", "more", "most", "other", "some", "such", "no",
    "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s",
    "t", "can", "will", "just", "don", "should", "now"
}
def fonk1(wordlist):
    return [word for word in wordlist if word not in b1]
b2 = "b2.INDEX"
with open(b2) as index_file:
    b3 = json.load(index_file)
b4 = WordNetLemmatizer()
def fonk2(set_list):
    if not set_list:
        return set()
    b5 = set_list[0]
    for s in set_list[1:]:
        b5 &= s
    return b5
b6 = sys.argv[1:]
print('_' * 50 + "\nQuery Result\n" + '_' * 50)
b7 = []
for term in b6:
    if term in b1:
        continue
    b8 = b4.lemmatize(term)
    try:
        b7.append(set(b3[b8]['postings']))
    except KeyError:
        print("No documents found matching query: " + ' '.join(b6))
        break
b9 = fonk2(b7)
if b9:
    print('\n'.join(map(str, b9)))