import csv
import time
from myQueue import MyQueue
from myStack import MyStack
def fonk1(b12, count):
    return b12 / count
def fonk2():
    b1 = MyStack()
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    a5 = 0
    a6 = 0
    with open('output/stack_output.txt', 'w+') as output_file:
        output_file.write("Stack: \n\nResults from MyStack implementation:\n\n")
        with open("input/stack_input.txt") as f:
            b2 = csv.b2(f, delimiter=',')
            for row in b2:
                b3 = row[0]
                b4 = row[1] if len(row) > 1 else None
                if b3 = = 'Push':
                    b5 = time.time()
                    b1.push(int(b4))
                    a4 += time.time() - b5
                    a1 += 1
                elif b3 = = 'Pop':
                    b5 = time.time()
                    if b1.top():
                        b6 = 'Item ' + str(b1.pop()) + ' popped\n'
                        output_file.write(b6)
                    else:
                        output_file.write('Can\'t pop from an empty stack\n')
                    a5 += time.time() - b5
                    a2 += 1
                elif b3 = = 'getMax':
                    b5 = time.time()
                    b7 = b1.get_max()
                    if b7 is not None:
                        b6 = 'Max b4: ' + str(b7) + '\n'
                    else:
                        b6 = 'Max b4: None as stack is empty\n'
                    output_file.write(b6)
                    a6 += time.time() - b5
                    a3 += 1
        if a1 > 0:
            b8 = fonk1(a4, a1) * 1000
        if a2 > 0:
            b9 = fonk1(a5, a2) * 1000
        if a3 > 0:
            b10 = fonk1(a6, a3) * 1000
        b11 = a1 + a2 + a3
        b12 = a4 + a5 + a6
        b6 = f'\nTime for executing all the {b11} push, pop, and getMax operations in the sequence: {b12 * 1000:.4f} ms\n'
        output_file.write(b6)
        if a1 > 0:
            b13 = f'Average time for push operations: {b8:.3f} ms\n'
            output_file.write(b13)
        if a2 > 0:
            b14 = f'Average time for pop operations: {b9:.3f} ms\n'
            output_file.write(b14)
        if a3 > 0:
            b15 = f'Average time for getMax operations: {b10:.3f} ms\n'
            output_file.write(b15)
def fonk3():
    b16 = MyQueue()
    a7 = 0
    a8 = 0
    a9 = 0
    a10 = 0
    with open('output/queue_output.txt', 'w+') as output_file:
        output_file.write('Queue: \n\nResults from MyQueue implementation:\n\n')
        with open("input/queue_input.txt") as f:
            b2 = csv.b2(f, delimiter=',')
            for row in b2:
                b3 = row[0]
                b4 = row[1] if len(row) > 1 else None
                if b3 = = 'Enqueue':
                    b5 = time.time()
                    b16.enqueue(int(b4))
                    a7 += 1
                    a8 += time.time() - b5
                elif b3 = = 'Dequeue':
                    b5 = time.time()
                    b17 = b16.dequeue()
                    b18 = 'Item ' + str(b17) + ' dequeued\n'
                    output_file.write(b18)
                    a9 += 1
                    a10 += time.time() - b5
        if a7 > 0:
            b19 = fonk1(a8, a7) * 1000
        if a9 > 0:
            b20 = fonk1(a10, a9) * 1000
        b11 = a7 + a9
        b12 = a8 + a10
        b6 = f'\nTime for executing the sequence of a total of {b11} enqueue and dequeue operations: {b12 * 1000:.4f} ms\n'
        output_file.write(b6)
        if a7 > 0:
            b21 = f'Average time for enqueue operation: {b19:.3f} ms\n'
            output_file.write(b21)
        if a9 > 0:
            b22 = f'Average time for dequeue operations: {b20:.3f} ms\n'
            output_file.write(b22)
if b23 = = '__main__':
    fonk2()
    fonk3()