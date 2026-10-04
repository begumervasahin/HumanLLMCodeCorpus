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
    matching_doc_ids_sets = []
    for term in terms:
        doc_ids = index.get(term)
        if doc_ids:
            matching_doc_ids_sets.append(doc_ids)
        else:
            return None
    if matching_doc_ids_sets:
        intersecting_ids = set.intersection(*matching_doc_ids_sets)
        return [files[doc_id] for doc_id in intersecting_ids]
    return None
