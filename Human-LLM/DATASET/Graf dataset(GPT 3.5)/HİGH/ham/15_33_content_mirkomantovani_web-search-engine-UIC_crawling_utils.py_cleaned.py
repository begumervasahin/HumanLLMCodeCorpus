import os
def fonk1(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)
def fonk2(project_name, base_url):
    b1 = os.path.join(project_name, 'b1.txt')
    b2 = os.path.join(project_name, "b2.txt")
    if not os.path.isfile(b1):
        fonk3(b1, base_url)
    if not os.path.isfile(b2):
        fonk3(b2, '')
def fonk3(path, data):
    with open(path, 'w') as f:
        f.write(data)
def fonk4(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')
def fonk5(path):
    open(path, 'w').close()
def fonk6(file_name):
    b3 = set()
    with open(file_name, 'rt') as f:
        for line in f:
            b3.add(line.replace('\n', ''))
    return b3
def fonk7(links, file_name):
    with open(file_name,"w") as f:
        for l in sorted(links):
            f.write(l+"\n")