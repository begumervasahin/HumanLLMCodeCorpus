import difflib
import keyword
def fonk1(word, possibilities):
    b1 = difflib.get_close_matches(word, possibilities)
    return b1
b2 = 'appel'
b3 = ['ape', 'apple', 'peach', 'puppy']
b4 = fonk1(b2, b3)
print("Close matches for 'appel':", b4)
b5 = 'wheel'
b6 = 'pineapple'
b7 = 'accept'
b8 = fonk1(b5, keyword.kwlist)
b9 = fonk1(b6, keyword.kwlist)
b10 = fonk1(b7, keyword.kwlist)
print("Close matches for 'wheel':", b8)
print("Close matches for 'pineapple':", b9)
print("Close matches for 'accept':", b10)