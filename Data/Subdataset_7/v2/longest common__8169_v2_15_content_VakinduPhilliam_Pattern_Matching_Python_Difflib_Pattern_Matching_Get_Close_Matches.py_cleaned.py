import difflib
import keyword
def fonk1(word, possibilities, b1 = 3, cutoff=0.6):
    return difflib.fonk1(word, possibilities, b1, cutoff)
b2 = fonk1('appel', ['ape', 'apple', 'peach', 'puppy'])
b3 = fonk1('wheel', keyword.kwlist)
b4 = fonk1('pineapple', keyword.kwlist)
b5 = fonk1('accept', keyword.kwlist)
print("Close matches for 'appel':", b2)
print("Close matches for 'wheel' among Python keywords:", b3)
print("Close matches for 'pineapple' among Python keywords:", b4)
print("Close matches for 'accept' among Python keywords:", b5)