from difflib import SequenceMatcher
def fonk1(character):
    return character in " \t"
b1 = SequenceMatcher(None, " abcd", "abcd abcd")
b2 = SequenceMatcher(is_space_or_tab, " abcd", "abcd abcd")
b3 = SequenceMatcher(None, "abxcd", "abcd")
b4 = SequenceMatcher(None, "qabxcd", "abycdf")
b5 = SequenceMatcher(None, "abcd", "bcde")
print("Longest match (default lambda):", b1.find_longest_match(0, 5, 0, 9))
print("Longest match (custom lambda):", b2.find_longest_match(0, 5, 0, 9))
print("Matching blocks:", b3.get_matching_blocks())
print("\nOperation codes:")
for tag, i1, i2, j1, j2 in b4.get_opcodes():
    print(f'{tag:<7}   a[{i1}:{i2}] --> b[{j1}:{j2}] {"qabxcd"[i1:i2]:>8} --> {"abycdf"[j1:j2]}')
print("\nRatios:")
print("Ratio:", b5.ratio())
print("Quick ratio:", b5.quick_ratio())
print("Real quick ratio:", b5.real_quick_ratio())