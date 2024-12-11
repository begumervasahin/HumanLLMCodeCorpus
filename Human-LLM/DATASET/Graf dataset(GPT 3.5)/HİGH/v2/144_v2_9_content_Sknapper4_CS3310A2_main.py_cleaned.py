from myQueue import MyQueue
from myStack import MyStack
import csv
import time
def fonk1():
    b1 = MyStack()
    push_count, pop_count, b2 = 0, 0, 0
    push_time, pop_time, b3 = 0, 0, 0
    with open("input/stack_input.txt") as f:
        b4 = open('output/stack_output.txt', 'w+')
        b4.write("Stack: \n\nResults from MyStack implementation:\n\n")
        b5 = csv.b5(f, delimiter=',')
        for row in b5:
            b6 = row[0]
            b7 = row[1] if len(row) > 1 else None
            if b6 = = 'Push':
                b8 = time.time()
                b1.push(b7)
                push_time += time.time() - b8
                push_count += 1
            elif b6 = = 'Pop':
                b8 = time.time()
                if b1.top:
                    b4.write(f"Item {b1.pop()} popped\n")
                else:
                    b4.write("Can't pop from an empty stack\n")
                pop_time += time.time() - b8
                pop_count += 1
            elif b6 = = 'getMax':
                b8 = time.time()
                if b1.get_max:
                    b4.write(f"Max b7 {b1.get_max}\n")
                else:
                    b4.write(f"Max b7 is {b1.get_max} as stack is empty\n")
                b3 += time.time() - b8
                b2 += 1
    b9 = fonk3(push_time, push_count) * 1000 if push_count > 0 else 0
    b10 = fonk3(pop_time, pop_count) * 1000 if pop_count > 0 else 0
    b11 = fonk3(b3, b2) * 1000 if b2 > 0 else 0
    b12 = push_count + pop_count + b2
    b13 = push_time + pop_time + b3
    b14 = f"\nTime for executing all the {b12} push, pop, and getMax operations in the sequence: {b13 * 1000:.4f} ms\n"
    b4.write(b14)
    b15 = f"Average time for push operations: {b9:.3f} ms\n"
    b4.write(b15)
    b16 = f"Average time for pop operations: {b10:.3f} ms\n"
    b4.write(b16)
    b17 = f"Average time for getMax operations: {b11:.3f} ms\n"
    b4.write(b17)
    b4.close()
def fonk2():
    b18 = MyQueue()
    enqueue_count, b19 = 0, 0
    enqueue_time, b20 = 0, 0
    with open("input/queue_input.txt") as f:
        b4 = open('output/queue_output.txt', 'w+')
        b4.write("Queue: \n\nResults from MyQueue implementation:\n\n")
        b5 = csv.b5(f, delimiter=',')
        for row in b5:
            b6 = row[0]
            b7 = row[1] if len(row) > 1 else None
            if b6 = = 'Enqueue':
                b8 = time.time()
                b18.enqueue(b7)
                enqueue_count += 1
                enqueue_time += time.time() - b8
            elif b6 = = 'Dequeue':
                b8 = time.time()
                b21 = b18.dequeue()
                b22 = f"Item {b21} dequeued\n"
                b4.write(b22)
                b19 += 1
                b20 += time.time() - b8
    b23 = fonk3(enqueue_time, enqueue_count) * 1000 if enqueue_count > 0 else 0
    b24 = fonk3(b20, b19) * 1000 if b19 > 0 else 0
    b12 = enqueue_count + b19
    b13 = enqueue_time + b20
    b14 = f"\nTime for executing the sequence of a total of {b12} enqueue and dequeue operations: {b13 * 1000:.4f} ms\n"
    b4.write(b14)
    b25 = f"Average time for enqueue operation: {b23:.3f} ms\n"
    b4.write(b25)
    b26 = f"Average time for dequeue operations: {b24:.3f} ms\n"
    b4.write(b26)
    b4.close()
def fonk3(b13, count):
    return b13 / count if count != 0 else 0
if b27 = = '__main__':
    fonk1()
    fonk2()