from collections import defaultdict
def get_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
def words(text):
    return text.lower().split()
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
        return None
    document_sets = [index.get(term) for term in terms if term in index]
    if len(document_sets) != len(terms):
        return None
    matching_ids = set.intersection(*document_sets)
    return [files[doc_id] for doc_id in matching_ids] if matching_ids else None
if __name__ == "__main__":
    files = ["file1.txt", "file2.txt", "file3.txt"]
    index = create_index(files)
    search_terms = ["term1", "term2"]
    result = index_search(files, index, search_terms)
    print("Matching files:", result)