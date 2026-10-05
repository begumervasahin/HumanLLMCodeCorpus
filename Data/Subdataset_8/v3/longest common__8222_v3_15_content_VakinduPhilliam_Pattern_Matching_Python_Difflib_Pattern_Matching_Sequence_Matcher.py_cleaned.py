from difflib import SequenceMatcher
def is_space_or_tab(character):
    return character in " \t"
default_matcher = SequenceMatcher(None, " abcd", "abcd abcd")
custom_matcher = SequenceMatcher(is_space_or_tab, " abcd", "abcd abcd")
abxcd_matcher = SequenceMatcher(None, "abxcd", "abcd")
qabxcd_matcher = SequenceMatcher(None, "qabxcd", "abycdf")
abcd_bcde_matcher = SequenceMatcher(None, "abcd", "bcde")
print("Longest match (default lambda):", default_matcher.find_longest_match(0, 5, 0, 9))
print("Longest match (custom lambda):", custom_matcher.find_longest_match(0, 5, 0, 9))
print("Matching blocks:", abxcd_matcher.get_matching_blocks())
print("\nOperation codes:")
for tag, i1, i2, j1, j2 in qabxcd_matcher.get_opcodes():
    print(f'{tag:<7}   a[{i1}:{i2}] --> b[{j1}:{j2}] {"qabxcd"[i1:i2]:>8} --> {"abycdf"[j1:j2]}')
print("\nRatios:")
print("Ratio:", abcd_bcde_matcher.ratio())
print("Quick ratio:", abcd_bcde_matcher.quick_ratio())
print("Real quick ratio:", abcd_bcde_matcher.real_quick_ratio())