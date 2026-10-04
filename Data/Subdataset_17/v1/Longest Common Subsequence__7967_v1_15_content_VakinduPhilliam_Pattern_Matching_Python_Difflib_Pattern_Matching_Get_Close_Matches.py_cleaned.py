import difflib
import keyword
def get_close_matches(word, possibilities):
    matches = difflib.get_close_matches(word, possibilities)
    return matches
matches_1 = get_close_matches('appel', ['ape', 'apple', 'peach', 'puppy'])
matches_2 = get_close_matches('wheel', keyword.kwlist)
matches_3 = get_close_matches('pineapple', keyword.kwlist)
matches_4 = get_close_matches('accept', keyword.kwlist)
print(f"Close matches for 'appel': {matches_1}")
print(f"Close matches for 'wheel': {matches_2}")
print(f"Close matches for 'pineapple': {matches_3}")
print(f"Close matches for 'accept': {matches_4}")