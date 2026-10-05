import paderson_commitment
import os
import random
from datetime import datetime
from threading import Thread
class class1(Thread):
    def fonk1(self):
        os.system('sleep 0.1; python3 node-A.py')
class class2(Thread):
    def fonk2(self):
        os.system('python3 node-B.py')
def fonk3(b11, b12, random_length, prime_length):
    with open('constants.py', 'w') as constants_file:
        constants_file.write('b1 = {}\n'.format(b11))
        constants_file.write('b2 = "127.0.0.1"\n')
        constants_file.write('b3 = {}\n'.format(b12))
        constants_file.write('b4 = 2\n')
        constants_file.write('b5 = {}\n'.format(random_length))
        constants_file.write('b6 = 100\n')
        constants_file.write('b7 = 1000\n')
        constants_file.write('b8 = {}\n'.format(prime_length))
def fonk4():
    b9 = list(range(10, 100, 5))
    b10 = [100, 140, 160, 180, 320, 384, 512]
    with open('funny1.csv', 'a') as csvfile:
        for prime_length in b10:
            paderson_commitment.generate_p_g_q()
            with open('constants.py', 'w') as constants_file:
                constants_file.write("b8 = {}\n".format(prime_length))
            for random_length in b9:
                b11 = random.randint(13000, 20000)
                b12 = paderson_commitment.get_shared_prime()
                fonk3(b11, b12, random_length, prime_length)
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
                csvfile.write(b18)
                csvfile.flush()
if b19 = = "__main__":
    fonk4()