from nltk.stem import WordNetLemmatizer
import sys
import json
b1 = "Clyde D'Cruz"
b2 = "GPL"
b3 = {
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves",
    "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their",
    "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are",
    "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an",
    "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about",
    "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up",
    "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when",
    "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor",
    "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should",
    "now"
}
def fonk1(wordlist):
    return [word for word in wordlist if word not in b3]
b4 = "b4.INDEX"
with open(b4, 'r') as index_file:
    b5 = json.load(index_file)
b6 = WordNetLemmatizer()
def fonk2(set_list):
    if not set_list:
        return set()
    b7 = set_list[0]
    for s in set_list[1:]:
        b7 &= s
    return b7
b8 = sys.argv[1:]
b9 = fonk1(b8)
b10 = []
print('_' * 50 + "\nQuery Result \n" + '_' * 50)
for word in b9:
    b11 = b6.lemmatize(word)
    try:
        b10.append(set(b5[b11]['postings']))
    except KeyError:
        print("No documents found matching query : " + ' '.join(b8))
        break
b12 = fonk2(b10)
if b12:
    print('\n'.join(map(str, b12)))