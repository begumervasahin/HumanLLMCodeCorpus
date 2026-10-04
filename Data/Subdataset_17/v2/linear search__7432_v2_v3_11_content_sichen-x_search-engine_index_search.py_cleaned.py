from collections import defaultdict
def get_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()
def words(text):
    return text.split()
def build_index(files):
    if not files:
        return None
    index = defaultdict(set)
    for doc_id, file_path in enumerate(files):
        words_in_file = words(get_text(file_path))
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
if __name__ == "__main__":
    files = ["file1.txt", "file2.txt", "file3.txt"]
    index = build_index(files)
    search_terms = ["term1", "term2"]
    result = search_documents(files, index, search_terms)
    print("Matching files:", result)