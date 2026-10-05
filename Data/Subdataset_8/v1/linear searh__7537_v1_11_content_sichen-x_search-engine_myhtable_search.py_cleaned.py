
from words import get_text, words
def myhtable_create_index(files):
    if len(files) <= 0:
        return None
    table = htable(4011)
    for i in range(len(files)):
        file_content = get_text(files[i])
        key_words = words(file_content)
        for word in key_words:
            htable_put(table, word, set([i]))
    return table
def myhtable_index_search(files, index, terms):
    if files is None or index is None or terms is None or \
            len(files) == 0 or len(index) == 0 or len(terms) == 0:
        return None
    ret_file_list = []
    list_of_sets = []
    for term in terms:
        value = htable_get(index, term)
        if value:
            list_of_sets.append(value)
        else:
            return None
    if len(list_of_sets) > 0:
        intersection_ids = set.intersection(*list_of_sets)
        for id in intersection_ids:
            ret_file_list.append(files[id])
    else:
        return None
    return ret_file_list
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