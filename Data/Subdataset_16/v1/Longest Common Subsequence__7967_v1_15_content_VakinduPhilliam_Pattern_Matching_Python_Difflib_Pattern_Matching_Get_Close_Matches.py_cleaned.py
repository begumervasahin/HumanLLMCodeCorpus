import difflib
import keyword
def fonk1(word, possibilities):
    b1 = difflib.fonk1(word, possibilities)
    return b1
b2 = fonk1('appel', ['ape', 'apple', 'peach', 'puppy'])
b3 = fonk1('wheel', keyword.kwlist)
b4 = fonk1('pineapple', keyword.kwlist)
b5 = fonk1('accept', keyword.kwlist)
print(f"Close b1 for 'appel': {b2}")
print(f"Close b1 for 'wheel': {b3}")
print(f"Close b1 for 'pineapple': {b4}")
print(f"Close b1 for 'accept': {b5}")