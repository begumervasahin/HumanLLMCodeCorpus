from difflib import SequenceMatcher
def fonk1(char):
    return char in " \t"
b1 = SequenceMatcher(None, " abcd", "abcd abcd")
b2 = b1.find_longest_match(0, 5, 0, 9)
b3 = SequenceMatcher(is_space_or_tab, " abcd", "abcd abcd")
b4 = b3.find_longest_match(0, 5, 0, 9)
b5 = SequenceMatcher(None, "abxcd", "abcd")
b6 = b5.get_matching_blocks()
b7 = "qabxcd"
b8 = "abycdf"
b9 = SequenceMatcher(None, b7, b8)
for tag, i1, i2, j1, j2 in b9.get_opcodes():
    print('{:7}   b7[{}:{}] --> b8[{}:{}] {!r:>8} --> {!r}'.format(
        tag, i1, i2, j1, j2, b7[i1:i2], b8[j1:j2]))
b10 = SequenceMatcher(None, "abcd", "bcde")
b11 = b10.ratio()
b12 = b10.b12()
b13 = b10.b13()