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
            if row[1]:
                b5 = row[1]
            if b4 = = 'Push':
                b6 = time.time()
                b1.push(b5)
                a4 += time.time() - b6
                a1 += 1
            if b4 = = 'Pop':
                b6 = time.time()
                if b1.top:
                    b7 = 'Item' + str(b1.pop()) + ' popped\n'
                    b2.write(b7)
                else:
                    b2.write('Can\'t pop from an empty stack\n')
                a5 += time.time() - b6
                a2 += 1
            if b4 = = 'getMax':
                b6 = time.time()
                if b1.get_max:
                    b7 = 'Max b5' + str(b1.get_max) + '\n'
                    b2.write(b7)
                else:
                    b7 = 'Max b5 is' + str(b1.get_max) + 'as stack is empty\n'
                    b2.write(b7)
                a6 += time.time() - b6
                a3 += 1
    if a1 > 0:
        b8 = fonk3(a4, a1) * 1000
    if a2 > 0:
        b9 = fonk3(a5, a2) * 1000
    if a3 > 0:
        b10 = fonk3(a6, a3) * 1000
    b11 = a1 + a2 + a3
    b12 = a4 + a5 + a6
    b7 = f'\nTime for executing all the %d push, pop, and getMax operations in the sequence: %.4f ms\n' \
                        % (b11, b12 * 1000)
    b2.write(b7)
    b13 = f'Average time for push operations: %.3f ms\n' % b8
    b2.write(b13)
    b14 = f'Average time for pop operations: %.3f ms\n' % b9
    b2.write(b14)
    b15 = f'Average time for getMax operations: %.3f ms\n' % b10
    b2.write(b15)
    b2.close()
def fonk2():
    b16 = MyQueue()
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
            if row[1]:
                b5 = row[1]
            if b4 = = 'Enqueue':
                b6 = time.time()
                b16.enqueue(b5)
                a7 += 1
                a8 += time.time() - b6
            if b4 = = 'Dequeue':
                b6 = time.time()
                b17 = b16.dequeue()
                b18 = 'Item' + str(b17) + ' dequeued\n'
                b2.write(b18)
                a9 += 1
                a10 += time.time() - b6
    if a7 > 0:
        b19 = fonk3(a8, a7) * 1000
    if a9 > 0:
        b20 = fonk3(a10, a9) * 1000
    b11 = a7 + a9
    b12 = a8 + a10
    b7 = f'\nTime for executing the sequence of a total of %d enqueue and dequeue operations: %.4f ms\n' \
                        % (b11, b12 * 1000)
    b2.write(b7)
    b21 = f'Average time for enqueue operation: %.3f ms\n' % b19
    b2.write(b21)
    b22 = f'Average time for dequeue operations: %.3f ms\n' % b20
    b2.write(b22)
    b2.close()
def fonk3(b12, count):
    return b12 / count
if b23 = = '__main__':
    fonk1()
    fonk2()