import difflib
import keyword
def fonk1(word, possibilities, b1 = 3, cutoff=0.6):
    return difflib.get_close_matches(word, possibilities, b1, cutoff)
b2 = [
    ("appel", ['ape', 'apple', 'peach', 'puppy']),
    ("wheel", keyword.kwlist),
    ("pineapple", keyword.kwlist),
    ("accept", keyword.kwlist)
]
for word, possibilities in b2:
    b3 = fonk1(word, possibilities)
    print(f"Close b3 for '{word}': {b3}")