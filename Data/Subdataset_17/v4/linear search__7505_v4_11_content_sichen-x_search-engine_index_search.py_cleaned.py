from collections import defaultdict
from words import get_text, words
def create_index(files):
    if not files:
        return None
    index = defaultdict(set)
    for i, file in enumerate(files):
        file_content = get_text(file)
        key_words = words(file_content)
        for word in key_words:
            index[word].add(i)
    return index
def index_search(files, index, terms):
    if not files or not index or not terms:
        return None
    term_sets = [index.get(term) for term in terms if index.get(term)]
    if not term_sets:
        return None
    intersection_ids = set.intersection(*term_sets)
    return [files[doc_id] for doc_id in intersection_ids]