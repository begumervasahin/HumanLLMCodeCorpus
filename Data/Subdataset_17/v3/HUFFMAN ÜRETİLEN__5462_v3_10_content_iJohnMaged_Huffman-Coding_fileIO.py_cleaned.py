import os
import errno
def split_extension(path):
    base_name, ext = os.path.splitext(path)
    return base_name, ext[1:]
def get_basename(path):
    base_name, _ = split_extension(os.path.basename(path))
    return base_name
def get_filename(path):
    return os.path.basename(path)
def get_file_extension(path):
    _, ext = split_extension(path)
    return ext
def append_to_filename(path, suffix):
    base_name, ext = os.path.splitext(path)
    return f"{base_name}{suffix}{ext}"
def change_extension(path, new_extension):
    base_name, _ = os.path.splitext(path)
    return f"{base_name}.{new_extension}"
def get_directory(path):
    return os.path.dirname(os.path.abspath(path))
def get_file_size(path):
    return os.path.getsize(path)
def get_directory_size(path):
    total_size = 0
    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += get_file_size(file_path)
    return total_size
def generate_output_file_path(directory):
    dir_name = os.path.basename(os.path.normpath(directory))
    return os.path.join(os.getcwd(), f"{dir_name}.huffman")
def generate_huffman_file_path(path, is_directory=False):
    return generate_output_file_path(path) if is_directory else change_extension(path, "huffman")
def get_files_to_process(path):
    if os.path.isdir(path):
        files, total_size = list_files(path)
        output_path = generate_huffman_file_path(path, is_directory=True)
    elif os.path.isfile(path):
        files = {get_filename(path): path}
        total_size = get_file_size(path)
        output_path = generate_huffman_file_path(path)
    else:
        raise FileNotFoundError(f"The specified path does not exist: {path}")
    return files, total_size, output_path
def list_files(path):
    files = {}
    total_size = 0
    parent_dir = os.path.dirname(os.path.abspath(path))
    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            relative_path = os.path.relpath(file_path, parent_dir)
            files[relative_path] = file_path
            total_size += get_file_size(file_path)
    return files, total_size
def create_directory_if_not_exists(path):
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
def invert_dictionary(d):
    return {v: k for k, v in d.items()}
