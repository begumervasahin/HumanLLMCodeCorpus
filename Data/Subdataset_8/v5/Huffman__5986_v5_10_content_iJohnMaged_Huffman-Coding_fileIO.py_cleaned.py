import os
import errno
def split_extension(path):
    filename, ext = os.path.splitext(path)
    return [filename, ext[1:]]
def base_name(path):
    return split_extension(os.path.basename(path))[0]
def file_name(path):
    return os.path.basename(path)
def file_extension(path):
    return os.path.splitext(path)[1][1:]
def add_to_name(path, word):
    filename, ext = os.path.splitext(path)
    return filename + word + ext
def alter_extension(path, new_exten):
    filename, ext = os.path.splitext(path)
    return filename + "." + new_exten
def directory_name(path):
    return os.path.split(os.path.abspath(path))[0]
def get_size(path):
    return os.path.getsize(path)
def directory_size(path):
    total_size = 0
    for p, dirs, files in os.walk(path):
        for f in files:
            total_size += get_size(os.path.join(p, f))
    return total_size
def output_file_path(p):
    p = os.path.join(p, '')
    return os.path.join(os.getcwd(), '') + os.path.basename(os.path.dirname(p)) + ".huffman"
def huffman_file_path(p, dir=False):
    if not dir:
        return os.path.join(os.getcwd(), '') + alter_extension(p, "huffman")
    return output_file_path(p)
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
    f = {}
    total_size = 0
    path = path.rstrip(os.sep)
    parent = os.path.dirname(path)
    for p, dirs, files in os.walk(path):
        for file in files:
            fp = os.path.join(p, file)
            total_size += get_size(fp)
            f[(os.path.relpath(os.path.join(p, file), parent))] = fp
    return f, total_size
def create_path_if_not_exist(path):
    dr = os.path.dirname(path)
    if not dr:
        return
    try:
        os.makedirs(dr)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
def invert_dict(d):
    return dict([(v, k) for k, v in d.items()])