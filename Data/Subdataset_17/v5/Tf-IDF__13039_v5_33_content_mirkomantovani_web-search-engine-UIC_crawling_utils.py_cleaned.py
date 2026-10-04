import os
def create_domain_directory(directory):
    if not os.path.exists(directory):
        print(f'Creating directory: {directory}')
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
    with open(path, 'w') as file:
        pass
def get_set_from_file(file_name):
    with open(file_name, 'rt') as file:
        return {line.strip() for line in file}
def write_set_to_file(links, file_name):
    with open(file_name, 'w') as file:
        for link in sorted(links):
            file.write(link + '\n')
if __name__ == "__main__":
    project_name = 'my_project'
    base_url = 'http:
    create_domain_directory(project_name)
    create_data_files(project_name, base_url)
    append_to_file(os.path.join(project_name, 'queue.txt'), 'http:
    append_to_file(os.path.join(project_name, 'queue.txt'), 'http:
    print(get_set_from_file(os.path.join(project_name, 'queue.txt')))
    write_set_to_file({'http: