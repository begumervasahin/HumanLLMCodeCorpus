
def is_space_or_tab(x):
    return x in " \t"
s = SequenceMatcher(None, " abcd", "abcd abcd")
longest_match = s.find_longest_match(0, 5, 0, 9)
s = SequenceMatcher(is_space_or_tab, " abcd", "abcd abcd")
longest_match_custom = s.find_longest_match(0, 5, 0, 9)
s = SequenceMatcher(None, "abxcd", "abcd")
matching_blocks = s.get_matching_blocks()
a = "qabxcd"
b = "abycdf"
s = SequenceMatcher(None, a, b)
for tag, i1, i2, j1, j2 in s.get_opcodes():
    print('{:7}   a[{}:{}] --> b[{}:{}] {!r:>8} --> {!r}'.format(
        tag, i1, i2, j1, j2, a[i1:i2], b[j1:j2]))
s = SequenceMatcher(None, "abcd", "bcde")
similarity_ratio = s.ratio()
quick_ratio = s.quick_ratio()
real_quick_ratio = s.real_quick_ratio()