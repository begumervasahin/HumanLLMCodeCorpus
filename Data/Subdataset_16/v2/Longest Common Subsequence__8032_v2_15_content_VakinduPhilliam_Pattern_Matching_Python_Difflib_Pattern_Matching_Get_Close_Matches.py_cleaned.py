import difflib
import keyword
def fonk1(word, possibilities):
    return difflib.fonk1(word, possibilities)
b1 = ['ape', 'apple', 'peach', 'puppy']
b2 = keyword.kwlist
b3 = fonk1('appel', b1)
b4 = fonk1('wheel', b2)
b5 = fonk1('pineapple', b2)
b6 = fonk1('accept', b2)
print(f"Close matches for 'appel': {b3}")
print(f"Close matches for 'wheel': {b4}")
print(f"Close matches for 'pineapple': {b5}")
print(f"Close matches for 'accept': {b6}")