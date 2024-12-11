import hashlib
import sys
b1 = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF
a1 = 2
def fonk1(exponent, public_key_victim):
    b2 = '{:x}'.format(pow(public_key_victim, exponent, b1))
    b3 = hashlib.sha512(b2.encode())
    b4 = b3.hexdigest()
    return b4
class class1:
    def fonk2(self):
        self.b5 = b1
        self.b6 = a1
    def fonk3(self, public_key_victim1, public_key_victim2, num_cpus, collision_number):
        b7 = num_cpus * 2
        def fonk4(x):
            return fonk1(x, public_key_victim1)
        def fonk5(x):
            return fonk1(x, public_key_victim2)
        b8 = []
        b9 = []
        a2 = 1
        while True:
            a2 += b7
            b8.append(fonk4(a2))
            b9.append(fonk5(a2 + 1))
            b10 = len(b9)
            for n in range(b10 - 1):
                if b8[n][:collision_number] == b9[b10 - 1][:collision_number]:
                    b11 = b8[n]
                    b12 = b9[b10 - 1]
                    b13 = (n + 1) * 2 + 1
                    b14 = (b10) * 2 + 2
                    return b13, b14
            for m in range(b10 - 1):
                if b9[m][:collision_number] == b8[b10 - 1][:collision_number]:
                    b15 = b8[b10 - 1]
                    b16 = b9[m]
                    b14 = (m + 1) * 2 + 2
                    b13 = (b10) * 2 + 1
                    return b13, b14
if b17 = = '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <b18> <b19>")
        sys.exit(1)
    b18 = int(sys.argv[1], 16)
    b19 = int(sys.argv[2], 16)
    b20 = class1()
    b13, b14 = b20.fonk3(b18, b19, 1, 7)
    print("\nStarting the Birthday Attack to get the first 7 characters equal..")
    print("If you would like to try more characters with a stronger machine..")
    print("Look in the __main__ function at the end of code and change according to the comment\n")
    print("The private key for the exchange with Alice:", hex(b13))
    print("The generated public key for Alice:", fonk1(b13, b18))
    print("The private key for the exchange with Bob:", hex(b14))
    print("The generated public key for Bob:", fonk1(b14, b19))