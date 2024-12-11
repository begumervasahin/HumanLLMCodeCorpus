
from nltk.stem import WordNetLemmatizer
import sys
import json
b1 = set(["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"])
def fonk1(wordlist):
    return [set(wordlist) - b1]
b2 = "b2.INDEX"
b3 = open(b2)
b4 = json.loads(b3.read())
b5 = WordNetLemmatizer()
def fonk2(set_list):
    if not set_list:
        return set()
    b6 = set_list[0]
    for s in set_list[1:]:
        b6 &= s
    return b6
b7 = sys.argv[1:]
b8 = []
b9 = []
print('_'*50 + "\nQuery Result\n" + '_'*50)
for w in b7:
    if w in b1:
        continue
    b10 = b5.lemmatize(w)
    try:
        b9.append(set(b4[b10]['postings']))
    except:
        print("No documents found matching query: " + ' '.join(b7))
        break
b11 = fonk2(b9)
if len(b11) > 0:
    print('\n'.join(list(b11)))