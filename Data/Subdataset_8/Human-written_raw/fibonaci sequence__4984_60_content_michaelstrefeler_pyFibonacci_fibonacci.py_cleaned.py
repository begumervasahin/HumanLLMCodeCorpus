from turtle import *
amount = input('Choose up to which number of the fibonacci sequence you want to go up to: ')
while not amount.isdecimal():
    amount = input('Please write a number (min 5): ')
amount = int(amount)
while amount < 5:
    amount = input('Please write a number bigger than 4: ')
    if amount.isdecimal():
        amount = int(amount)
myFibonacci = []
for i in range(0, int(amount)):
    if i == 0:
        myFibonacci.append(i)
    elif i == 1:
        myFibonacci.append(i)
    else:
        next_number = myFibonacci[i-1] + myFibonacci[i-2]
        myFibonacci.append(next_number)
index = 0
for number in myFibonacci:
    print('FÂ°', index, ': ', number)
    index += 1
penup()
goto(135.00, -20.00)
pendown()
first_one = True
for fib in myFibonacci:
    if fib == 0:
        pass
    elif fib == 1:
        if first_one:
            forward(25 * fib / 2)
            write(fib)
            forward(25 * fib / 2)
            left(90)
            forward(25 * fib)
            left(90)
            forward(25 * fib)
            left(90)
            forward(25 * fib)
            left(90)
            first_one = False
        else:
            forward(25 * fib)
            forward(25 * fib / 2)
            write(fib)
            forward(25 * fib / 2)
            left(90)
            forward(25 * fib)
            left(90)
            forward(25 * fib)
            left(90)
            forward(25 * fib)
            left(90)
            forward(25 * fib)
            left(90)
            forward(25 * fib)
    elif fib == 21:
        forward(25 * fib)
        left(90)
        forward(25 * fib)
        left(90)
        forward(25 * fib / 2)
        write(fib)
        forward(25 * fib / 2)
        left(90)
        break
    else:
        if fib == 2 or fib == 13:
            forward(25 * fib)
            left(90)
            forward(25 * fib)
            left(90)
            forward(25 * fib)
            left(90)
            forward(25 * fib / 2)
            write(fib)
            forward(25 * fib / 2)
            left(90)
        elif fib == 3:
            forward(25 * fib)
            left(90)
            forward(25 * fib)
            left(90)
            forward(25 * fib / 2)
            write(fib)
            forward(25 * fib / 2)
            left(90)
            forward(25 * fib)
            left(90)
        elif fib == 5:
            forward(25 * fib)
            left(90)
            forward(25 * fib / 2)
            write(fib)
            forward(25 * fib / 2)
            left(90)
            forward(25 * fib)
            left(90)
            forward(25 * fib)
            left(90)
        else:
            forward(25 * fib / 2)
            write(fib)
            forward(25 * fib / 2)
            left(90)
            forward(25 * fib)
            left(90)
            forward(25 * fib)
            left(90)
            forward(25 * fib)
            left(90)
        forward(25 * fib)
        left(90)
        forward(25 * fib)
penup()
goto(135.00, 5.00)
pendown()
color('red')
shape('turtle')
pensize(2)
setheading(180)
for i in range(len(myFibonacci)):
    if i < 9:
        circle(25 * myFibonacci[i], 90)
    else:
        break
done()