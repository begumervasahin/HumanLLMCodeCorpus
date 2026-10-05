from words import get_text, words
def linear_search(files, terms):
    if files == None or terms == None or len(files) == 0 or len(terms) == 0:
        return None
    ret_docs = []
    for file in files:
        file_content = get_text(file)
        all_terms_not_found = False
        words_in_file = words(file_content)
        for term in terms:
            if term not in words_in_file:
                all_terms_not_found = True
                break
        if all_terms_not_found is False:
            ret_docs.append(file)
    return ret_docs