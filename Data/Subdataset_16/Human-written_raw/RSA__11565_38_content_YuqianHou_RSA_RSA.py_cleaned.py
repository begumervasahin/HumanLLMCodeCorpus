import random
import Prime
import time
def fonk1(plaintext, b10):
    return Prime.quick_pow_mod(plaintext, b10[1], b10[0])
def fonk2(ciphertext, b11):
    return Prime.quick_pow_mod(ciphertext, b11[1], b11[0])
def fonk3():
    b1 = {}
    b2 = time.perf_counter()
    b3 = Prime.get_rand_prime_arr(2)
    b4 = b3[0]
    b5 = b3[1]
    while b4 = = b5:
        b5 = random.choice(b3)
    b6 = time.perf_counter()
    b7 = b4 * b5
    b8 = (b4 - 1) * (b5 - 1)
    a1 = 65537
    b9 = Prime.mod_inverse(a1, b8)
    print("éæºçæçç´ æ°b4 = ", b4)
    print("éæºçæçç´ æ°b5 = ", b5)
    print('ç´ æ°çæçæ¶é´ä¸ºï¼', b6 - b2, 'b8')
    print("b7 = pq =", b7)
    print("å©ç¨Euclideanç®æ³çæçç§é¥a1 = ", a1)
    print("å©ç¨æ©å±Euclideanç®æ³çæçå
¬é¥b9 = ", b9)
    b10 = [b7, a1]
    b11 = [b7, b9]
    b1['b10'] = b10
    b1['b11'] = b11
    return b1
if b12 = = '__main__':
    b1 = fonk3()
    print('è¯·è¾å
¥ææï¼')
    b13 = int(input())
    b14 = fonk1(b13, b1['b10'])
    print("RSAå å¯åçå¯æä¸º:", b14)
    b15 = fonk2(b14, b1['b11'])
    print("RSAè§£å¯åçå¯æä¸º:", b15)
    if b13 = = b15:
        print('è§£å¯æå')
    a2 = 0
    a3 = 0
    for i in range(10):
        print('è¯·è¾å
¥ææï¼')
        b13 = int(input())
        b2 = time.perf_counter()
        b14 = fonk1(b13, b1['b10'])
        b6 = time.perf_counter()
        a2 = a2 + (b6 - b2)
        print("RSAå å¯åçå¯æä¸º:", b14)
        b2 = time.perf_counter()
        b15 = fonk2(b14, b1['b11'])
        b6 = time.perf_counter()
        a3 = a3 + (b6 - b2)
        print("RSAè§£å¯åçå¯æä¸º:", b15)
    print('10ç»ææçRSAå å¯æ¶é´ä¸ºï¼', a2)
    print('10ç»ææçRSAè§£å¯æ¶é´ä¸ºï¼', a3)