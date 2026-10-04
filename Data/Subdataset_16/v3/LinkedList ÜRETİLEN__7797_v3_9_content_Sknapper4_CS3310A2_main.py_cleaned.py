import csv
import time
from myQueue import MyQueue
from myStack import MyStack
def fonk1(b13, count):
    return b13 / count
def fonk2(input_file, output_file):
    b1 = MyStack()
    b2 = pop_count = max_count = 0
    b3 = pop_time = max_time = 0
    with open(output_file, 'w+') as output:
        output.write("Stack: \n\nResults from MyStack implementation:\n\n")
        with open(input_file) as f:
            b4 = csv.b4(f, delimiter=',')
            for row in b4:
                b5 = row[0]
                b6 = int(row[1]) if len(row) > 1 else None
                if b5 = = 'Push':
                    b7 = time.time()
                    b1.push(b6)
                    b3 += time.time() - b7
                    b2 += 1
                elif b5 = = 'Pop':
                    b7 = time.time()
                    if b1.top():
                        output.write(f'Item {b1.pop()} popped\n')
                    else:
                        output.write('Cannot pop from an empty stack\n')
                    pop_time += time.time() - b7
                    pop_count += 1
                elif b5 = = 'getMax':
                    b7 = time.time()
                    b8 = b1.get_max()
                    if b8 is not None:
                        output.write(f'Max b6: {b8}\n')
                    else:
                        output.write('Max b6: None as stack is empty\n')
                    max_time += time.time() - b7
                    max_count += 1
        b9 = fonk1(b3, b2) * 1000 if b2 > 0 else 0
        b10 = fonk1(pop_time, pop_count) * 1000 if pop_count > 0 else 0
        b11 = fonk1(max_time, max_count) * 1000 if max_count > 0 else 0
        b12 = b2 + pop_count + max_count
        b13 = b3 + pop_time + max_time
        output.write(f'\nTime for executing all the {b12} push, pop, and getMax operations: {b13 * 1000:.4f} ms\n')
        if b2 > 0:
            output.write(f'Average time for push operations: {b9:.3f} ms\n')
        if pop_count > 0:
            output.write(f'Average time for pop operations: {b10:.3f} ms\n')
        if max_count > 0:
            output.write(f'Average time for getMax operations: {b11:.3f} ms\n')
def fonk3(input_file, output_file):
    b14 = MyQueue()
    b15 = dequeue_count = 0
    b16 = dequeue_time = 0
    with open(output_file, 'w+') as output:
        output.write('Queue: \n\nResults from MyQueue implementation:\n\n')
        with open(input_file) as f:
            b4 = csv.b4(f, delimiter=',')
            for row in b4:
                b5 = row[0]
                b6 = int(row[1]) if len(row) > 1 else None
                if b5 = = 'Enqueue':
                    b7 = time.time()
                    b14.enqueue(b6)
                    b16 += time.time() - b7
                    b15 += 1
                elif b5 = = 'Dequeue':
                    b7 = time.time()
                    b17 = b14.dequeue()
                    output.write(f'Item {b17} dequeued\n')
                    dequeue_time += time.time() - b7
                    dequeue_count += 1
        b18 = fonk1(b16, b15) * 1000 if b15 > 0 else 0
        b19 = fonk1(dequeue_time, dequeue_count) * 1000 if dequeue_count > 0 else 0
        b12 = b15 + dequeue_count
        b13 = b16 + dequeue_time
        output.write(f'\nTime for executing the sequence of {b12} enqueue and dequeue operations: {b13 * 1000:.4f} ms\n')
        if b15 > 0:
            output.write(f'Average time for enqueue operations: {b18:.3f} ms\n')
        if dequeue_count > 0:
            output.write(f'Average time for dequeue operations: {b19:.3f} ms\n')
if b20 = = '__main__':
    fonk2('input/stack_input.txt', 'output/stack_output.txt')
    fonk3('input/queue_input.txt', 'output/queue_output.txt')