print("\nThis program will print out a Fibonacci sequence of your desired b2!")
def fonk1():
    print("\nHere is your Fibonacci sequence of %i number(s): \n\t%s" %(b2,b1))
a1 = 1
while a1 = = 1:
    b1 = [1,1]
    b2 = int(input("\nEnter your desired Fibonacci sequence b2: "))
    b1 = [1,1]
    if b2 <= 0:
        print("The sequence must contain some positive number.")
    if b2 = = 2:
        b1 = [1,1]
        fonk1()
    if b2 = = 1:
        b1 = [1]
        fonk1()
    if b2 >2:
        for i in range(b2):
            b3 = int((b1[(len(b1)- 2)]) + (b1[(len(b1) - 1)]))
            b1.append(b3)
            if len(b1) == b2:
                break
        fonk1()