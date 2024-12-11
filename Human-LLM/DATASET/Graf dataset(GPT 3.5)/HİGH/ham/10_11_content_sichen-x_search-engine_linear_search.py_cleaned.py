from words import get_text, words
def fonk1(b1, terms):
    if b1 = = None or terms == None or len(b1) == 0 or len(terms) == 0:
        return None
    b2 = []
    for file in b1:
        b3 = get_text(file)
        b4 = False
        b5 = words(b3)
        for term in terms:
            if term not in b5:
                b4 = True
                break
        if b4 is False:
            b2.append(file)
    return b2