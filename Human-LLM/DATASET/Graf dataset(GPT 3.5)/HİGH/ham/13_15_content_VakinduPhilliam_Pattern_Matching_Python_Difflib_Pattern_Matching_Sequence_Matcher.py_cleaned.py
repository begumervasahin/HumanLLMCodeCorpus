lambda x: x in " \t"
b1 = SequenceMatcher(None, " abcd", "abcd abcd")
b1.find_longest_match(0, 5, 0, 9)
b1 = SequenceMatcher(lambda x: x==" ", " abcd", "abcd abcd")
b1.find_longest_match(0, 5, 0, 9)
b1 = SequenceMatcher(None, "abxcd", "abcd")
b1.get_matching_blocks()
b2 = "qabxcd"
b3 = "abycdf"
b1 = SequenceMatcher(None, b2, b3)
for tag, i1, i2, j1, j2 in b1.get_opcodes():
        print('{:7}   b2[{}:{}] --> b3[{}:{}] {!r:>8} --> {!r}'.format(
            tag, i1, i2, j1, j2, b2[i1:i2], b3[j1:j2]))
b1 = SequenceMatcher(None, "abcd", "bcde")
b1.ratio()
b1.quick_ratio()
b1.real_quick_ratio()