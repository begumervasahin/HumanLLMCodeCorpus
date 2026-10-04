from collections import defaultdict
from words import get_text, words
def create_index(files):
    if not files:
        return None
    index = defaultdict(set)
    for doc_id, file in enumerate(files):
        content = get_text(file)
        key_words = words(content)
        for word in key_words:
            index[word].add(doc_id)
    return index
def index_search(files, index, terms):
    if not files or not index or not terms:
        return None
    matching_doc_ids = [index.get(term) for term in terms if term in index]
    if len(matching_doc_ids) != len(terms):
        return None
    intersecting_ids = set.intersection(*matching_doc_ids)
    return [files[doc_id] for doc_id in intersecting_ids]
