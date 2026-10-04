import os
from os import path
__author__ = 'huaijun'
def load_txt(file):
    try:
        with open(file, 'r', encoding='utf-8') as file_handle:
            content = file_handle.read()
        return content
    except Exception as e:
        raise e
def main():
    rootdir = os.getcwd()
    dirs = os.listdir(rootdir)
    filedirs = [d for d in dirs if d.startswith('C0')]
    sample_dir = path.join(rootdir, 'sample')
    if not path.isdir(sample_dir):
        os.mkdir(sample_dir)
    with open(path.join(rootdir, 'wrong_code.txt'), 'a+', encoding='utf-8') as log_file:
        for directory in filedirs:
            done_dir = path.join(sample_dir, directory)
            if not path.isdir(done_dir):
                os.mkdir(done_dir)
            dir_path = path.join(rootdir, directory)
            files = os.listdir(dir_path)
            for file_name in files:
                file_path = path.join(dir_path, file_name)
                try:
                    content = load_txt(file_path)
                    with open(path.join(done_dir, file_name), 'w', encoding='utf-8') as new_file:
                        new_file.write(content)
                except (IOError, UnicodeDecodeError, FileNotFoundError) as e:
                    log_file.write(f'Error processing {directory}/{file_name}: {str(e)}\n')
if __name__ == "__main__":
    main()