import csv
import time
from myQueue import MyQueue
from myStack import MyStack
def fonk1():
    b1 = MyStack()
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    a5 = 0
    a6 = 0
    with open('output/stack_output.txt', 'w+') as output_file:
        output_file.write("Stack:\n\nResults from MyStack implementation:\n\n")
        with open("input/stack_input.txt") as f:
            b2 = csv.b2(f, delimiter=',')
            for row in b2:
                b3 = row[0]
                b4 = row[1] if len(row) > 1 else None
                if b3 = = 'Push':
                    b5 = time.time()
                    b1.push(b4)
                    a4 += time.time() - b5
                    a1 += 1
                elif b3 = = 'Pop':
                    b5 = time.time()
                    if b1.top:
                        output_file.write(f'Item {b1.pop()} popped\n')
                    else:
                        output_file.write('Cannot pop from an empty stack\n')
                    a5 += time.time() - b5
                    a2 += 1
                elif b3 = = 'getMax':
                    b5 = time.time()
                    b6 = b1.get_max() if b1.get_max else 'undefined'
                    output_file.write(f'Max b4 is {b6}\n')
                    a6 += time.time() - b5
                    a3 += 1
        b7 = a1 + a2 + a3
        b8 = a4 + a5 + a6
        if a1 > 0:
            b9 = fonk3(a4, a1) * 1000
            output_file.write(f'Average time for push operations: {b9:.3f} ms\n')
        if a2 > 0:
            b10 = fonk3(a5, a2) * 1000
            output_file.write(f'Average time for pop operations: {b10:.3f} ms\n')
        if a3 > 0:
            b11 = fonk3(a6, a3) * 1000
            output_file.write(f'Average time for getMax operations: {b11:.3f} ms\n')
        output_file.write(f'\nTime for executing all the {b7} push, pop, and getMax operations: {b8 * 1000:.4f} ms\n')
def fonk2():
    b12 = MyQueue()
    a7 = 0
    a8 = 0
    a9 = 0
    a10 = 0
    with open('output/queue_output.txt', 'w+') as output_file:
        output_file.write('Queue:\n\nResults from MyQueue implementation:\n\n')
        with open("input/queue_input.txt") as f:
            b2 = csv.b2(f, delimiter=',')
            for row in b2:
                b3 = row[0]
                b4 = row[1] if len(row) > 1 else None
                if b3 = = 'Enqueue':
                    b5 = time.time()
                    b12.enqueue(b4)
                    a8 += time.time() - b5
                    a7 += 1
                elif b3 = = 'Dequeue':
                    b5 = time.time()
                    b13 = b12.dequeue()
                    output_file.write(f'Item {b13} dequeued\n')
                    a10 += time.time() - b5
                    a9 += 1
        b7 = a7 + a9
        b8 = a8 + a10
        if a7 > 0:
            b14 = fonk3(a8, a7) * 1000
            output_file.write(f'Average time for enqueue operations: {b14:.3f} ms\n')
        if a9 > 0:
            b15 = fonk3(a10, a9) * 1000
            output_file.write(f'Average time for dequeue operations: {b15:.3f} ms\n')
        output_file.write(f'\nTime for executing the sequence of {b7} enqueue and dequeue operations: {b8 * 1000:.4f} ms\n')
def fonk3(b8, count):
    return b8 / count
if b16 = = '__main__':
    fonk1()
    fonk2()