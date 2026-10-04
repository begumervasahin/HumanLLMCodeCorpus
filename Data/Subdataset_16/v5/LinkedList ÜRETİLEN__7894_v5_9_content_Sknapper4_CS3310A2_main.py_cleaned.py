import csv
import time
from myQueue import MyQueue
from myStack import MyStack
def fonk1():
    b1 = MyStack()
    push_count, pop_count, b2 = 0, 0, 0
    push_time, pop_time, b3 = 0, 0, 0
    with open('output/stack_output.txt', 'w+') as output_file:
        output_file.write("Stack:\n\nResults from MyStack implementation:\n\n")
        with open("input/stack_input.txt") as f:
            b4 = csv.b4(f, delimiter=',')
            for row in b4:
                b5 = row[0]
                b6 = row[1] if len(row) > 1 else None
                if b5 = = 'Push':
                    b7 = time.time()
                    b1.push(b6)
                    push_time += time.time() - b7
                    push_count += 1
                elif b5 = = 'Pop':
                    b7 = time.time()
                    if b1.top:
                        output_file.write(f'Item {b1.pop()} popped\n')
                    else:
                        output_file.write('Cannot pop from an empty stack\n')
                    pop_time += time.time() - b7
                    pop_count += 1
                elif b5 = = 'getMax':
                    b7 = time.time()
                    b8 = b1.get_max() if b1.get_max else 'undefined'
                    output_file.write(f'Max b6 is {b8}\n')
                    b3 += time.time() - b7
                    b2 += 1
        b9 = push_count + pop_count + b2
        b10 = push_time + pop_time + b3
        if push_count > 0:
            b11 = (push_time / push_count) * 1000
            output_file.write(f'Average time for push operations: {b11:.3f} ms\n')
        if pop_count > 0:
            b12 = (pop_time / pop_count) * 1000
            output_file.write(f'Average time for pop operations: {b12:.3f} ms\n')
        if b2 > 0:
            b13 = (b3 / b2) * 1000
            output_file.write(f'Average time for getMax operations: {b13:.3f} ms\n')
        output_file.write(f'\nTime for executing all the {b9} push, pop, and getMax operations: {b10 * 1000:.4f} ms\n')
def fonk2():
    b14 = MyQueue()
    enqueue_count, b15 = 0, 0
    dequeue_count, b16 = 0, 0
    with open('output/queue_output.txt', 'w+') as output_file:
        output_file.write('Queue:\n\nResults from MyQueue implementation:\n\n')
        with open("input/queue_input.txt") as f:
            b4 = csv.b4(f, delimiter=',')
            for row in b4:
                b5 = row[0]
                b6 = row[1] if len(row) > 1 else None
                if b5 = = 'Enqueue':
                    b7 = time.time()
                    b14.enqueue(b6)
                    b15 += time.time() - b7
                    enqueue_count += 1
                elif b5 = = 'Dequeue':
                    b7 = time.time()
                    b17 = b14.dequeue()
                    output_file.write(f'Item {b17} dequeued\n')
                    b16 += time.time() - b7
                    dequeue_count += 1
        b9 = enqueue_count + dequeue_count
        b10 = b15 + b16
        if enqueue_count > 0:
            b18 = (b15 / enqueue_count) * 1000
            output_file.write(f'Average time for enqueue operations: {b18:.3f} ms\n')
        if dequeue_count > 0:
            b19 = (b16 / dequeue_count) * 1000
            output_file.write(f'Average time for dequeue operations: {b19:.3f} ms\n')
        output_file.write(f'\nTime for executing the sequence of {b9} enqueue and dequeue operations: {b10 * 1000:.4f} ms\n')
def fonk3():
    fonk1()
    fonk2()
if b20 = = '__main__':
    fonk3()