from words import get_text, words
def linear_search(files, terms):
    if files is None or terms is None or len(files) == 0 or len(terms) == 0:
        return None
    matching_docs = []
    for file in files:
        file_content = get_text(file)
        all_terms_found = True
        words_in_file = words(file_content)
        for term in terms:
            if term not in words_in_file:
                all_terms_found = False
                break
        if all_terms_found:
            matching_docs.append(file)
    return matching_docs