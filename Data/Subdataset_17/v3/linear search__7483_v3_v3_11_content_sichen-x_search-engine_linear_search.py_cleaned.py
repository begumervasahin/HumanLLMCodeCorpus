import os
def get_text(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None
def extract_words(text):
    return text.split()
def linear_search(files, search_terms):
    if not files or not search_terms:
        return None
    matching_files = []
    for file_path in files:
        file_content = get_text(file_path)
        if file_content:
            file_words = extract_words(file_content)
            if all(term in file_words for term in search_terms):
                matching_files.append(file_path)
    return matching_files
def main():
    files = ["file1.txt", "file2.txt", "file3.txt"]
    search_terms = ["term1", "term2", "term3"]
    result = linear_search(files, search_terms)
    if result:
        print("Files containing all search terms:")
        for file_path in result:
            print(file_path)
    else:
        print("No files found containing all search terms.")
if __name__ == "__main__":
    main()