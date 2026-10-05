import re
def verify_sequence(sequence):
    return bool(re.match("^[ATCG ]*$", sequence))
def find_longest_common_subsequence(seq1, seq2):
    len_seq1 = len(seq1)
    len_seq2 = len(seq2)
    table = [[0] * (len_seq2 + 1) for _ in range(len_seq1 + 1)]
    for i in range(1, len_seq1 + 1):
        for j in range(1, len_seq2 + 1):
            if seq1[i - 1] == seq2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    index = table[len_seq1][len_seq2]
    lcs_chars = [""] * (index + 1)
    i, j = len_seq1, len_seq2
    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            lcs_chars[index - 1] = seq1[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif table[i - 1][j] > table[i][j - 1]:
            i -= 1
        else:
            j -= 1
    lcs_sequence = "".join(lcs_chars)
    return lcs_sequence
sequence1 = input("Enter the First Sequence\n").upper()
sequence2 = input("\nEnter the Querying Sequence\n").upper()
if verify_sequence(sequence1) and verify_sequence(sequence2):
    if len(sequence1) >= len(sequence2):
        print(f"Given Sequences: {sequence1}, {sequence2}")
        lcs_result = find_longest_common_subsequence(sequence1, sequence2)
        print(f"\nThe Longest Common Subsequence is: {lcs_result}")
        print(f"Length of the LCS: {len(lcs_result)}")
    else:
        print("The Querying Sequence should be shorter than or equal to the First Sequence")
else:
    print("Both sequences should only contain 'A', 'T', 'C', 'G', or space characters")