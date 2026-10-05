from turtle import *
b1 = input('Choose up to which number of the fibonacci sequence you want to go up to: ')
while not b1.isdecimal():
    b1 = input('Please write a number (min 5): ')
b1 = int(b1)
while b1 < 5:
    b1 = input('Please write a number bigger than 4: ')
    if b1.isdecimal():
        b1 = int(b1)
b2 = []
for b3 in range(0, int(b1)):
    if b3 = = 0:
        b2.append(b3)
    elif b3 = = 1:
        b2.append(b3)
    else:
        b4 = b2[b3-1] + b2[b3-2]
        b2.append(b4)
a1 = 0
for number in b2:
    print('FÂ°', a1, ': ', number)
    a1 += 1
penup()
goto(135.00, -20.00)
pendown()
b5 = True
for b6 in b2:
    if b6 = = 0:
        pass
    elif b6 = = 1:
        if b5:
            forward(25 * b6 / 2)
            write(b6)
            forward(25 * b6 / 2)
            left(90)
            forward(25 * b6)
            left(90)
            forward(25 * b6)
            left(90)
            forward(25 * b6)
            left(90)
            b5 = False
        else:
            forward(25 * b6)
            forward(25 * b6 / 2)
            write(b6)
            forward(25 * b6 / 2)
            left(90)
            forward(25 * b6)
            left(90)
            forward(25 * b6)
            left(90)
            forward(25 * b6)
            left(90)
            forward(25 * b6)
            left(90)
            forward(25 * b6)
    elif b6 = = 21:
        forward(25 * b6)
        left(90)
        forward(25 * b6)
        left(90)
        forward(25 * b6 / 2)
        write(b6)
        forward(25 * b6 / 2)
        left(90)
        break
    else:
        if b6 = = 2 or b6 == 13:
            forward(25 * b6)
            left(90)
            forward(25 * b6)
            left(90)
            forward(25 * b6)
            left(90)
            forward(25 * b6 / 2)
            write(b6)
            forward(25 * b6 / 2)
            left(90)
        elif b6 = = 3:
            forward(25 * b6)
            left(90)
            forward(25 * b6)
            left(90)
            forward(25 * b6 / 2)
            write(b6)
            forward(25 * b6 / 2)
            left(90)
            forward(25 * b6)
            left(90)
        elif b6 = = 5:
            forward(25 * b6)
            left(90)
            forward(25 * b6 / 2)
            write(b6)
            forward(25 * b6 / 2)
            left(90)
            forward(25 * b6)
            left(90)
            forward(25 * b6)
            left(90)
        else:
            forward(25 * b6 / 2)
            write(b6)
            forward(25 * b6 / 2)
            left(90)
            forward(25 * b6)
            left(90)
            forward(25 * b6)
            left(90)
            forward(25 * b6)
            left(90)
        forward(25 * b6)
        left(90)
        forward(25 * b6)
penup()
goto(135.00, 5.00)
pendown()
color('red')
shape('turtle')
pensize(2)
setheading(180)
for b3 in range(len(b2)):
    if b3 < 9:
        circle(25 * b2[b3], 90)
    else:
        break
done()