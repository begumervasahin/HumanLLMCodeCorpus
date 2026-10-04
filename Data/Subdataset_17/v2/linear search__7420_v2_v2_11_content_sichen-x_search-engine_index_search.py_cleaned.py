from collections import defaultdict
def get_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
def words(text):
    return text.lower().split()
def create_index(files):
    if not files:
        return None
    index = defaultdict(set)
    for i, file_path in enumerate(files):
        file_content = get_text(file_path)
        key_words = words(file_content)
        for word in key_words:
            index[word].add(i)
    return index
def index_search(files, index, terms):
    if not (files and index and terms):
        return None
    list_of_sets = [index.get(term) for term in terms if index.get(term)]
    if len(list_of_sets) != len(terms):
        return None
    intersection_ids = set.intersection(*list_of_sets)
    return [files[id] for id in intersection_ids] if intersection_ids else None
if __name__ == "__main__":
    files = ["file1.txt", "file2.txt", "file3.txt"]
    index = create_index(files)
    search_terms = ["term1", "term2"]
    result = index_search(files, index, search_terms)
    print("Matching files:", result)