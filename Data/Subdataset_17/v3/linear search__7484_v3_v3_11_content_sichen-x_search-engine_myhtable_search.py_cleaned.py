
from words import get_text, words
from htable import htable, htable_put, htable_get
def create_index(files):
    if not files:
        return None
    index_table = htable(4011)
    for file_index, file_name in enumerate(files):
        words_in_file = words(get_text(file_name))
        for word in words_in_file:
            current_set = htable_get(index_table, word)
            if current_set is None:
                htable_put(index_table, word, {file_index})
            else:
                current_set.add(file_index)
                htable_put(index_table, word, current_set)
    return index_table
def search_index(files, index, terms):
    if not (files and index and terms):
        return None
    term_sets = []
    for term in terms:
        term_set = htable_get(index, term)
        if term_set is None:
            return []
        term_sets.append(term_set)
    intersection_ids = set.intersection(*term_sets) if term_sets else set()
    matching_files = [files[file_index] for file_index in intersection_ids]
    return matching_files
if __name__ == "__main__":
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