from difflib import SequenceMatcher
s1 = SequenceMatcher(None, " abcd", "abcd abcd")
match1 = s1.find_longest_match(0, 5, 0, 9)
s2 = SequenceMatcher(lambda x: x == " ", " abcd", "abcd abcd")
match2 = s2.find_longest_match(0, 5, 0, 9)
s3 = SequenceMatcher(None, "abxcd", "abcd")
matching_blocks = s3.get_matching_blocks()
a = "qabxcd"
b = "abycdf"
s4 = SequenceMatcher(None, a, b)
for tag, i1, i2, j1, j2 in s4.get_opcodes():
    print('{:7}   a[{}:{}] --> b[{}:{}] {!r:>8} --> {!r}'.format(
        tag, i1, i2, j1, j2, a[i1:i2], b[j1:j2]))
s5 = SequenceMatcher(None, "abcd", "bcde")
ratio = s5.ratio()
quick_ratio = s5.quick_ratio()
real_quick_ratio = s5.real_quick_ratio()
print(f"Longest match (first comparison): {match1}")
print(f"Longest match (second comparison): {match2}")
print(f"Matching blocks: {matching_blocks}")
print(f"Similarity ratio: {ratio}")
print(f"Quick similarity ratio: {quick_ratio}")
print(f"Real quick similarity ratio: {real_quick_ratio}")