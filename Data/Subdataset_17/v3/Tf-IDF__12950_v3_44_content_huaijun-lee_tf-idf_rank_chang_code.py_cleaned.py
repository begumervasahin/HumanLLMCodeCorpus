import os
from os import path
__author__ = 'huaijun'
def load_txt(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file_handle:
            return file_handle.read()
    except Exception as e:
        raise e
def create_directory(directory_path):
    if not path.isdir(directory_path):
        os.mkdir(directory_path)
def log_error(log_file, directory, file_name, error_message):
    log_file.write(f'Error processing {directory}/{file_name}: {error_message}\n')
def process_files(root_directory):
    sample_dir = path.join(root_directory, 'sample')
    create_directory(sample_dir)
    with open(path.join(root_directory, 'wrong_code.txt'), 'a+', encoding='utf-8') as log_file:
        for directory in os.listdir(root_directory):
            if directory.startswith('C0'):
                process_directory(directory, root_directory, sample_dir, log_file)
def process_directory(directory, root_directory, sample_dir, log_file):
    done_dir = path.join(sample_dir, directory)
    create_directory(done_dir)
    dir_path = path.join(root_directory, directory)
    for file_name in os.listdir(dir_path):
        file_path = path.join(dir_path, file_name)
        try:
            content = load_txt(file_path)
            write_to_file(path.join(done_dir, file_name), content)
        except (IOError, UnicodeDecodeError, FileNotFoundError) as e:
            log_error(log_file, directory, file_name, str(e))
def write_to_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file_handle:
        file_handle.write(content)
def main():
    root_directory = os.getcwd()
    process_files(root_directory)
if __name__ == "__main__":
    main()