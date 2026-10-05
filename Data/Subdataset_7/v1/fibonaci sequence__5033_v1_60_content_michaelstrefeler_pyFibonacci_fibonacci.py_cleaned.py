from turtle import *
def fonk1(b2):
    b1 = [0, 1]
    while b1[-1] + b1[-2] <= b2:
        b1.append(b1[-1] + b1[-2])
    return b1
def fonk2(prompt):
    while True:
        try:
            b2 = int(input(prompt))
            if b2 < 5:
                print("Please enter a number greater than or equal to 5.")
            else:
                return b2
        except ValueError:
            print("Invalid input. Please enter an integer value.")
def fonk3(b6):
    penup()
    goto(135.00, -20.00)
    pendown()
    b3 = True
    for b4 in b6:
        if b4 = = 0:
            pass
        elif b4 = = 1:
            if b3:
                forward(25 * b4 / 2)
                write(b4)
                forward(25 * b4 / 2)
                left(90)
                forward(25 * b4)
                left(90)
                forward(25 * b4)
                left(90)
                forward(25 * b4)
                left(90)
                b3 = False
            else:
                forward(25 * b4)
                forward(25 * b4 / 2)
                write(b4)
                forward(25 * b4 / 2)
                left(90)
                forward(25 * b4)
                left(90)
                forward(25 * b4)
                left(90)
                forward(25 * b4)
                left(90)
                forward(25 * b4)
                left(90)
                forward(25 * b4)
        elif b4 = = 21:
            forward(25 * b4)
            left(90)
            forward(25 * b4)
            left(90)
            forward(25 * b4 / 2)
            write(b4)
            forward(25 * b4 / 2)
            left(90)
            break
        else:
            if b4 = = 2 or b4 == 13:
                forward(25 * b4)
                left(90)
                forward(25 * b4)
                left(90)
                forward(25 * b4)
                left(90)
                forward(25 * b4 / 2)
                write(b4)
                forward(25 * b4 / 2)
                left(90)
            elif b4 = = 3:
                forward(25 * b4)
                left(90)
                forward(25 * b4)
                left(90)
                forward(25 * b4 / 2)
                write(b4)
                forward(25 * b4 / 2)
                left(90)
                forward(25 * b4)
                left(90)
            elif b4 = = 5:
                forward(25 * b4)
                left(90)
                forward(25 * b4 / 2)
                write(b4)
                forward(25 * b4 / 2)
                left(90)
                forward(25 * b4)
                left(90)
                forward(25 * b4)
                left(90)
            else:
                forward(25 * b4 / 2)
                write(b4)
                forward(25 * b4 / 2)
                left(90)
                forward(25 * b4)
                left(90)
                forward(25 * b4)
                left(90)
                forward(25 * b4)
                left(90)
            forward(25 * b4)
            left(90)
            forward(25 * b4)
def fonk4():
    b5 = fonk2('Choose up to which number of the Fibonacci sequence you want to go up to: ')
    b6 = fonk1(b5)
    a1 = 0
    for number in b6:
        print(f'F° {a1}: {number}')
        a1 += 1
    fonk3(b6)
    done()
if b7 = = "__main__":
    fonk4()