import getopt
import os
import sys
import time
def sort_files(directory_path, separator):
    extensions = (".jpg", ".mp4", ".mts", ".mov")
    for root, _, filenames in os.walk(directory_path):
        for filename in filenames:
            if filename.lower().endswith(extensions):
                parse_file(root, filename, separator)
def parse_file(directory_path, filename, separator):
    full_file_path = os.path.join(directory_path, filename)
    new_path = get_destination_path(full_file_path, separator)
    new_path = os.path.join(directory_path, new_path)
    os.makedirs(new_path, exist_ok=True)
    os.rename(full_file_path, os.path.join(new_path, filename))
def get_destination_path(full_file_path, separator):
    epoch_sec = os.path.getmtime(full_file_path)
    new_path = time.strftime('%Y' + separator + '%Y %m %d', time.localtime(epoch_sec))
    return new_path
def main(argv):
    separator = "\\"
    path = ""
    try:
        opts, _ = getopt.getopt(argv, "hi:o:", ["separator=", "path="])
    except getopt.GetoptError:
        print('Usage: SortFiles.py --separator <value> --path <path>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--help':
            print('Usage: SortFiles.py --separator <value> --path <path>')
            sys.exit()
        elif opt == "--separator":
            separator = arg
        elif opt == "--path":
            path = arg
    sort_files(path, separator)
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "runtests":
        print('Running tests')
    else:
        main(sys.argv[1:])