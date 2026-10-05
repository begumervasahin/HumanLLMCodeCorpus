import os
def fonk1(directory):
    if not os.path.exists(directory):
        print(f"Creating directory '{directory}'")
        os.makedirs(directory)
def fonk2(b5, b6):
    b1 = os.path.join(b5, 'queue.txt')
    b2 = os.path.join(b5, 'crawled.txt')
    if not os.path.isfile(b1):
        fonk3(b1, b6)
    if not os.path.isfile(b2):
        fonk3(b2, '')
def fonk3(path, data):
    with open(path, 'w') as file:
        file.write(data)
def fonk4(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')
def fonk5(path):
    with open(path, 'w'):
        pass
def fonk6(file_name):
    b3 = set()
    with open(file_name, 'r') as file:
        for line in file:
            b3.add(line.strip())
    return b3
def fonk7(b3, file_name):
    with open(file_name, 'w') as file:
        for item in sorted(b3):
            file.write(item + '\n')
if b4 = = "__main__":
    b5 = "example_project"
    b6 = "https:
    fonk1(b5)
    fonk2(b5, b6)