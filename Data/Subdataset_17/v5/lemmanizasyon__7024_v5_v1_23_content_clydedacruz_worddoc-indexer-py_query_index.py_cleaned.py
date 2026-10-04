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
    "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no",
    "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don",
    "should", "now"
])
def remove_stopwords(wordlist):
    return [word for word in wordlist if word not in ENGLISH_STOPWORDS]
def load_index(file_path):
    with open(file_path, 'r') as index_file:
        return json.load(index_file)
def set_list_intersection(set_list):
    if not set_list:
        return set()
    result = set_list[0]
    for s in set_list[1:]:
        result &= s
    return result
def process_query(query_terms, index_dict, lemmatizer):
    normalized_query = remove_stopwords(query_terms)
    result_sets = []
    for word in normalized_query:
        lem_word = lemmatizer.lemmatize(word)
        try:
            result_sets.append(set(index_dict[lem_word]['postings']))
        except KeyError:
            return f"No documents found matching query: {' '.join(query_terms)}"
    query_result = set_list_intersection(result_sets)
    if query_result:
        return '\n'.join(query_result)
    else:
        return "No matching documents found."
def main():
    index_file = "INDEX_FILE.INDEX"
    index_dict = load_index(index_file)
    lemmatizer = WordNetLemmatizer()
    query_terms = sys.argv[1:]
    print('_' * 50 + "\nQuery Result \n" + '_' * 50)
    result = process_query(query_terms, index_dict, lemmatizer)
    print(result)
if __name__ == "__main__":
    main()