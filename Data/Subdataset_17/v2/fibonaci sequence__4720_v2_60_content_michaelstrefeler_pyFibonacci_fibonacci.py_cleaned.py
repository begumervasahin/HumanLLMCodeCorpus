from turtle import *
def get_fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence
def draw_fibonacci_spiral(sequence):
    penup()
    goto(135, -20)
    pendown()
    first_one = True
    for fib in sequence:
        if fib == 0:
            continue
        if fib == 1:
            draw_square(fib, first_one)
            first_one = False
        elif fib == 21:
            draw_final_square(fib)
            break
        else:
            draw_special_squares(fib)
    draw_spiral(sequence)
    done()
def draw_square(fib, first_one):
    if first_one:
        forward(25 * fib / 2)
    else:
        forward(25 * fib)
    write(fib)
    forward(25 * fib / 2)
    left(90)
    for _ in range(3):
        forward(25 * fib)
        left(90)
def draw_final_square(fib):
    forward(25 * fib)
    left(90)
    forward(25 * fib)
    left(90)
    forward(25 * fib / 2)
    write(fib)
    forward(25 * fib / 2)
    left(90)
def draw_special_squares(fib):
    if fib in [2, 13]:
        draw_special_pattern(fib, "left")
    elif fib == 3:
        draw_special_pattern(fib, "bottom")
    elif fib == 5:
        draw_special_pattern(fib, "top")
    else:
        draw_standard_square(fib)
def draw_special_pattern(fib, direction):
    forward(25 * fib)
    left(90)
    forward(25 * fib)
    left(90)
    if direction == "left":
        forward(25 * fib)
        left(90)
        forward(25 * fib / 2)
    elif direction == "bottom":
        forward(25 * fib / 2)
        left(90)
        forward(25 * fib)
    elif direction == "top":
        forward(25 * fib / 2)
    write(fib)
    forward(25 * fib / 2)
    left(90)
def draw_standard_square(fib):
    forward(25 * fib / 2)
    write(fib)
    forward(25 * fib / 2)
    left(90)
    for _ in range(3):
        forward(25 * fib)
        left(90)
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
def main():
    while True:
        amount = input('Choose up to which number of the Fibonacci sequence you want to go up to (min 5): ')
        if amount.isdecimal() and int(amount) >= 5:
            amount = int(amount)
            break
        print('Please enter a number bigger than 4.')
    fibonacci_sequence = get_fibonacci_sequence(amount)
    for index, number in enumerate(fibonacci_sequence):
        print(f'F°{index}: {number}')
    draw_fibonacci_spiral(fibonacci_sequence)
if __name__ == "__main__":
    main()