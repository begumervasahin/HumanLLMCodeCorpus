from difflib import get_close_matches
import keyword
matches_for_appel = get_close_matches('appel', ['ape', 'apple', 'peach', 'puppy'])
print("Close matches for 'appel':", matches_for_appel)
matches_for_wheel = get_close_matches('wheel', keyword.kwlist)
print("Close matches for 'wheel':", matches_for_wheel)
matches_for_pineapple = get_close_matches('pineapple', keyword.kwlist)
print("Close matches for 'pineapple':", matches_for_pineapple)
matches_for_accept = get_close_matches('accept', keyword.kwlist)
print("Close matches for 'accept':", matches_for_accept)