from turtle import *
amount = input('Choose up to which number of the Fibonacci sequence you want to go up to: ')
while not amount.isdecimal() or int(amount) < 5:
    amount = input('Please write a number greater than or equal to 5: ')
amount = int(amount)
fibonacci_sequence = [0, 1]
while len(fibonacci_sequence) < amount:
    next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_number)
for index, number in enumerate(fibonacci_sequence):
    print(f'Fibonacci {index}: {number}')
penup()
goto(135.00, -20.00)
pendown()
first_one = True
for fib in fibonacci_sequence:
    if fib == 0:
        pass
    elif fib == 1:
        if first_one:
            forward(12.5)
            write(fib)
            forward(12.5)
            left(90)
            forward(25)
            left(90)
            forward(25)
            left(90)
            forward(25)
            left(90)
            first_one = False
        else:
            forward(25)
            forward(12.5)
            write(fib)
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
        forward(12.5 * fib)
        left(90)
        forward(12.5 * fib)
        left(90)
        forward(12.5)
        write(fib)
        forward(12.5)
        left(90)
penup()
goto(135.00, 5.00)
pendown()
color('red')
shape('turtle')
pensize(2)
setheading(180)
for i in range(len(fibonacci_sequence)):
    if i < 9:
        circle(12.5 * fibonacci_sequence[i], 90)
    else:
        break
done()