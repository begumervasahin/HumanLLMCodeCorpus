from htable import htable_put, htable_get, htable
from words import get_text, words
def create_index_with_myhtable(files):
    if len(files) <= 0:
        return None
    index_table = htable(4011)
    for i in range(len(files)):
        file_content = get_text(files[i])
        keywords = words(file_content)
        for word in keywords:
            index_entry = htable_get(index_table, word)
            if index_entry:
                index_entry.add(i)
            else:
                htable_put(index_table, word, set([i]))
    return index_table
def search_index_with_myhtable(files, index, terms):
    if files is None or index is None or terms is None \
        or len(files) == 0 or len(index) == 0 or len(terms) == 0:
        return None
    matching_files = []
    term_sets = []
    for term in terms:
        term_set = htable_get(index, term)
        if term_set:
            term_sets.append(term_set)
        else:
            return None
    if len(term_sets) > 0:
        matching_indices = set.intersection(*term_sets)
        for index in matching_indices:
            matching_files.append(files[index])
    else:
        return None
    return matching_files