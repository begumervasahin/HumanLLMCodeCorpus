import random
import time
import Prime
def fonk1(b11, b9):
    b7, b1 = b9
    return Prime.quick_pow_mod(b11, b1, b7)
def fonk2(b12, b10):
    b7, b2 = b10
    return Prime.quick_pow_mod(b12, b2, b7)
def fonk3():
    b3 = time.perf_counter()
    b5, b4 = Prime.get_rand_prime_arr(2)
    while b5 = = b4:
        b4 = random.choice(Prime.get_rand_prime_arr(2))
    b6 = time.perf_counter()
    b7 = b5 * b4
    b8 = (b5 - 1) * (b4 - 1)
    b1 = 65537
    b2 = Prime.mod_inverse(b1, b8)
    print(f"éæºçæçç´ æ° b5 = {b5}")
    print(f"éæºçæçç´ æ° b4 = {b4}")
    print(f'ç´ æ°çæçæ¶é´ä¸ºï¼ {b6 - b3} s')
    print(f"b7 = b5 * b4 = {b7}")
    print(f"å©ç¨Euclideanç®æ³çæçå
¬é¥ b1 = {b1}")
    print(f"å©ç¨æ©å±Euclideanç®æ³çæçç§é¥ b2 = {b2}")
    b9 = (b7, b1)
    b10 = (b7, b2)
    return b9, b10
def fonk4():
    b9, b10 = fonk3()
    print('è¯·è¾å
¥ææï¼')
    b11 = int(input())
    b12 = fonk1(b11, b9)
    print(f"RSAå å¯åçå¯æä¸º: {b12}")
    b13 = fonk2(b12, b10)
    print(f"RSAè§£å¯åçææä¸º: {b13}")
    if b11 = = b13:
        print('è§£å¯æå')
    a1 = 0
    a2 = 0
    for _ in range(10):
        print('è¯·è¾å
¥ææï¼')
        b11 = int(input())
        b3 = time.perf_counter()
        b12 = fonk1(b11, b9)
        b6 = time.perf_counter()
        a1 += (b6 - b3)
        print(f"RSAå å¯åçå¯æä¸º: {b12}")
        b3 = time.perf_counter()
        b13 = fonk2(b12, b10)
        b6 = time.perf_counter()
        a2 += (b6 - b3)
        print(f"RSAè§£å¯åçææä¸º: {b13}")
    print(f'10ç»ææçRSAå å¯æ¶é´ä¸ºï¼ {a1}')
    print(f'10ç»ææçRSAè§£å¯æ¶é´ä¸ºï¼ {a2}')
if b14 = = '__main__':
    fonk4()