import sys
import json
from nltk.stem import WordNetLemmatizer
__author__ = "Clyde D'Cruz"
__license__ = "GPL"
ENGLISH_STOPWORDS = set([
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves",
    "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their",
    "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are",
    "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an",
    "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about",
    "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up",
    "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when",
    "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor",
    "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"
])
def remove_stopwords(wordlist):
    return [word for word in wordlist if word not in ENGLISH_STOPWORDS]
def set_list_intersection(set_list):
    if not set_list:
        return set()
    result = set_list[0]
    for s in set_list[1:]:
        result &= s
    return result
def main(query_terms):
    INDEX_FILE = "INDEX_FILE.INDEX"
    with open(INDEX_FILE, 'r') as index_file:
        index_dictionary = json.loads(index_file.read())
    lemmatizer = WordNetLemmatizer()
    normalized_query = []
    result_sets = []
    print('_' * 50 + "\nQuery Result \n" + '_' * 50)
    for w in query_terms:
        if w in ENGLISH_STOPWORDS:
            continue
        lem_word = lemmatizer.lemmatize(w)
        try:
            result_sets.append(set(index_dictionary[lem_word]['postings']))
        except KeyError:
            print(f"No documents found matching query: {' '.join(query_terms)}")
            return
    query_result = set_list_intersection(result_sets)
    if query_result:
        print('\n'.join(list(query_result)))
    else:
        print(f"No documents found matching query: {' '.join(query_terms)}")
if __name__ == "__main__":
    query_terms = sys.argv[1:]
    main(query_terms)