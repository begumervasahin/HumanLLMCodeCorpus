import difflib
import keyword
def find_close_matches(word, possibilities):
    close_matches = difflib.get_close_matches(word, possibilities)
    return close_matches
word1 = 'appel'
possibilities1 = ['ape', 'apple', 'peach', 'puppy']
matches1 = find_close_matches(word1, possibilities1)
print("Close matches for 'appel':", matches1)
words_to_check = ['wheel', 'pineapple', 'accept']
for word in words_to_check:
    matches = find_close_matches(word, keyword.kwlist)
    print(f"Close matches for '{word}':", matches)