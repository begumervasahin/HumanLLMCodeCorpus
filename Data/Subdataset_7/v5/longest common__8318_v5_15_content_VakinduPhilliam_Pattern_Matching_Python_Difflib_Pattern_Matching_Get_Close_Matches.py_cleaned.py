import difflib
import keyword
def fonk1(word, possibilities):
    b1 = difflib.get_close_matches(word, possibilities)
    return b1
b2 = 'appel'
b3 = ['ape', 'apple', 'peach', 'puppy']
b4 = fonk1(b2, b3)
print("Close b6 for 'appel':", b4)
b5 = ['wheel', 'pineapple', 'accept']
for word in b5:
    b6 = fonk1(word, keyword.kwlist)
    print(f"Close b6 for '{word}':", b6)