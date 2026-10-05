from myQueue import MyQueue
from myStack import MyStack
import csv
import time
def fonk1():
    b1 = MyStack()
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    a5 = 0
    a6 = 0
    b2 = open('output/stack_output.txt', 'w+')
    b2.write("Stack: \n\nResults from MyStack implementation:\n\n")
    with open("input/stack_input.txt") as f:
        b3 = csv.b3(f, delimiter=',')
        for row in b3:
            b4 = row[0]
            b5 = row[1] if len(row) > 1 else None
            if b4 = = 'Push':
                b6 = time.time()
                b1.push(b5)
                a4 += time.time() - b6
                a1 += 1
            elif b4 = = 'Pop':
                b6 = time.time()
                if b1.top:
                    b7 = b1.pop()
                    b2.write(f'Item {b7} popped\n')
                else:
                    b2.write("Can't pop from an empty stack\n")
                a5 += time.time() - b6
                a2 += 1
            elif b4 = = 'getMax':
                b6 = time.time()
                b8 = b1.get_max()
                if b8 is not None:
                    b2.write(f'Max b5: {b8}\n')
                else:
                    b2.write("Max b5 is None as stack is empty\n")
                a6 += time.time() - b6
                a3 += 1
    if a1 > 0:
        b9 = fonk3(a4, a1) * 1000
    if a2 > 0:
        b10 = fonk3(a5, a2) * 1000
    if a3 > 0:
        b11 = fonk3(a6, a3) * 1000
    b12 = a1 + a2 + a3
    b13 = a4 + a5 + a6
    b14 = f'\nTime for executing all {b12} push, pop, and getMax operations in the sequence: {b13 * 1000:.4f} ms\n'
    b2.write(b14)
    b15 = f'Average time for push operations: {b9:.3f} ms\n'
    b2.write(b15)
    b16 = f'Average time for pop operations: {b10:.3f} ms\n'
    b2.write(b16)
    b17 = f'Average time for getMax operations: {b11:.3f} ms\n'
    b2.write(b17)
    b2.close()
def fonk2():
    b18 = MyQueue()
    a7 = 0
    a8 = 0
    a9 = 0
    a10 = 0
    b2 = open('output/queue_output.txt', 'w+')
    b2.write('Queue: \n\nResults from MyQueue implementation:\n\n')
    with open("input/queue_input.txt") as f:
        b3 = csv.b3(f, delimiter=',')
        for row in b3:
            b4 = row[0]
            b5 = row[1] if len(row) > 1 else None
            if b4 = = 'Enqueue':
                b6 = time.time()
                b18.enqueue(b5)
                a7 += 1
                a8 += time.time() - b6
            elif b4 = = 'Dequeue':
                b6 = time.time()
                b19 = b18.dequeue()
                b2.write(f'Item {b19} dequeued\n')
                a9 += 1
                a10 += time.time() - b6
    if a7 > 0:
        b20 = fonk3(a8, a7) * 1000
    if a9 > 0:
        b21 = fonk3(a10, a9) * 1000
    b12 = a7 + a9
    b13 = a8 + a10
    b14 = f'\nTime for executing the sequence of a total of {b12} enqueue and dequeue operations: {b13 * 1000:.4f} ms\n'
    b2.write(b14)
    b22 = f'Average time for enqueue operation: {b20:.3f} ms\n'
    b2.write(b22)
    b23 = f'Average time for dequeue operations: {b21:.3f} ms\n'
    b2.write(b23)
    b2.close()
def fonk3(b13, count):
    return b13 / count
if b24 = = '__main__':
    fonk1()
    fonk2()