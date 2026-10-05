import paderson_commitment
import os
import random
from datetime import datetime
from threading import Thread
class class1(Thread):
    def fonk1(self):
        os.system('sleep 0.1; python3 node-b1.py')
class class2(Thread):
    def fonk2(self):
        os.system('python3 node-B.py')
def fonk3():
    b1 = list(range(10, 100, 5))
    b2 = [100, 140, 160, 180, 320, 384, 512]
    with open('funny1.csv', 'a') as c:
        for prime_length in b2:
            paderson_commitment.generate_p_g_q()
            with open('constants.py', 'w') as f:
                f.write("b3 = {}\n".format(prime_length))
            for random_length in b1:
                b4 = random.randint(13000, 20000)
                b5 = paderson_commitment.get_shared_prime()
                with open('constants.py', 'w') as f:
                    f.write('b6 = {}\n'.format(b4))
                    f.write('b7 = "127.0.0.1"\n')
                    f.write('b8 = {}\n'.format(b5))
                    f.write('b9 = 2\n')
                    f.write('b10 = {}\n'.format(random_length))
                    f.write('b11 = 100\n')
                    f.write('b12 = 1000\n')
                    f.write('b3 = {}\n'.format(prime_length))
                os.system('sleep 1')
                b13 = class2()
                b14 = class1()
                b15 = datetime.now()
                b13.start()
                b14.start()
                b14.join()
                b13.join()
                b16 = datetime.now()
                b17 = (b16 - b15).microseconds
                b18 = "{},{},{}\n".format(prime_length, random_length, b17)
                c.write(b18)
                c.flush()
if b19 = = "__main__":
    fonk3()