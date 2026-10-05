from difflib import ndiff, restore
def compute_diff(original_lines, modified_lines):
    return list(ndiff(original_lines, modified_lines))
def restore_lines(diff, which):
    return ''.join(restore(diff, which))
def main():
    original_lines = 'one\ntwo\nthree\n'.splitlines(keepends=True)
    modified_lines = 'ore\ntree\nemu\n'.splitlines(keepends=True)
    diff = compute_diff(original_lines, modified_lines)
    restored_original = restore_lines(diff, 1)
    restored_modified = restore_lines(diff, 2)
    print(restored_original, end="")
    print(restored_modified, end="")
if __name__ == "__main__":
    main()