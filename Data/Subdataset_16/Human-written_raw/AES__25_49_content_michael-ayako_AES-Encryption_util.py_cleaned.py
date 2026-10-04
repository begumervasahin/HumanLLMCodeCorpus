import logging
import random
import io
def fonk1():
    logging.info("Configuring b2...")
    try:
        logging.basicConfig(b1 = "./chatterbot/logs%s.log"%((__file__).split(".")[0]), format='%(asctime)s %(message)s', filemode='w')
        b2 = logging.getLogger()
        b2.setLevel(logging.DEBUG)
        logging.info("Logger configured...")
    except Exception as err:
        logging.info("Logging not configured: "+err)
def fonk2(b1):
    try:
        b3 = open(b1, 'rb')
        b3.close()
        logging.info("File %s was found"%(b1))
        return
    except Exception as err:
        logging.error(err)
        exit()
def fonk3():
    print("Please select a random word from the list and share it to the reciever of this file by typing the numbers adjacent to the word")
    b4 = []
    for x in range(6):
        b5 = random.randint(10000,65535)
        print("[%s] - %s\n"%(x,b5))
        b4.append(b5)
    try:
        b6 = int(input())
        return b4[b6]
    except Exception as err:
        logging.error(err)
        exit()
def fonk4(BITSMATRIX):
    b7 = []
    for x in BITSMATRIX:
        b8 = ''
        for y in x:
            for z in y:
                b8 += str(z)
        b7.append(b8)
    b9 = []
    for x in b7:
        b9.append(chr(int(x,2)))
    with open('msg.enc','w',b10 = 'utf-8') as f:
        for x in b9:
            f.write(x)
def fonk5(BITSMATRIX):
    b7 = []
    for x in BITSMATRIX:
        b8 = ''
        for y in x:
            for z in y:
                b8 += str(z)
        b7.append(b8)
    b9 = []
    for x in b7:
        b9.append(chr(int(x,2)))
    with open('msg.txt','w',b10 = 'utf-8') as f:
        for x in b9:
            f.write(x)
def fonk6():
    logging.info("Quitting")
    exit()