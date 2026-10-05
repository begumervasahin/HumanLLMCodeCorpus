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
            b7, b6 = row[0], row[1] if len(row) > 1 else None
            if b7 = = 'Push':
                b8 = time.time()
                b1.push(b6)
                push_time += time.time() - b8
                push_count += 1
            elif b7 = = 'Pop':
                b8 = time.time()
                if b1.top:
                    b4.write(f"Item {b1.pop()} popped\n")
                else:
                    b4.write("Can't pop from an empty stack\n")
                pop_time += time.time() - b8
                pop_count += 1
            elif b7 = = 'getMax':
                b8 = time.time()
                b9 = b1.get_max
                b4.write(f"Max b6 {b9 if b9 else 'is not available'}\n")
                b3 += time.time() - b8
                b2 += 1
    b10 = fonk3(push_time, push_count)
    b11 = fonk3(pop_time, pop_count)
    b12 = fonk3(b3, b2)
    fonk4(b4, push_count, pop_count, b2, b10, b11, b12, push_time, pop_time, b3)
    b4.close()
def fonk2():
    b13 = MyQueue()
    enqueue_count, b14 = 0, 0
    enqueue_time, b15 = 0, 0
    with open("input/queue_input.txt") as f:
        b4 = open('output/queue_output.txt', 'w+')
        b4.write("Queue: \n\nResults from MyQueue implementation:\n\n")
        b5 = csv.b5(f, delimiter=',')
        for row in b5:
            b7, b6 = row[0], row[1] if len(row) > 1 else None
            if b7 = = 'Enqueue':
                b8 = time.time()
                b13.enqueue(b6)
                enqueue_time += time.time() - b8
                enqueue_count += 1
            elif b7 = = 'Dequeue':
                b8 = time.time()
                b16 = b13.dequeue()
                b17 = f"Item {b16 if b16 else 'is not available'} dequeued\n"
                b4.write(b17)
                b15 += time.time() - b8
                b14 += 1
    b18 = fonk3(enqueue_time, enqueue_count)
    b19 = fonk3(b15, b14)
    fonk4(b4, enqueue_count, b14, None, b18, b19, None, enqueue_time, b15, None)
    b4.close()
def fonk3(b21, count):
    return b21 / count if count != 0 else 0
def fonk4(b4, op1_count, op2_count, op3_count, op1_avg, op2_avg, op3_avg, op1_time, op2_time, op3_time):
    b20 = op1_count + op2_count + (op3_count if op3_count else 0)
    b21 = op1_time + op2_time + (op3_time if op3_time else 0)
    b4.write(f"\nTotal number of operations: {b20}\n")
    b4.write(f"Total time for all operations: {b21 * 1000:.4f} ms\n")
    if op1_count > 0:
        b4.write(f"Average time for operation 1: {op1_avg * 1000:.3f} ms\n")
    if op2_count > 0:
        b4.write(f"Average time for operation 2: {op2_avg * 1000:.3f} ms\n")
    if op3_count and op3_count > 0:
        b4.write(f"Average time for operation 3: {op3_avg * 1000:.3f} ms\n")
if b22 = = '__main__':
    fonk1()
    fonk2()