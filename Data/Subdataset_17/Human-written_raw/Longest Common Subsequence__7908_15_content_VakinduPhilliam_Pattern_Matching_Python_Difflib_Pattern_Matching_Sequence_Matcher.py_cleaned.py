lambda x: x in " \t"
s = SequenceMatcher(None, " abcd", "abcd abcd")
s.find_longest_match(0, 5, 0, 9)
s = SequenceMatcher(lambda x: x==" ", " abcd", "abcd abcd")
s.find_longest_match(0, 5, 0, 9)
s = SequenceMatcher(None, "abxcd", "abcd")
s.get_matching_blocks()
a = "qabxcd"
b = "abycdf"
s = SequenceMatcher(None, a, b)
for tag, i1, i2, j1, j2 in s.get_opcodes():
        print('{:7}   a[{}:{}] --> b[{}:{}] {!r:>8} --> {!r}'.format(
            tag, i1, i2, j1, j2, a[i1:i2], b[j1:j2]))
s = SequenceMatcher(None, "abcd", "bcde")
s.ratio()
s.quick_ratio()
s.real_quick_ratio()