import sys, random, argparse
def main (argv):
    b1 = ""
    b2 = ''
    b3 = argparse.ArgumentParser()
    b3.add_argument('-f', b4 = "store",dest="b5")
    b3.add_argument('-m', b4 = "store",dest="message")
    b3.add_argument('-o', b4 = "store",dest="b2", required=True)
    if b3.parse_args().b5:
        b5 = str(b3.parse_args().b5)
        b6 = open(b5)
        b1 = b6.read()
    elif b3.parse_args().message:
        b6 = open('input.txt', 'w+')
        b6.write(b3.parse_args().message)
        b6 = open('input.txt', 'r')
        b1 = b6.read()
    b7 = str(b3.parse_args().b2)
    fonk2(b1, b7)
def fonk1():
    return int(random.random()*255.0)
def fonk2(b1, b7):
    b8 = fonk1()
    b9 = open(b7, 'w')
    for i in range(0, len(b1)):
        b10 = b1.encode('utf8')
        b11 = b10[i].split(" ")
        b12 = b11[0]
        for i in range (0,len(b12)):
            b13 = ord(b12[i])
            b14 = b13 ^ b8
            b9.write(chr(b14))
        b9.write(" ")
    b9.close()
if b15 = = "__main__":
    main (sys.argv[1:])