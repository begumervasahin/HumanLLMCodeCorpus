from ecc_simple import *
import random
def elgamal_encryption(message, public_Bob, private_Alice, g):
    shared_key_Alice = times(private_Alice, public_Bob)
    c1 = times(private_Alice, g)
    c2 = add(encode(message, 100), shared_key_Alice)
    return c1, c2
def elgamal_decryption(ciphertext, private_Bob):
    c1, c2 = ciphertext
    shared_key_Bob = times(private_Bob, c1)
    plaintext = subtract(c2, shared_key_Bob)
    decrypted_message = decode(plaintext, 100)
    return decrypted_message
def main():
    set_p256_param()
    p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
    x = 48439561293906451759052585252797914202762949526041747995844080717082404635286
    y = 36134250956749795798585127919587881956611106672985015071877198253568414405109
    g = (x, y)
    private_Alice = random.randrange(1, p)
    private_Bob = random.randrange(1, p)
    public_Alice = times(private_Alice, g)
    public_Bob = times(private_Bob, g)
    message = 32454324564335645345643
    ciphertext = elgamal_encryption(message, public_Bob, private_Alice, g)
    decrypted_message = elgamal_decryption(ciphertext, private_Bob)
    print("Decrypted message:", decrypted_message)
if __name__ == "__main__":
    main()