from argparse import ArgumentParser
def fonk1(key, b6, b7):
    return (b6 ** key) % b7
def fonk2():
    b1 = ArgumentParser()
    b1.add_argument("-b4", "--A_private_key", b2 = True)
    b1.add_argument("-b5", "--B_private_key", b2 = True)
    b1.add_argument("-b6", "--base", b2 = True)
    b1.add_argument("-b7", "--prime", b2 = True)
    b3 = b1.parse_args()
    b4 = int(b3.A_private_key)
    b5 = int(b3.B_private_key)
    b6 = int(b3.base)
    b7 = int(b3.prime)
    b8 = fonk1(b4, b6, b7)
    b9 = fonk1(b5, b6, b7)
    b10 = fonk1(b4, b9, b7)
    b11 = fonk1(b5, b8, b7)
    print('Shared secret: {}'.format(b10))
    pass
if b12 = = '__main__':
    fonk2()