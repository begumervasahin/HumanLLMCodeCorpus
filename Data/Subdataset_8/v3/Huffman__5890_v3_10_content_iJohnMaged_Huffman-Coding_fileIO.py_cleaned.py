import os
import errno
def split_extension(path):
    filename, extension = os.path.splitext(path)
    return filename, extension[1:]
def base_name(path):
    filename, _ = split_extension(os.path.basename(path))
    return filename
def file_name(path):
    return os.path.basename(path)
def file_extension(path):
    _, extension = split_extension(path)
    return extension
def add_to_name(path, word):
    filename, extension = split_extension(path)
    return f"{filename}{word}{extension}"
def alter_extension(path, new_extension):
    filename, _ = split_extension(path)
    return f"{filename}.{new_extension}"
def directory_name(path):
    return os.path.dirname(os.path.abspath(path))
def get_size(path):
    return os.path.getsize(path)
def directory_size(path):
    total_size = 0
    for root, _, files in os.walk(path):
        for file in files:
            total_size += get_size(os.path.join(root, file))
    return total_size
def output_file(path):
    return os.path.join(os.getcwd(), os.path.basename(os.path.dirname(path)) + ".huffman")
def huffman_file_path(path, is_directory=False):
    if not is_directory:
        return alter_extension(os.path.join(os.getcwd(), path), "huffman")
    return output_file(path)
def files_to_process(path):
    if os.path.isdir(path):
        files, original_size = list_files(path)
        output = huffman_file_path(path, is_directory=True)
    elif os.path.isfile(path):
        files = {os.path.basename(path): path}
        original_size = get_size(path)
        output = huffman_file_path(path)
    else:
        raise FileNotFoundError
    return files, original_size, output
def list_files(directory):
    files = {}
    total_size = 0
    directory = directory.rstrip(os.sep)
    parent = os.path.dirname(directory)
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(root, filename)
            total_size += get_size(filepath)
            files[os.path.relpath(os.path.join(root, filename), parent)] = filepath
    return files, total_size
def create_path_if_not_exists(path):
    directory = os.path.dirname(path)
    if directory:
        try:
            os.makedirs(directory)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
def invert_dictionary(dictionary):
    return {value: key for key, value in dictionary.items()}