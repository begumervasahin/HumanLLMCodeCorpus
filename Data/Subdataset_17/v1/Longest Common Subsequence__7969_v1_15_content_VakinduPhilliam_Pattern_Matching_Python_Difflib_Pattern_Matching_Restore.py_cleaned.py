import difflib
sequence1 = 'one\ntwo\nthree\n'.splitlines(keepends=True)
sequence2 = 'ore\ntree\nemu\n'.splitlines(keepends=True)
differ = difflib.Differ()
diff = list(differ.compare(sequence1, sequence2))
restored1 = difflib.restore(diff, 1)
restored2 = difflib.restore(diff, 2)
print(''.join(restored1), end="")
print(''.join(restored2), end="")