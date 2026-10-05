import difflib
import keyword
def get_close_matches(word, possibilities, n=3, cutoff=0.6):
    return difflib.get_close_matches(word, possibilities, n, cutoff)
print(get_close_matches('appel', ['ape', 'apple', 'peach', 'puppy']))
print(get_close_matches('wheel', keyword.kwlist))
print(get_close_matches('pineapple', keyword.kwlist))
print(get_close_matches('accept', keyword.kwlist))