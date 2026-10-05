import random
b1 = []
b2 = []
b3 = []
b4 = []
b5 = ""
b6 = open("b4.txt","r")
b4 = b6.readlines()
b6.close()
b7 = open("b1.txt","r")
b1 = b7.readlines()
b7.close()
b8 = open("b2.txt","r")
b2 = b8.readlines()
b8.close()
b9 = open("b3.txt","r")
b3 = b9.readlines()
b9.close()
while True:
    try:
        b10 = int(input("How many sentences do you want to generate? "))
        break
    except:
        print("Wrong input, use integer numbers!")
for i in range(b10):
    b5 = "A "+b3[random.randrange(len(b3))].strip() + \
          " "+b2[random.randrange(len(b2))].strip() + " " +\
          b4[random.randrange(len(b4))].strip() + " a " + \
          b3[random.randrange(len(b3))].strip() + \
          " " + b2[random.randrange(len(b2))].strip() + " " +\
          b1[random.randrange(len(b1))].strip()+"."
    print(b5)