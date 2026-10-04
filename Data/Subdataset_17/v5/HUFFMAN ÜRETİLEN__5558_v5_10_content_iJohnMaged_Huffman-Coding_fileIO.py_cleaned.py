import errno
import os
def splitext_(path):
    file_name, ext = os.path.splitext(path)
    return file_name, ext.lstrip('.')
def get_basename(path):
    return splitext_(os.path.basename(path))[0]
def get_filename(path):
    return os.path.basename(path)
def get_file_extension(path):
    return splitext_(path)[1]
def add_to_filename(path, suffix):
    file_name, ext = splitext_(path)
    return f"{file_name}{suffix}.{ext}"
def change_extension(path, new_extension):
    file_name, _ = splitext_(path)
    return f"{file_name}.{new_extension.lstrip('.')}"
def get_directory_name(path):
    return os.path.dirname(os.path.abspath(path))
def get_file_size(path):
    return os.path.getsize(path)
def get_directory_size(path):
    total_size = 0
    for root, _, files in os.walk(path):
        for file in files:
            total_size += get_file_size(os.path.join(root, file))
    return total_size
def generate_output_file_path(directory_path):
    directory_name = os.path.basename(os.path.normpath(directory_path))
    return os.path.join(os.getcwd(), f"{directory_name}.huffman")
def get_huffman_file_path(path, is_directory=False):
    if is_directory:
        return generate_output_file_path(path)
    return change_extension(path, "huffman")
def prepare_files_for_processing(path):
    if os.path.isdir(path):
        files, original_size = list_files_in_directory(path)
        output_path = get_huffman_file_path(path, is_directory=True)
    elif os.path.isfile(path):
        files = {get_filename(path): path}
        original_size = get_file_size(path)
        output_path = get_huffman_file_path(path)
    else:
        raise FileNotFoundError(f"The specified path does not exist: {path}")
    return files, original_size, output_path
def list_files_in_directory(path):
    files = {}
    total_size = 0
    path = path.rstrip(os.sep)
    parent_dir = os.path.dirname(path)
    for root, _, file_names in os.walk(path):
        for file_name in file_names:
            file_path = os.path.join(root, file_name)
            total_size += get_file_size(file_path)
            relative_path = os.path.relpath(file_path, parent_dir)
            files[relative_path] = file_path
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