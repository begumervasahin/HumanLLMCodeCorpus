from collections import defaultdict
from words import get_text, words
def create_index(files):
    if not files:
        return None
    index = defaultdict(set)
    for doc_id, file_path in enumerate(files):
        file_content = get_text(file_path)
        key_words = words(file_content)
        for word in key_words:
            index[word].add(doc_id)
    return index
def index_search(files, index, terms):
    if not files or not index or not terms:
        return None
    term_sets = [index.get(term) for term in terms]
    if not all(term_sets):
        return None
    intersection_sets = set.intersection(*term_sets)
    matching_files = [files[doc_id] for doc_id in intersection_sets]
    return matching_files