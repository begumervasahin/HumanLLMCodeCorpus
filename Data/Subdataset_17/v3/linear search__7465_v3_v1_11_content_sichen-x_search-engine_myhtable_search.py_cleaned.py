
from htable import htable, htable_put, htable_get
from words import get_text, words
def myhtable_create_index(files):
    if not files:
        return None
    table = htable(4011)
    for i, file in enumerate(files):
        file_content = get_text(file)
        key_words = words(file_content)
        for word in key_words:
            existing_set = htable_get(table, word)
            if existing_set is None:
                htable_put(table, word, {i})
            else:
                existing_set.add(i)
                htable_put(table, word, existing_set)
    return table
def myhtable_index_search(files, index, terms):
    if not files or not index or not terms:
        return None
    list_of_sets = []
    for term in terms:
        value = htable_get(index, term)
        if value:
            list_of_sets.append(value)
        else:
            return None
    if not list_of_sets:
        return None
    intersection_ids = set.intersection(*list_of_sets)
    ret_file_list = [files[id] for id in intersection_ids]
    return ret_file_list
if __name__ == "__main__":
    files = ["file1.txt", "file2.txt", "file3.txt"]
    index = myhtable_create_index(files)
    search_terms = ["term1", "term2", "term3"]
    result = myhtable_index_search(files, index, search_terms)
    if result:
        print("Search Result:")
        for file in result:
            print(file)
    else:
        print("No results found.")