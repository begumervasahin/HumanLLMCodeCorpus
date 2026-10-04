import difflib
sequence1 = 'one\ntwo\nthree\n'.splitlines(keepends=True)
sequence2 = 'ore\ntree\nemu\n'.splitlines(keepends=True)
differ = difflib.Differ()
diff = list(differ.compare(sequence1, sequence2))
restored_sequence1 = difflib.restore(diff, 1)
restored_sequence2 = difflib.restore(diff, 2)
print(''.join(restored_sequence1), end="")
print(''.join(restored_sequence2), end="")