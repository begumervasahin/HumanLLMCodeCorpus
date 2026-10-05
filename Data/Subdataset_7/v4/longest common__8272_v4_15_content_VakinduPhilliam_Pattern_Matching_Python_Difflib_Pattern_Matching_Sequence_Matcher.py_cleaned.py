
def fonk1(x):
    return x in " \t"
b1 = SequenceMatcher(None, " abcd", "abcd abcd")
b2 = b1.find_longest_match(0, 5, 0, 9)
b1 = SequenceMatcher(is_space_or_tab, " abcd", "abcd abcd")
b3 = b1.find_longest_match(0, 5, 0, 9)
b1 = SequenceMatcher(None, "abxcd", "abcd")
b4 = b1.get_matching_blocks()
b5 = "qabxcd"
b6 = "abycdf"
b1 = SequenceMatcher(None, b5, b6)
for tag, i1, i2, j1, j2 in b1.get_opcodes():
    print('{:7}   b5[{}:{}] --> b6[{}:{}] {!r:>8} --> {!r}'.format(
        tag, i1, i2, j1, j2, b5[i1:i2], b6[j1:j2]))
b1 = SequenceMatcher(None, "abcd", "bcde")
b7 = b1.ratio()
b8 = b1.b8()
b9 = b1.b9()