def get_text(file):
    pass
def words(text):
    pass
def linear_search(files, terms):
    if not files or not terms:
        return None
    result_files = []
    for file in files:
        file_content = get_text(file)
        if file_content:
            content_words = words(file_content)
            if all(term in content_words for term in terms):
                result_files.append(file)
    return result_files
if __name__ == "__main__":
    files = ["file1.txt", "file2.txt", "file3.txt"]
    search_terms = ["term1", "term2", "term3"]
    matching_files = linear_search(files, search_terms)
    print("Files containing all search terms:")
    for file in matching_files:
        print(file)