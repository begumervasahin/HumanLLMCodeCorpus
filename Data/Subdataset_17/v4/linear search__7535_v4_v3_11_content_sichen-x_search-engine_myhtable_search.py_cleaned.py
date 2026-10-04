
from words import get_text, words
def create_index(files):
    if not files:
        return None
    index_table = htable(4011)
    for file_index, file_name in enumerate(files):
        words_in_file = words(get_text(file_name))
        for word in words_in_file:
            existing_set = htable_get(index_table, word)
            if existing_set is None:
                existing_set = set()
            existing_set.add(file_index)
            htable_put(index_table, word, existing_set)
    return index_table
def search_index(files, index, terms):
    if not (files and index and terms):
        return None
    matching_files = []
    term_sets = []
    for term in terms:
        term_set = htable_get(index, term)
        if term_set is None:
            return None
        term_sets.append(term_set)
    intersection_ids = set.intersection(*term_sets)
    for file_index in intersection_ids:
        matching_files.append(files[file_index])
    return matching_files
files = ["file1.txt", "file2.txt", "file3.txt"]
index = create_index(files)
search_terms = ["term1", "term2", "term3"]
result = search_index(files, index, search_terms)
if result:
    print("Search Result:")
    for file in result:
        print(file)
else:
    print("No results found.")