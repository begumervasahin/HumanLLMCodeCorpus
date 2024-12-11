from turtle import *
b1 = input('Choose up to which number of the Fibonacci sequence you want to go up to: ')
while not b1.isdecimal() or int(b1) < 5:
    b1 = input('Please write a number greater than or equal to 5: ')
b1 = int(b1)
b2 = [0, 1]
while len(b2) < b1:
    b3 = b2[-1] + b2[-2]
    b2.append(b3)
for index, number in enumerate(b2):
    print(f'Fibonacci {index}: {number}')
penup()
goto(135.00, -20.00)
pendown()
b4 = True
for b5 in b2:
    if b5 = = 0:
        pass
    elif b5 = = 1:
        if b4:
            forward(12.5)
            write(b5)
            forward(12.5)
            left(90)
            forward(25)
            left(90)
            forward(25)
            left(90)
            forward(25)
            left(90)
            b4 = False
        else:
            forward(25)
            forward(12.5)
            write(b5)
            forward(12.5)
            left(90)
            forward(25)
            left(90)
            forward(25)
            left(90)
            forward(25)
            left(90)
            forward(25)
    else:
        forward(12.5 * b5)
        left(90)
        forward(12.5 * b5)
        left(90)
        forward(12.5)
        write(b5)
        forward(12.5)
        left(90)
penup()
goto(135.00, 5.00)
pendown()
color('red')
shape('turtle')
pensize(2)
setheading(180)
for i in range(len(b2)):
    if i < 9:
        circle(12.5 * b2[i], 90)
    else:
        break
done()