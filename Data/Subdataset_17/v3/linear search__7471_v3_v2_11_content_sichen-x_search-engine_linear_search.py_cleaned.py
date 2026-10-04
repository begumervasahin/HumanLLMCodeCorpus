def get_text(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except IOError:
        return None
def words(text):
    return text.split()
def linear_search(files, terms):
    if not files or not terms:
        return None
    matching_files = []
    for file_path in files:
        file_content = get_text(file_path)
        if file_content:
            file_words = words(file_content)
            if all(term in file_words for term in terms):
                matching_files.append(file_path)
    return matching_files
if __name__ == "__main__":
    files = ["file1.txt", "file2.txt", "file3.txt"]
    search_terms = ["term1", "term2", "term3"]
    result = linear_search(files, search_terms)
    print("Files containing all search terms:")
    if result:
        for file in result:
            print(file)
    else:
        print("No files contain all search terms.")