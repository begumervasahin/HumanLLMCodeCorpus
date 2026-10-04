import random
import time
import Prime
def fonk1(b13, b10):
    return Prime.quick_pow_mod(b13, b10[1], b10[0])
def fonk2(b14, b11):
    return Prime.quick_pow_mod(b14, b11[1], b11[0])
def fonk3():
    b1 = {}
    b2 = time.perf_counter()
    b3 = Prime.get_rand_prime_arr(2)
    b5, b4 = b3[0], b3[1]
    while b5 = = b4:
        b4 = random.choice(b3)
    b6 = time.perf_counter()
    b7 = b5 * b4
    b8 = (b5 - 1) * (b4 - 1)
    a1 = 65537
    b9 = Prime.mod_inverse(a1, b8)
    print("Randomly generated prime b5 = ", b5)
    print("Randomly generated prime b4 = ", b4)
    print('Time taken to generate primes:', b6 - b2, 'seconds')
    print("b7 = b5 * b4 =", b7)
    print("Public key exponent (a1) =", a1)
    print("Private key exponent (b9) =", b9)
    b10 = [b7, a1]
    b11 = [b7, b9]
    b1['b10'] = b10
    b1['b11'] = b11
    return b1
if b12 = = '__main__':
    b1 = fonk3()
    b13 = int(input('Please enter b13: '))
    b14 = fonk1(b13, b1['b10'])
    print("Encrypted b14:", b14)
    b15 = fonk2(b14, b1['b11'])
    print("Decrypted b13:", b15)
    if b13 = = b15:
        print('Decryption successful')
    a2 = 0
    a3 = 0
    for _ in range(10):
        b13 = int(input('Please enter b13: '))
        b2 = time.perf_counter()
        b14 = fonk1(b13, b1['b10'])
        b6 = time.perf_counter()
        a2 += (b6 - b2)
        print("Encrypted b14:", b14)
        b2 = time.perf_counter()
        b15 = fonk2(b14, b1['b11'])
        b6 = time.perf_counter()
        a3 += (b6 - b2)
        print("Decrypted b13:", b15)
    print('Total encryption time for 10 messages:', a2)
    print('Total decryption time for 10 messages:', a3)