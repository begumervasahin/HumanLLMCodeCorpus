from words import get_text, words
def linear_search(files, terms):
    if not files or not terms:
        return None
    matching_docs = []
    for file in files:
        file_content = get_text(file)
        words_in_file = words(file_content)
        if all(term in words_in_file for term in terms):
            matching_docs.append(file)
    return matching_docs