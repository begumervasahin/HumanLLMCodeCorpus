import difflib
import keyword
def get_close_matches(word, possibilities):
    return difflib.get_close_matches(word, possibilities)
word_list_1 = ['ape', 'apple', 'peach', 'puppy']
word_list_2 = keyword.kwlist
matches_for_appel = get_close_matches('appel', word_list_1)
matches_for_wheel = get_close_matches('wheel', word_list_2)
matches_for_pineapple = get_close_matches('pineapple', word_list_2)
matches_for_accept = get_close_matches('accept', word_list_2)
print(f"Close matches for 'appel': {matches_for_appel}")
print(f"Close matches for 'wheel': {matches_for_wheel}")
print(f"Close matches for 'pineapple': {matches_for_pineapple}")
print(f"Close matches for 'accept': {matches_for_accept}")