from myQueue import MyQueue
from myStack import MyStack
import csv
import time
def fonk1():
    b1 = MyStack()
    push_count, pop_count, b2 = 0, 0, 0
    push_time, pop_time, b3 = 0, 0, 0
    with open("input/stack_input.txt") as file:
        with open('output/stack_output.txt', 'w+') as output_file:
            output_file.write("Stack:\n\nResults from MyStack implementation:\n\n")
            b4 = csv.b4(file, delimiter=',')
            for row in b4:
                b6, b5 = row[0], row[1] if len(row) > 1 else None
                if b6 = = 'Push':
                    b7 = time.time()
                    b1.push(b5)
                    push_time += time.time() - b7
                    push_count += 1
                elif b6 = = 'Pop':
                    b7 = time.time()
                    if b1.top:
                        b8 = b1.pop()
                        output_file.write(f'Item {b8} popped\n')
                    else:
                        output_file.write("Can't pop from an empty b1\n")
                    pop_time += time.time() - b7
                    pop_count += 1
                elif b6 = = 'getMax':
                    b7 = time.time()
                    b9 = b1.get_max()
                    if b9 is not None:
                        output_file.write(f'Max b5: {b9}\n')
                    else:
                        output_file.write("Max b5 is None as b1 is empty\n")
                    b3 += time.time() - b7
                    b2 += 1
    b10 = push_count + pop_count + b2
    b11 = push_time + pop_time + b3
    with open('output/stack_output.txt', 'a') as output_file:
        b12 = f'\nTime for executing all {b10} push, pop, and getMax operations in the sequence: {b11 * 1000:.4f} ms\n'
        output_file.write(b12)
        if push_count > 0:
            b13 = fonk3(push_time, push_count) * 1000
            output_file.write(f'Average time for push operations: {b13:.3f} ms\n')
        if pop_count > 0:
            b14 = fonk3(pop_time, pop_count) * 1000
            output_file.write(f'Average time for pop operations: {b14:.3f} ms\n')
        if b2 > 0:
            b15 = fonk3(b3, b2) * 1000
            output_file.write(f'Average time for getMax operations: {b15:.3f} ms\n')
def fonk2():
    b16 = MyQueue()
    enqueue_count, b17 = 0, 0
    enqueue_time, b18 = 0, 0
    with open("input/queue_input.txt") as file:
        with open('output/queue_output.txt', 'w+') as output_file:
            output_file.write('Queue:\n\nResults from MyQueue implementation:\n\n')
            b4 = csv.b4(file, delimiter=',')
            for row in b4:
                b6, b5 = row[0], row[1] if len(row) > 1 else None
                if b6 = = 'Enqueue':
                    b7 = time.time()
                    b16.enqueue(b5)
                    enqueue_count += 1
                    enqueue_time += time.time() - b7
                elif b6 = = 'Dequeue':
                    b7 = time.time()
                    b19 = b16.dequeue()
                    output_file.write(f'Item {b19} dequeued\n')
                    b17 += 1
                    b18 += time.time() - b7
    b10 = enqueue_count + b17
    b11 = enqueue_time + b18
    with open('output/queue_output.txt', 'a') as output_file:
        b12 = f'\nTime for executing the sequence of a total of {b10} enqueue and dequeue operations: {b11 * 1000:.4f} ms\n'
        output_file.write(b12)
        if enqueue_count > 0:
            b20 = fonk3(enqueue_time, enqueue_count) * 1000
            output_file.write(f'Average time for enqueue operation: {b20:.3f} ms\n')
        if b17 > 0:
            b21 = fonk3(b18, b17) * 1000
            output_file.write(f'Average time for dequeue operations: {b21:.3f} ms\n')
def fonk3(b11, count):
    return b11 / count if count > 0 else 0
if b22 = = '__main__':
    fonk1()
    fonk2()