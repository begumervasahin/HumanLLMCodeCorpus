from words import get_text, words
def fonk1(files, terms):
    if files is None or terms is None or len(files) == 0 or len(terms) == 0:
        return None
    b1 = []
    for file in files:
        b2 = get_text(file)
        b3 = True
        b4 = words(b2)
        for term in terms:
            if term not in b4:
                b3 = False
                break
        if b3:
            b1.append(file)
    return b1