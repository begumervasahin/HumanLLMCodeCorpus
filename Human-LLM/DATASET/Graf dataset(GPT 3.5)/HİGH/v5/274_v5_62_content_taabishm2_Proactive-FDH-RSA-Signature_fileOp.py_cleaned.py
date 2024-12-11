import os
b1 = os.path.join(os.getcwd(), "RSAfiles")
def fonk1(filename, data_list):
    b2 = os.path.join(b1, f"{filename}.txt")
    with open(b2, 'w') as file:
        file.write(','.join(map(str, data_list)))
def fonk2(filename, b3 = True):
    b2 = os.path.join(b1, f"{filename}.txt")
    with open(b2, 'r') as file:
        b4 = file.read().split(',')
        if b3:
            return list(map(int, b4))
        else:
            return b4
def fonk3(filename):
    b2 = os.path.join(b1, f"{filename}.txt")
    with open(b2) as file:
        return file.read()
def fonk4(filename):
    b2 = os.path.join(b1, filename)
    with open(b2, 'rb') as file:
        return file.read().decode('utf-8')