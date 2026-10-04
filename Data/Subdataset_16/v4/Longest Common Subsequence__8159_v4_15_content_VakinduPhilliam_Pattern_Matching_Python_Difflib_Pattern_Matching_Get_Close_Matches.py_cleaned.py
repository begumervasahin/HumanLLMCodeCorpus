from difflib import get_close_matches
import keyword
b1 = get_close_matches('appel', ['ape', 'apple', 'peach', 'puppy'])
print("Close matches for 'appel':", b1)
b2 = get_close_matches('wheel', keyword.kwlist)
print("Close matches for 'wheel':", b2)
b3 = get_close_matches('pineapple', keyword.kwlist)
print("Close matches for 'pineapple':", b3)
b4 = get_close_matches('accept', keyword.kwlist)
print("Close matches for 'accept':", b4)