import random
import secrets
import math
class RSA:
    def __init__(self):
        self.P,self.Q = self.find_2prime()
        self.N = self.P * self.Q
        self.L = ((self.P - 1) *(self.Q - 1) ) / math.gcd(self.P-1, self.Q-1)
    def judge_prime(self,n):
        if n == 2: return True
        if n == 1 or n & 1 == 0: return False
        d = (n - 1) >> 1
        while d & 1 == 0:
            d >>= 1
        for _ in range(100):
            a = random.randint(1, n - 1)
            t = d
            y = pow(a, t, n)
            while t != n - 1 and y != 1 and y != n - 1:
                y = (y * y) % n
                t <<= 1
            if y != n - 1 and t & 1 == 0:
                return False
        return True
    def find_2prime(self):
        keys = []
        while len(keys) != 2:
            rand_bit = secrets.randbits(10)
            is_prime = self.judge_prime(rand_bit)
            if is_prime:
                keys.append(rand_bit)
        return keys
    def public_key(self):
        self.E = random.randint(1,self.L)
        while math.gcd(int(self.E),int(self.L)) != 1:
            self.E = random.randint(1,self.L)
        return self.E,self.N
    def private_key(self):
        self.D = random.randint(1,self.L)
        while (self.E*self.D)%self.L != 1:
            self.D = random.randint(1,self.L)
        return self.D,self.N
def E_text(e,n,text):
    text_int = [ord(i) for i in text]
    text_int_e = [str(pow(i,e,n)) for i in text_int]
    return " ".join(text_int_e)
def D_text(d,n,e_text):
    text_s = e_text.split(" ")
    text_int_d = [pow(int(i),d,n) for i in text_s]
    text_d = [chr(i) for i in text_int_d]
    return "".join(text_d)
if __name__ == "__main__":
    rsa = RSA()
    e,n = rsa.public_key()
    d,n = rsa.private_key()
    text = input()
    enc = E_text(e,n,text)
    print(enc)
    dec = D_text(d,n,enc)
    print(dec)
    print("-----------------------------------------------------")
    print("d:{0},n:{1}".format(d,n))