from difflib import SequenceMatcher
b1 = lambda x: x in " \t"
b2 = SequenceMatcher(None, " abcd", "abcd abcd")
b3 = SequenceMatcher(b1, " abcd", "abcd abcd")
b4 = SequenceMatcher(None, "abxcd", "abcd")
b5 = SequenceMatcher(None, "qabxcd", "abycdf")
b6 = SequenceMatcher(None, "abcd", "bcde")
print("Longest match (default lambda):", b2.find_longest_match(0, 5, 0, 9))
print("Longest match (custom lambda):", b3.find_longest_match(0, 5, 0, 9))
print("Matching blocks:", b4.get_matching_blocks())
print("\nOperation codes:")
for tag, i1, i2, j1, j2 in b5.get_opcodes():
    print('{:7}   a[{}:{}] --> b[{}:{}] {!r:>8} --> {!r}'.format(
        tag, i1, i2, j1, j2, a[i1:i2], b[j1:j2]))
print("\nRatios:")
print("Ratio:", b6.ratio())
print("Quick ratio:", b6.quick_ratio())
print("Real quick ratio:", b6.real_quick_ratio())