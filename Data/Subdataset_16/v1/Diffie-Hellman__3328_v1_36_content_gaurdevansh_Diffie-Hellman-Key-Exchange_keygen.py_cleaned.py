import random
a1 = 26994308385016394749558484505346578147056894665639
a2 = 2
def fonk1(filename):
    b1 = str(random.randint(1000, 10000))
    with open(filename, 'w') as outfile:
        outfile.write(b1)
def fonk2(private_filename, public_filename):
    with open(private_filename, 'r') as infile:
        b1 = int(infile.read())
    b2 = pow(a2, b1, a1)
    with open(public_filename, 'w') as outfile:
        outfile.write(str(b2))
def fonk3(private_filename, public_filename):
    with open(private_filename, 'r') as infile:
        b1 = int(infile.read())
    with open(public_filename, 'r') as infile:
        b2 = int(infile.read())
    b3 = pow(b2, b1, a1)
    return b3
def fonk4():
    b4 = 'b1.txt'
    b5 = 'b2.txt'
    fonk1(b4)
    fonk2(b4, b5)
    b3 = fonk3(b4, b5)
    print(f'Shared Secret: {b3}')
if b6 = = '__main__':
    fonk4()