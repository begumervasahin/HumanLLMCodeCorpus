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
def fonk3():
    b1 = [100, 140, 160, 180, 320, 384, 512]
    b2 = list(range(10, 100, 5))
    with open('funny1.csv', 'a') as csv_file:
        for prime_length in b1:
            fonk4('LENGTH_OF_PRIME', prime_length)
            p, b3, b3 = paderson_commitment.generate_p_g_q()
            for random_length in b2:
                b4 = random.randint(13000, 20000)
                fonk4('PORT', b4)
                fonk4('SHARED_PRIME', p)
                fonk4('RANDOM_STRING_LENGTH', random_length)
                os.system('sleep 1')
                b5 = datetime.now()
                fonk5()
                b6 = datetime.now()
                b7 = (b6 - b5).microseconds
                fonk6(csv_file, prime_length, random_length, b7)
def fonk4(key, value):
    with open('constants.py', 'w') as constants_file:
        constants_file.write(f"{key} = {value}\n")
def fonk5():
    b8 = class2()
    b9 = class1()
    b8.start()
    b9.start()
    b9.join()
    b8.join()
def fonk6(csv_file, prime_length, random_length, b7):
    b10 = f"{prime_length},{random_length},{b7}\n"
    csv_file.write(b10)
    csv_file.flush()
if b11 = = "__main__":
    fonk3()