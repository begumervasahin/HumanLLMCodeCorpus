import os
from os import path
__author__ = 'huaijun'
def load_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
def main():
    root_dir = os.getcwd()
    dirs = os.listdir(root_dir)
    file_dirs = [ele for ele in dirs if ele.startswith('C0')]
    sample_dir = path.join(root_dir, 'sample')
    if not path.isdir(sample_dir):
        os.mkdir(sample_dir)
    log_file_path = path.join(root_dir, 'wrong_code.txt')
    with open(log_file_path, 'a+', encoding='utf-8') as log_file:
        for dir_name in file_dirs:
            done_dir = path.join(sample_dir, dir_name)
            if not path.isdir(done_dir):
                os.mkdir(done_dir)
            file_url = path.join(root_dir, dir_name)
            sub_dirs = os.listdir(file_url)
            for file_name in sub_dirs:
                file_path = path.join(file_url, file_name)
                try:
                    text = load_txt(file_path)
                    output_path = path.join(done_dir, file_name)
                    with open(output_path, 'w', encoding='utf-8') as output_file:
                        output_file.write(text)
                except (IOError, UnicodeDecodeError, FileNotFoundError) as e:
                    log_file.write(f'Error with file {dir_name}/{file_name}: {str(e)}\n')
if __name__ == "__main__":
    main()