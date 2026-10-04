__author__ = "Clyde D'Cruz"
__license__ = "GPL"
import sys
import json
from nltk.stem import WordNetLemmatizer
ENGLISH_STOPWORDS = {
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
def remove_stopwords(wordlist):
    return [word for word in wordlist if word not in ENGLISH_STOPWORDS]
def load_index(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
def lemmatize_word(word, lemmatizer):
    return lemmatizer.lemmatize(word)
def find_intersection(sets):
    if not sets:
        return set()
    result = sets[0]
    for s in sets[1:]:
        result &= s
    return result
def process_query(query_terms, index, lemmatizer):
    result_sets = []
    for term in query_terms:
        if term in ENGLISH_STOPWORDS:
            continue
        lemmatized_term = lemmatize_word(term, lemmatizer)
        try:
            result_sets.append(set(index[lemmatized_term]['postings']))
        except KeyError:
            print(f"No documents found matching query: {' '.join(query_terms)}")
            return
    query_result = find_intersection(result_sets)
    if query_result:
        print('\n'.join(query_result))
    else:
        print(f"No documents found matching query: {' '.join(query_terms)}")
def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <query_terms>")
        return
    query_terms = sys.argv[1:]
    index = load_index("INDEX_FILE.INDEX")
    lemmatizer = WordNetLemmatizer()
    print('_' * 50 + "\nQuery Result\n" + '_' * 50)
    process_query(query_terms, index, lemmatizer)
if __name__ == "__main__":
    main()