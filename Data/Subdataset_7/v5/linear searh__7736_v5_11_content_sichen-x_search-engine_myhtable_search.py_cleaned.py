from htable import htable_put, htable_get, htable
from words import get_text, words
def fonk1(files):
    if not files:
        return None
    b1 = htable(4011)
    for file_index, file_path in enumerate(files):
        b2 = get_text(file_path)
        b3 = words(b2)
        for word in b3:
            b4 = htable_get(b1, word)
            if b4:
                b4.add(file_index)
            else:
                htable_put(b1, word, {file_index})
    return b1
def fonk2(files, index, terms):
    if not files or not index or not terms:
        return None
    b5 = []
    b6 = []
    for term in terms:
        b7 = htable_get(index, term)
        if b7:
            b6.append(b7)
        else:
            return None
    if b6:
        b8 = set.intersection(*b6)
        for index in b8:
            b5.append(files[index])
    else:
        return None
    return b5