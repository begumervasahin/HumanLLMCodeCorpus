import difflib
original_text = 'one\ntwo\nthree\n'
modified_text = 'ore\ntree\nemu\n'
original_lines = original_text.splitlines(keepends=True)
modified_lines = modified_text.splitlines(keepends=True)
differ = difflib.Differ()
diff = list(differ.compare(original_lines, modified_lines))
restored_original = difflib.restore(diff, 1)
restored_modified = difflib.restore(diff, 2)
restored_original_text = ''.join(restored_original)
restored_modified_text = ''.join(restored_modified)
print(restored_original_text, end="")
print(restored_modified_text, end="")