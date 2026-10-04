from collections import defaultdict
from words import get_text, words
def build_index(files):
    if not files:
        return None
    index = defaultdict(set)
    for doc_id, file_path in enumerate(files):
        content = get_text(file_path)
        words_in_file = words(content)
        for word in words_in_file:
            index[word].add(doc_id)
    return index
def search_documents(files, index, terms):
    if not (files and index and terms):
        return None
    term_sets = [index.get(term) for term in terms]
    if any(term_set is None for term_set in term_sets):
        return None
    intersection_ids = set.intersection(*term_sets)
    return [files[doc_id] for doc_id in intersection_ids]
def main():
    files = ["file1.txt", "file2.txt", "file3.txt"]
    index = build_index(files)
    search_terms = ["term1", "term2"]
    result = search_documents(files, index, search_terms)
    print("Matching files:", result)
if __name__ == "__main__":
    main()