import hashlib
import sys
PRIME = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF
GENERATOR = 2
def generate_shared_key(e, pk_victim):
    shared_sec_victim = '{:x}'.format(pow(pk_victim, e, PRIME))
    hash_victim = hashlib.sha512(shared_sec_victim.encode())
    key_victim = hash_victim.hexdigest()
    return key_victim
class DiffieHellAttack:
    def __init__(self):
        self.prime = PRIME
        self.generator = GENERATOR
    def birthday_attack(self, pk_victim1, pk_victim2, number_cpus, collision_number):
        iteration_number = number_cpus * 2
        def generate_shared_key_pk1(x):
            return generate_shared_key(x, pk_victim1)
        def generate_shared_key_pk2(x):
            return generate_shared_key(x, pk_victim2)
        z = True
        compare_table1 = []
        compare_table2 = []
        i = 1
        while z:
            i += iteration_number
            compare_table1.append(generate_shared_key_pk1(i))
            compare_table2.append(generate_shared_key_pk2(i + 1))
            l = len(compare_table2)
            for n in range(l - 1):
                if compare_table1[n][:collision_number] == compare_table2[l - 1][:collision_number]:
                    out11 = compare_table1[n]
                    out12 = compare_table2[l - 1]
                    out_num1 = (n + 1) * 2 + 1
                    out_num2 = (l) * 2 + 2
                    z = False
            for m in range(l - 1):
                if compare_table2[m][:collision_number] == compare_table1[l - 1][:collision_number]:
                    out21 = compare_table1[l - 1]
                    out22 = compare_table2[m]
                    out_num2 = (m + 1) * 2 + 2
                    out_num1 = (l) * 2 + 1
                    z = False
        return out_num1, out_num2
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <private_key_A> <private_key_B>")
        sys.exit(1)
    A = int(sys.argv[1], 16)
    B = int(sys.argv[2], 16)
    DHA = DiffieHellAttack()
    out_num1, out_num2 = DHA.birthday_attack(A, B, 1, 7)
    print("\nStarting the Birthday Attack to get the first 7 characters equal..")
    print("If you would like to try more characters with a stronger machine..")
    print("Look in the __main__ function at the end of code and change according to the comment\n")
    print("The private key for the exchange with Alice:", hex(out_num1))
    print("The generated public key for Alice:", generate_shared_key(out_num1, A))
    print("The private key for the exchange with Bob:", hex(out_num2))
    print("The generated public key for Bob:", generate_shared_key(out_num2, B))