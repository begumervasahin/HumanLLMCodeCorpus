from words import get_text, words
def myhtable_create_index(files):
    if not files:
        return None
    table = htable(4011)
    for doc_id, file_name in enumerate(files):
        file_content = get_text(file_name)
        key_words = words(file_content)
        for word in key_words:
            current_docs = htable_get(table, word)
            if current_docs is None:
                current_docs = set()
            current_docs.add(doc_id)
            htable_put(table, word, current_docs)
    return table
def myhtable_index_search(files, index, terms):
    if not files or not index or not terms:
        return None
    term_sets = []
    for term in terms:
        doc_ids = htable_get(index, term)
        if doc_ids:
            term_sets.append(doc_ids)
        else:
            return None
    if term_sets:
        common_doc_ids = set.intersection(*term_sets)
        result_files = [files[doc_id] for doc_id in common_doc_ids]
        return result_files if result_files else None
    return None
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