from turtle import *
def get_fibonacci_sequence(n):
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence
def draw_square(size, label):
    for _ in range(2):
        forward(25 * size)
        write(label)
        forward(25 * size)
        left(90)
    for _ in range(2):
        forward(25 * size)
        left(90)
def draw_fibonacci_spiral(sequence):
    penup()
    goto(135, -20)
    pendown()
    first_square = True
    for fib in sequence:
        if fib == 0:
            continue
        if fib == 1:
            if first_square:
                forward(25 * fib / 2)
                write(fib)
                forward(25 * fib / 2)
                left(90)
                first_square = False
            else:
                forward(25 * fib)
                draw_square(fib, fib)
                left(90)
        else:
            draw_square(fib, fib)
            left(90)
    draw_spiral(sequence)
def draw_spiral(sequence):
    penup()
    goto(135, 5)
    pendown()
    color('red')
    shape('turtle')
    pensize(2)
    setheading(180)
    for fib in sequence:
        if fib < 9:
            circle(25 * fib, 90)
        else:
            break
    done()
def get_valid_input():
    while True:
        amount = input('Choose up to which number of the Fibonacci sequence you want to go up to (min 5): ')
        if amount.isdecimal() and int(amount) >= 5:
            return int(amount)
        print('Please enter a number greater than or equal to 5.')
def main():
    amount = get_valid_input()
    fibonacci_sequence = get_fibonacci_sequence(amount)
    for index, number in enumerate(fibonacci_sequence):
        print(f'F°{index}: {number}')
    draw_fibonacci_spiral(fibonacci_sequence)
if __name__ == "__main__":
    main()