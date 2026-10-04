from collections import defaultdict
from words import get_text, words
def create_index(files):
    if not files:
        return None
    index = defaultdict(set)
    for doc_id, file_path in enumerate(files):
        file_content = get_text(file_path)
        key_words = words(file_content)
        for word in key_words:
            index[word].add(doc_id)
    return index
def index_search(files, index, terms):
    if not (files and index and terms):
        return None
    doc_id_sets = [index.get(term) for term in terms if term in index]
    if not doc_id_sets or len(doc_id_sets) != len(terms):
        return None
    matching_doc_ids = set.intersection(*doc_id_sets)
    return [files[doc_id] for doc_id in matching_doc_ids]
if __name__ == "__main__":
    files = ["file1.txt", "file2.txt", "file3.txt"]
    index = create_index(files)
    search_terms = ["term1", "term2"]
    result = index_search(files, index, search_terms)
    print("Matching files:", result)