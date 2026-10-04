from difflib import SequenceMatcher
s1 = SequenceMatcher(None, " abcd", "abcd abcd")
longest_match1 = s1.find_longest_match(0, 5, 0, 9)
print("Longest match (no custom isjunk):", longest_match1)
s2 = SequenceMatcher(lambda x: x == " ", " abcd", "abcd abcd")
longest_match2 = s2.find_longest_match(0, 5, 0, 9)
print("Longest match (custom isjunk):", longest_match2)
s3 = SequenceMatcher(None, "abxcd", "abcd")
matching_blocks = s3.get_matching_blocks()
print("Matching blocks:", matching_blocks)
a = "qabxcd"
b = "abycdf"
s4 = SequenceMatcher(None, a, b)
print("Opcodes:")
for tag, i1, i2, j1, j2 in s4.get_opcodes():
    print(f'{tag:7} a[{i1}:{i2}] --> b[{j1}:{j2}] {a[i1:i2]!r:>8} --> {b[j1:j2]!r}')
s5 = SequenceMatcher(None, "abcd", "bcde")
ratio = s5.ratio()
quick_ratio = s5.quick_ratio()
real_quick_ratio = s5.real_quick_ratio()
print("Ratio:", ratio)
print("Quick ratio:", quick_ratio)
print("Real quick ratio:", real_quick_ratio)