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
    list_of_sets = []
    for term in terms:
        value_set = index.get(term)
        if value_set:
            list_of_sets.append(value_set)
        else:
            return None
    if list_of_sets:
        intersection_ids = set.intersection(*list_of_sets)
        return [files[id] for id in intersection_ids]
    return None
