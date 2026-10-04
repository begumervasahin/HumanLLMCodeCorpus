
from b1 import RSA
from convertN2T import str2num, num2block, block2num, num2str
def fonk1():
    print('================== - Criptografia RSA - ======================')
    a1 = 15
    b1 = RSA()
    with open("original_msg", "r") as msg_file:
        b2 = msg_file.read()
    print('================== -------------------- ======================')
    b3 = str2num(b2)
    print('\nMensagem original')
    print(b2)
    print('\n---------------------------')
    print(b3)
    b4 = num2block(b3, a1)
    b5 = b1.encryption(b4)
    print("--------------------------")
    b6 = b1.decryption(b5)
    b3 = block2num(b6, a1)
    print('---------- Voltando numero para string----------------\n')
    b7 = num2str(b3)
    print(b7)
if b8 = = '__main__':
    fonk1()