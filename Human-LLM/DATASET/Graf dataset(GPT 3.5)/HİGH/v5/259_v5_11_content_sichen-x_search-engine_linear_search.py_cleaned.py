from words import get_text, words
def fonk1(files, terms):
    if not files or not terms:
        return None
    b1 = []
    for file in files:
        b2 = get_text(file)
        b3 = words(b2)
        if all(term in b3 for term in terms):
            b1.append(file)
    return b1