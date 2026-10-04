from collections import defaultdict
def get_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()
def words(text):
    return text.split()
def build_index(files):
    index = defaultdict(set)
    for doc_id, file_path in enumerate(files):
        file_content = get_text(file_path)
        words_in_file = words(file_content)
        for word in words_in_file:
            index[word].add(doc_id)
    return index
def search_documents(files, index, terms):
    if not terms:
        return []
    term_sets = [index.get(term) for term in terms if index.get(term)]
    if not term_sets:
        return []
    intersection_ids = set.intersection(*term_sets)
    return [files[doc_id] for doc_id in intersection_ids]
def main():
    files = ["file1.txt", "file2.txt", "file3.txt"]
    index = build_index(files)
    search_terms = ["term1", "term2"]
    matching_files = search_documents(files, index, search_terms)
    print("Matching files:", matching_files)
if __name__ == "__main__":
    main()