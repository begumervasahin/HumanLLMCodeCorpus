from filecmp import dircmp
def print_diff_files(directory_comparison):
    for file_name in directory_comparison.diff_files:
        print(f"Different file: {file_name} found in {directory_comparison.left} and {directory_comparison.right}")
    for subdir_comparison in directory_comparison.subdirs.values():
        print_diff_files(subdir_comparison)
if __name__ == "__main__":
    dir1 = 'dir1'
    dir2 = 'dir2'
    directory_comparison = dircmp(dir1, dir2)
    print_diff_files(directory_comparison)