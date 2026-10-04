from collections import defaultdict
from words import get_text, words
def create_index(files):
    index = defaultdict(set)
    for doc_id, file_path in enumerate(files):
        file_content = get_text(file_path)
        key_words = words(file_content)
        for word in key_words:
            index[word].add(doc_id)
    return index
def index_search(files, index, terms):
    if not (files and index and terms):
        return []
    term_sets = [index.get(term, set()) for term in terms]
    if not term_sets:
        return []
    matching_ids = set.intersection(*term_sets)
    return [files[doc_id] for doc_id in matching_ids]
if __name__ == "__main__":
    files = ["file1.txt", "file2.txt", "file3.txt"]
    index = create_index(files)
    search_terms = ["term1", "term2"]
    results = index_search(files, index, search_terms)
    print("Matching files:", results)