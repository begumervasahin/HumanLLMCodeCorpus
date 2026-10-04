import getopt
import os
import time
import sys
def sort_files(directory, separator):
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.lower().endswith((".jpg", ".mp4", ".mts", ".mov")):
                move_file_to_date_folder(dirpath, filename, separator)
def move_file_to_date_folder(directory_path, filename, separator):
    full_filepath = os.path.join(directory_path, filename)
    print(f"Processing file: {full_filepath}")
    destination_path = get_destination_path(full_filepath, separator)
    destination_directory = os.path.join(directory_path, destination_path)
    print(f"Destination directory: {destination_directory}")
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    new_file_path = os.path.join(destination_directory, filename)
    print(f"Moving file to: {new_file_path}")
    os.rename(full_filepath, new_file_path)
def get_destination_path(filepath, separator):
    modification_time = os.path.getmtime(filepath)
    destination_path = time.strftime(f'%Y{separator}%m{separator}%d', time.localtime(modification_time))
    return destination_path
def main(argv):
    separator = os.sep
    directory = ""
    try:
        opts, _ = getopt.getopt(argv, "h", ["separator=", "path="])
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_usage()
            sys.exit()
        elif opt == "--separator":
            separator = arg
        elif opt == "--path":
            directory = arg
    if not directory:
        print("Error: Path is required")
        print_usage()
        sys.exit(2)
    print(f'Separator: {separator}')
    print(f'Path: {directory}')
    sort_files(directory, separator)
def print_usage():
    print('Usage: SortFiles.py --separator <value> --path <path>')
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "runtests":
        print('Running tests')
    else:
        main(sys.argv[1:])