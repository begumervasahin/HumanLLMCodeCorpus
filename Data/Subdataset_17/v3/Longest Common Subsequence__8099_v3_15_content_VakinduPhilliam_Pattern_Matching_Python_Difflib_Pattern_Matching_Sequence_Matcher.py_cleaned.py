from difflib import SequenceMatcher
def print_longest_match(seq1, seq2, isjunk=None):
    matcher = SequenceMatcher(isjunk, seq1, seq2)
    longest_match = matcher.find_longest_match(0, len(seq1), 0, len(seq2))
    print("Longest match:", longest_match)
def print_matching_blocks(seq1, seq2):
    matcher = SequenceMatcher(None, seq1, seq2)
    matching_blocks = matcher.get_matching_blocks()
    print("Matching blocks:", matching_blocks)
def print_opcodes(seq1, seq2):
    matcher = SequenceMatcher(None, seq1, seq2)
    print("Opcodes:")
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        print(f'{tag:7} a[{i1}:{i2}] --> b[{j1}:{j2}] {seq1[i1:i2]!r:>8} --> {seq2[j1:j2]!r}')
def print_similarity_ratios(seq1, seq2):
    matcher = SequenceMatcher(None, seq1, seq2)
    ratio = matcher.ratio()
    quick_ratio = matcher.quick_ratio()
    real_quick_ratio = matcher.real_quick_ratio()
    print("Ratio:", ratio)
    print("Quick ratio:", quick_ratio)
    print("Real quick ratio:", real_quick_ratio)
print("Example 1:")
print_longest_match(" abcd", "abcd abcd")
print("\nExample 2:")
print_longest_match(" abcd", "abcd abcd", isjunk=lambda x: x == " ")
print("\nExample 3:")
print_matching_blocks("abxcd", "abcd")
print("\nExample 4:")
print_opcodes("qabxcd", "abycdf")
print("\nExample 5:")
print_similarity_ratios("abcd", "bcde")