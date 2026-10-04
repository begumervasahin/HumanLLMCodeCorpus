import random
import Prime
import time
def encryption(plaintext, puk):
    return Prime.quick_pow_mod(plaintext, puk[1], puk[0])
def decryption(ciphertext, prk):
    return Prime.quick_pow_mod(ciphertext, prk[1], prk[0])
def get_RSAKey():
    RSAKey = {}
    start = time.perf_counter()
    prime_arr = Prime.get_rand_prime_arr(2)
    p = prime_arr[0]
    q = prime_arr[1]
    while p == q:
        q = random.choice(prime_arr)
    end = time.perf_counter()
    n = p * q
    s = (p - 1) * (q - 1)
    a = 65537
    b = Prime.mod_inverse(a, s)
    print("éæºçæçç´ æ°p =", p)
    print("éæºçæçç´ æ°q =", q)
    print('ç´ æ°çæçæ¶é´ä¸ºï¼', end - start, 's')
    print("n = pq =", n)
    print("å©ç¨Euclideanç®æ³çæçç§é¥a =", a)
    print("å©ç¨æ©å±Euclideanç®æ³çæçå
¬é¥b =", b)
    puk = [n, a]
    prk = [n, b]
    RSAKey['puk'] = puk
    RSAKey['prk'] = prk
    return RSAKey
if __name__ == '__main__':
    RSAKey = get_RSAKey()
    print('è¯·è¾å
¥ææï¼')
    m = int(input())
    c = encryption(m, RSAKey['puk'])
    print("RSAå å¯åçå¯æä¸º:", c)
    m1 = decryption(c, RSAKey['prk'])
    print("RSAè§£å¯åçå¯æä¸º:", m1)
    if m == m1:
        print('è§£å¯æå')
    sumEnTime = 0
    sumDeTime = 0
    for i in range(10):
        print('è¯·è¾å
¥ææï¼')
        m = int(input())
        start = time.perf_counter()
        c = encryption(m, RSAKey['puk'])
        end = time.perf_counter()
        sumEnTime = sumEnTime + (end - start)
        print("RSAå å¯åçå¯æä¸º:", c)
        start = time.perf_counter()
        m1 = decryption(c, RSAKey['prk'])
        end = time.perf_counter()
        sumDeTime = sumDeTime + (end - start)
        print("RSAè§£å¯åçå¯æä¸º:", m1)
    print('10ç»ææçRSAå å¯æ¶é´ä¸ºï¼', sumEnTime)
    print('10ç»ææçRSAè§£å¯æ¶é´ä¸ºï¼', sumDeTime)