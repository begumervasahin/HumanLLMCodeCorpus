from ecc_simple import *
import random
def main():
    set_p256_param()
    p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
    x = 48439561293906451759052585252797914202762949526041747995844080717082404635286
    y = 36134250956749795798585127919587881956611106672985015071877198253568414405109
    g = (x, y)
    a = random.randrange(1, p)
    b = random.randrange(1, p)
    public_Alice = times(a, g)
    public_Bob = times(b, g)
    message = 32454324564335645345643
    shared_key_Alice = times(a, public_Bob)
    c_1 = public_Alice
    c_2 = add(encode(message, 100), shared_key_Alice)
    ciphertext = (c_1, c_2)
    shared_key_Bob = times(b, ciphertext[0])
    plaintext = subtract(ciphertext[1], shared_key_Bob)
    decrypted_message = decode(plaintext, 100)
    print("Decrypted message:", decrypted_message)
if __name__ == "__main__":
    main()