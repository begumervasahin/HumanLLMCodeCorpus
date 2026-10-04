
def get_text(file):
    pass
def words(text):
    pass
def linear_search(files, terms):
    if files is None or terms is None or len(files) == 0 or len(terms) == 0:
        return None
    ret_docs = []
    for file in files:
        file_content = get_text(file)
        if file_content is not None:
            all_terms_found = all(term in words(file_content) for term in terms)
            if all_terms_found:
                ret_docs.append(file)
    return ret_docs
if __name__ == "__main__":
    files = ["file1.txt", "file2.txt", "file3.txt"]
    search_terms = ["term1", "term2", "term3"]
    result = linear_search(files, search_terms)
    print("Files containing all search terms:")
    for file in result:
        print(file)