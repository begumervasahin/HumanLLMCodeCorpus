from difflib import SequenceMatcher
def fonk1(seq1, seq2, b1 = None):
    b2 = SequenceMatcher(b1, seq1, seq2)
    b3 = b2.find_longest_match(0, len(seq1), 0, len(seq2))
    print("Longest match:", b3)
def fonk2(seq1, seq2):
    b2 = SequenceMatcher(None, seq1, seq2)
    b4 = b2.get_matching_blocks()
    print("Matching blocks:", b4)
def fonk3(seq1, seq2):
    b2 = SequenceMatcher(None, seq1, seq2)
    print("Opcodes:")
    for tag, i1, i2, j1, j2 in b2.get_opcodes():
        print(f'{tag:7} a[{i1}:{i2}] --> b[{j1}:{j2}] {seq1[i1:i2]!r:>8} --> {seq2[j1:j2]!r}')
def fonk4(seq1, seq2):
    b2 = SequenceMatcher(None, seq1, seq2)
    b5 = b2.b5()
    b6 = b2.b6()
    b7 = b2.b7()
    print("Ratio:", b5)
    print("Quick b5:", b6)
    print("Real quick b5:", b7)
print("Example 1:")
fonk1(" abcd", "abcd abcd")
print("\nExample 2:")
fonk1(" abcd", "abcd abcd", b1 = lambda x: x == " ")
print("\nExample 3:")
fonk2("abxcd", "abcd")
print("\nExample 4:")
fonk3("qabxcd", "abycdf")
print("\nExample 5:")
fonk4("abcd", "bcde")