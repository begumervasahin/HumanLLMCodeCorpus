import sys
import json
from nltk.stem import WordNetLemmatizer
b1 = "Clyde D'Cruz"
b2 = "GPL"
b3 = {
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
    "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself",
    "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which",
    "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be",
    "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an",
    "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for",
    "with", "about", "against", "between", "into", "through", "during", "before", "after",
    "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under",
    "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all",
    "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not",
    "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don",
    "should", "now"
}
def fonk1(wordlist):
    return [word for word in wordlist if word.lower() not in b3]
def fonk2(set_list):
    if not set_list:
        return set()
    b4 = set_list[0]
    for s in set_list[1:]:
        b4 &= s
    return b4
def fonk3(b13):
    b5 = "b5.INDEX"
    try:
        with open(b5, 'r') as index_file:
            b6 = json.load(index_file)
    except FileNotFoundError:
        print(f"Index file {b5} not found.")
        return
    except json.JSONDecodeError:
        print(f"Error decoding JSON from index file {b5}.")
        return
    b7 = WordNetLemmatizer()
    b8 = fonk1(b13)
    b9 = []
    print('_' * 50 + "\nQuery Result\n" + '_' * 50)
    for word in b8:
        b10 = b7.lemmatize(word.lower())
        if b10 in b6:
            b9.append(set(b6[b10]['postings']))
        else:
            print(f"No documents found matching query: {' '.join(b13)}")
            return
    b11 = fonk2(b9)
    if b11:
        print('\n'.join(b11))
    else:
        print(f"No documents found matching query: {' '.join(b13)}")
if b12 = = "__main__":
    if len(sys.argv) > 1:
        b13 = sys.argv[1:]
        fonk3(b13)
    else:
        print("Please provide query terms.")