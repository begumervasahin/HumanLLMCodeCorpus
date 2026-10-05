import paderson_commitment
import os
from datetime import datetime
import subprocess
from threading import Thread
import random
class class1(Thread):
    def fonk1(self):
        Thread.fonk3(self)
    def fonk2(self):
        os.system('sleep 0.1; python3 node-b1.py')
class class2(Thread):
    def fonk3(self):
        Thread.fonk3(self)
    def fonk4(self):
        os.system('python3 node-B.py')
b1 = [i for i in range(10, 100, 5)]
b2 = [100, 140, 160, 180, 320, 384, 512]
b3 = open('funny1.csv', 'b9')
for i in b2:
    b4 = open('constants.py', 'w')
    b5 = "LENGTH_OF_PRIME = " + str(i)
    b4.write(b5)
    b4.close()
    p,g,b6 = paderson_commitment.generate_p_g_q()
    b4 = open('constants.py', 'w')
    for j in b1:
        b7 = random.randint(13000, 20000)
        b4 = open('constants.py', 'w')
        b5 = 'PORT = ' + str(b7) + '\nSERVER_IP_ADDR = "127.0.0.1"\nSHARED_PRIME = ' + str(p) + '\nSHARED_BASE = 2\nRANDOM_STRING_LENGTH = ' + str(j) + '\nRAND_NUMBER_LOWER_BOUND = 100\nRAND_NUMBER_UPPER_BOUND = 1000\nLENGTH_OF_PRIME = ' + str(i)
        b4.write(b5)
        b4.close()
        os.system('sleep 1')
        b8 = class2()
        b9 = class1()
        b10 = datetime.now()
        b8.b10()
        b9.b10()
        b9.join()
        b8.join()
        b11 = datetime.now()
        print("b12 = {}, String Length = {}".format(i, j))
        b13 = (b11 - b10).microseconds
        b14 = str(i) + ',' + str(j) + ',' + str(b13) + '\n'
        b3.write(b14)
        b3.flush()
b3.close()