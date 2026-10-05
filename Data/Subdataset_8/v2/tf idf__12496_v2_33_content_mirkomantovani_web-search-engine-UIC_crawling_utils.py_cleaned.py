import os
def create_domain_directory(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)
def create_data_files(project_name, base_url):
    queue_path = os.path.join(project_name, 'queue.txt')
    crawled_path = os.path.join(project_name, 'crawled.txt')
    if not os.path.isfile(queue_path):
        write_file(queue_path, base_url)
    if not os.path.isfile(crawled_path):
        write_file(crawled_path, '')
def write_file(path, data):
    with open(path, 'w') as file:
        file.write(data)
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')
def delete_file_contents(path):
    with open(path, 'w'):
        pass
def get_set_from_file(file_name):
    data_set = set()
    with open(file_name, 'r') as file:
        for line in file:
            data_set.add(line.strip())
    return data_set
def write_set_to_file(data_set, file_name):
    with open(file_name, 'w') as file:
        for item in sorted(data_set):
            file.write(item + '\n')
if __name__ == "__main__":
    project_name = "example_project"
    base_url = "https:
    create_domain_directory(project_name)
    create_data_files(project_name, base_url)