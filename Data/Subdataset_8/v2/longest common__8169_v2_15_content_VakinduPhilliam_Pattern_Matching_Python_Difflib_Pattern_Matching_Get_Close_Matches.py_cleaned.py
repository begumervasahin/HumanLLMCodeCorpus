import difflib
import keyword
def get_close_matches(word, possibilities, n=3, cutoff=0.6):
    return difflib.get_close_matches(word, possibilities, n, cutoff)
word1_matches = get_close_matches('appel', ['ape', 'apple', 'peach', 'puppy'])
word2_matches = get_close_matches('wheel', keyword.kwlist)
word3_matches = get_close_matches('pineapple', keyword.kwlist)
word4_matches = get_close_matches('accept', keyword.kwlist)
print("Close matches for 'appel':", word1_matches)
print("Close matches for 'wheel' among Python keywords:", word2_matches)
print("Close matches for 'pineapple' among Python keywords:", word3_matches)
print("Close matches for 'accept' among Python keywords:", word4_matches)