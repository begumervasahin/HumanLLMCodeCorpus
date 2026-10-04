import difflib
import keyword
def find_close_matches(word, possibilities):
    return difflib.get_close_matches(word, possibilities)
custom_word_list = ['ape', 'apple', 'peach', 'puppy']
python_keywords = keyword.kwlist
matches_for_appel = find_close_matches('appel', custom_word_list)
matches_for_wheel = find_close_matches('wheel', python_keywords)
matches_for_pineapple = find_close_matches('pineapple', python_keywords)
matches_for_accept = find_close_matches('accept', python_keywords)
print(f"Close matches for 'appel': {matches_for_appel}")
print(f"Close matches for 'wheel': {matches_for_wheel}")
print(f"Close matches for 'pineapple': {matches_for_pineapple}")
print(f"Close matches for 'accept': {matches_for_accept}")