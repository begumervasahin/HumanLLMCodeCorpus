import os
def fonk1(directory):
    if not os.path.exists(directory):
        print(f'Creating directory: {directory}')
        os.makedirs(directory)
def fonk2(b4, b5):
    b1 = os.path.join(b4, 'queue.txt')
    b2 = os.path.join(b4, 'crawled.txt')
    if not os.path.isfile(b1):
        fonk3(b1, b5)
    if not os.path.isfile(b2):
        fonk3(b2, '')
def fonk3(path, data):
    with open(path, 'w') as file:
        file.write(data)
def fonk4(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')
def fonk5(path):
    with open(path, 'w') as file:
        pass
def fonk6(file_name):
    with open(file_name, 'rt') as file:
        return {line.strip() for line in file}
def fonk7(links, file_name):
    with open(file_name, 'w') as file:
        for link in sorted(links):
            file.write(link + '\n')
if b3 = = "__main__":
    b4 = 'my_project'
    b5 = 'http:
    fonk1(b4)
    fonk2(b4, b5)
    fonk4(os.path.join(b4, 'queue.txt'), 'http:
    fonk4(os.path.join(b4, 'queue.txt'), 'http:
    print(fonk6(os.path.join(b4, 'queue.txt')))
    fonk7({'http: