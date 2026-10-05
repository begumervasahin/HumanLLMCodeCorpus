from difflib import SequenceMatcher
def is_space_or_tab(character):
    return character in " \t"
sequence_matcher_default = SequenceMatcher(None, " abcd", "abcd abcd")
sequence_matcher_custom = SequenceMatcher(is_space_or_tab, " abcd", "abcd abcd")
sequence_matcher_abxcd = SequenceMatcher(None, "abxcd", "abcd")
sequence_matcher_qabxcd = SequenceMatcher(None, "qabxcd", "abycdf")
sequence_matcher_abcd_bcde = SequenceMatcher(None, "abcd", "bcde")
print("Longest match (default lambda):", sequence_matcher_default.find_longest_match(0, 5, 0, 9))
print("Longest match (custom lambda):", sequence_matcher_custom.find_longest_match(0, 5, 0, 9))
print("Matching blocks:", sequence_matcher_abxcd.get_matching_blocks())
print("\nOperation codes:")
for tag, i1, i2, j1, j2 in sequence_matcher_qabxcd.get_opcodes():
    print('{:7}   a[{}:{}] --> b[{}:{}] {!r:>8} --> {!r}'.format(
        tag, i1, i2, j1, j2, "qabxcd"[i1:i2], "abycdf"[j1:j2]))
print("\nRatios:")
print("Ratio:", sequence_matcher_abcd_bcde.ratio())
print("Quick ratio:", sequence_matcher_abcd_bcde.quick_ratio())
print("Real quick ratio:", sequence_matcher_abcd_bcde.real_quick_ratio())