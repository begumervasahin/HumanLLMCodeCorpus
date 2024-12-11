import os
def fonk1(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)
def fonk2(project_name, base_url):
    b1 = os.path.join(project_name, 'queue.txt')
    b2 = os.path.join(project_name, 'crawled.txt')
    if not os.path.isfile(b1):
        fonk3(b1, base_url)
    if not os.path.isfile(b2):
        fonk3(b2, '')
def fonk3(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)
def fonk4(file_path, data):
    with open(file_path, 'a') as file:
        file.write(data + '\n')
def fonk5(file_path):
    open(file_path, 'w').close()
def fonk6(file_path):
    b3 = set()
    with open(file_path, 'rt') as file:
        for line in file:
            b3.add(line.strip())
    return b3
def fonk7(b3, file_path):
    with open(file_path, 'w') as file:
        for data in sorted(b3):
            file.write(data + '\n')