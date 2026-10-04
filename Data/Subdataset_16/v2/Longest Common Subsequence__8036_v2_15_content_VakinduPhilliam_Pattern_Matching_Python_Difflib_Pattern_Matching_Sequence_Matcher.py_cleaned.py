from difflib import SequenceMatcher
b1 = SequenceMatcher(None, " abcd", "abcd abcd")
b2 = b1.find_longest_match(0, 5, 0, 9)
print("Longest match (no custom isjunk):", b2)
b3 = SequenceMatcher(lambda x: x == " ", " abcd", "abcd abcd")
b4 = b3.find_longest_match(0, 5, 0, 9)
print("Longest match (custom isjunk):", b4)
b5 = SequenceMatcher(None, "abxcd", "abcd")
b6 = b5.get_matching_blocks()
print("Matching blocks:", b6)
b7 = "qabxcd"
b8 = "abycdf"
b9 = SequenceMatcher(None, b7, b8)
print("Opcodes:")
for tag, i1, i2, j1, j2 in b9.get_opcodes():
    print(f'{tag:7} b7[{i1}:{i2}] --> b8[{j1}:{j2}] {b7[i1:i2]!r:>8} --> {b8[j1:j2]!r}')
b10 = SequenceMatcher(None, "abcd", "bcde")
b11 = b10.b11()
b12 = b10.b12()
b13 = b10.b13()
print("Ratio:", b11)
print("Quick b11:", b12)
print("Real quick b11:", b13)