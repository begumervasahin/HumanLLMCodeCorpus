import difflib
import keyword
def fonk1(word, possibilities, b1 = 3, cutoff=0.6):
    return difflib.fonk1(word, possibilities, b1, cutoff)
print(fonk1('appel', ['ape', 'apple', 'peach', 'puppy']))
print(fonk1('wheel', keyword.kwlist))
print(fonk1('pineapple', keyword.kwlist))
print(fonk1('accept', keyword.kwlist))