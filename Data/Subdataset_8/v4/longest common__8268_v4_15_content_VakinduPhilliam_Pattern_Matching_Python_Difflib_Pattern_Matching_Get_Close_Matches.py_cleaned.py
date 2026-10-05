import difflib
import keyword
def find_close_matches(word, possibilities):
    close_matches = difflib.get_close_matches(word, possibilities)
    return close_matches
word1 = 'appel'
possibilities1 = ['ape', 'apple', 'peach', 'puppy']
matches1 = find_close_matches(word1, possibilities1)
print("Close matches for 'appel':", matches1)
word2 = 'wheel'
word3 = 'pineapple'
word4 = 'accept'
matches2 = find_close_matches(word2, keyword.kwlist)
matches3 = find_close_matches(word3, keyword.kwlist)
matches4 = find_close_matches(word4, keyword.kwlist)
print("Close matches for 'wheel':", matches2)
print("Close matches for 'pineapple':", matches3)
print("Close matches for 'accept':", matches4)