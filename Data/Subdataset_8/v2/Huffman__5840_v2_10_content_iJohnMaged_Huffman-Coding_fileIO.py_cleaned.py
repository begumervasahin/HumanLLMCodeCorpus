import os
import errno
def split_extension(path):
    filename, extension = os.path.splitext(path)
    return [filename, extension[1:]]
def base_name(path):
    return split_extension(os.path.basename(path))[0]
def file_name(path):
    return os.path.basename(path)
def file_extension(path):
    return os.path.splitext(path)[1][1:]
def add_to_name(path, word):
    filename, ext = os.path.splitext(path)
    return filename + word + ext
def alter_extension(path, new_extension):
    filename, ext = os.path.splitext(path)
    return filename + "." + new_extension
def directory_name(path):
    return os.path.split(os.path.abspath(path))[0]
def get_size(path):
    return os.path.getsize(path)
def directory_size(path):
    total_size = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            total_size += get_size(os.path.join(root, file))
    return total_size
def output_file(p):
    p = os.path.join(p, '')
    return os.path.join(os.getcwd(), '') + os.path.basename(os.path.dirname(p)) + ".huffman"
def huffman_file_path(p, dir=False):
    if not dir:
        return os.path.join(os.getcwd(), '') + alter_extension(p, "huffman")
    return output_file(p)
def files_to_process(p):
    if os.path.isdir(p):
        files, original_size = list_files(p)
        output = huffman_file_path(p, True)
    elif os.path.isfile(p):
        files = {os.path.basename(p): p}
        original_size = get_size(p)
        output = huffman_file_path(p)
    else:
        raise FileNotFoundError
    return files, original_size, output
def list_files(path):
    files = {}
    total_size = 0
    path = path.rstrip(os.sep)
    parent = os.path.dirname(path)
    for root, dirs, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(root, filename)
            total_size += get_size(filepath)
            files[(os.path.relpath(os.path.join(root, filename), parent))] = filepath
    return files, total_size
def create_path_if_not_exists(path):
    directory = os.path.dirname(path)
    if not directory:
        return
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
def invert_dictionary(d):
    return dict([(value, key) for key, value in d.items()])