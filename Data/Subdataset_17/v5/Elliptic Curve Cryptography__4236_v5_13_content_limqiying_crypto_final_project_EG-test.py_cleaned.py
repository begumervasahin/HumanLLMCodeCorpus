from ecc_simple import *
import random
def elgamal_encrypt(message, public_key_bob, private_key_alice, base_point):
    shared_key_alice = times(private_key_alice, public_key_bob)
    c1 = times(private_key_alice, base_point)
    c2 = add(encode(message, 100), shared_key_alice)
    return c1, c2
def elgamal_decrypt(ciphertext, private_key_bob):
    c1, c2 = ciphertext
    shared_key_bob = times(private_key_bob, c1)
    plaintext = subtract(c2, shared_key_bob)
    decrypted_message = decode(plaintext, 100)
    return decrypted_message
def main():
    set_p256_param()
    p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
    x = 48439561293906451759052585252797914202762949526041747995844080717082404635286
    y = 36134250956749795798585127919587881956611106672985015071877198253568414405109
    base_point = (x, y)
    private_key_alice = random.randrange(1, p)
    private_key_bob = random.randrange(1, p)
    public_key_alice = times(private_key_alice, base_point)
    public_key_bob = times(private_key_bob, base_point)
    message = 32454324564335645345643
    ciphertext = elgamal_encrypt(message, public_key_bob, private_key_alice, base_point)
    decrypted_message = elgamal_decrypt(ciphertext, private_key_bob)
    print("Decrypted message:", decrypted_message)
if __name__ == "__main__":
    main()