import hashlib
import sys
b1 = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF
a1 = 2
def fonk1(e, pk_victim):
    b2 = '{:x}'.format(pow(pk_victim, e, b1))
    b3 = hashlib.sha512(b2.encode())
    b4 = b3.hexdigest()
    return b4
class class1:
    def fonk2(self):
        self.b5 = b1
        self.b6 = a1
    def fonk3(self, pk_victim1, pk_victim2, numberCPUs, collisionnumber):
        b7 = numberCPUs * 2
        def fonk4(x):
            return fonk1(x, pk_victim1)
        def fonk5(x):
            return fonk1(x, pk_victim2)
        b8 = True
        b9 = []
        b10 = []
        a2 = 1
        while b8 = = True:
            a2 += b7
            b9.append(fonk4(a2))
            b10.append(fonk5(a2 + 1))
            b11 = len(b10)
            for n in range(b11 - 1):
                if b9[n][:collisionnumber] == b10[b11 - 1][:collisionnumber]:
                    b12 = b9[n]
                    b13 = b10[b11 - 1]
                    b14 = (n + 1) * 2 + 1
                    b15 = (b11) * 2 + 2
                    b8 = False
            for m in range(b11 - 1):
                if b10[m][:collisionnumber] == b9[b11 - 1][:collisionnumber]:
                    b16 = b9[b11 - 1]
                    b17 = b10[m]
                    b15 = (m + 1) * 2 + 2
                    b14 = (b11) * 2 + 1
                    b8 = False
        return b14, b15
if b18 = = '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <private_key_A> <private_key_B>")
        sys.exit(1)
    b19 = int(sys.argv[1], 16)
    b20 = int(sys.argv[2], 16)
    b21 = class1()
    b14, b15 = b21.fonk3(b19, b20, 1, 7)
    print("\nStarting the Birthday Attack to get the first 7 characters equal..")
    print("If you would like to try more characters with a stronger machine..")
    print("Look in the __main__ function at the end of code and change according to the comment\n")
    print("The private key for the exchange with Alice:", hex(b14))
    print("The generated public key for Alice:", fonk1(b14, b19))
    print("The private key for the exchange with Bob:", hex(b15))
    print("The generated public key for Bob:", fonk1(b15, b20))