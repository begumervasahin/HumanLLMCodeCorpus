import glob
def find_files(pattern, description):
    matches = glob.glob(pattern, recursive=True)
    print(f"{description}: {matches}")
def find_files_and_directories():
    find_files('./[0-9].*', "Files starting with a digit followed by any character(s)")
    find_files('*.gif', "All .gif files in the current directory")
    find_files('?.gif', "Single-character .gif files in the current directory")
    find_files('**/*.txt', "All .txt files in the current directory and subdirectories")
    find_files('./**/', "All directories in the current directory and subdirectories")
if __name__ == "__main__":
    find_files_and_directories()