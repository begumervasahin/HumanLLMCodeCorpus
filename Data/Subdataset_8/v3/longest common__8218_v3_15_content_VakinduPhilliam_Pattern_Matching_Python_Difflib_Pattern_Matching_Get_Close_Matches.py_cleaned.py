import difflib
import keyword
def find_close_matches(word, possibilities, n=3, cutoff=0.6):
    return difflib.get_close_matches(word, possibilities, n, cutoff)
test_cases = [
    ("appel", ['ape', 'apple', 'peach', 'puppy']),
    ("wheel", keyword.kwlist),
    ("pineapple", keyword.kwlist),
    ("accept", keyword.kwlist)
]
for word, possibilities in test_cases:
    matches = find_close_matches(word, possibilities)
    print(f"Close matches for '{word}': {matches}")