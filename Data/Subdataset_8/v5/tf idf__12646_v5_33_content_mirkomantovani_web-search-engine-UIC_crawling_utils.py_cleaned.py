import os
def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)
def create_data_files(project_name, base_url):
    queue_file_path = os.path.join(project_name, 'queue.txt')
    crawled_file_path = os.path.join(project_name, 'crawled.txt')
    if not os.path.isfile(queue_file_path):
        write_data_to_file(queue_file_path, base_url)
    if not os.path.isfile(crawled_file_path):
        write_data_to_file(crawled_file_path, '')
def write_data_to_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)
def append_data_to_file(file_path, data):
    with open(file_path, 'a') as file:
        file.write(data + '\n')
def clear_file_contents(file_path):
    open(file_path, 'w').close()
def get_data_set_from_file(file_path):
    data_set = set()
    with open(file_path, 'rt') as file:
        for line in file:
            data_set.add(line.strip())
    return data_set
def write_data_set_to_file(data_set, file_path):
    with open(file_path, 'w') as file:
        for data in sorted(data_set):
            file.write(data + '\n')