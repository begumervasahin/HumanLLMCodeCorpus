from myQueue import MyQueue
from myStack import MyStack
import csv
import time
def read_stack_input_file():
    mystack = MyStack()
    push_count, pop_count, max_count = 0, 0, 0
    push_time, pop_time, max_time = 0, 0, 0
    with open("input/stack_input.txt") as f:
        output_file = open('output/stack_output.txt', 'w+')
        output_file.write("Stack: \n\nResults from MyStack implementation:\n\n")
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            action, value = row[0], row[1] if len(row) > 1 else None
            if action == 'Push':
                start_time = time.time()
                mystack.push(value)
                push_time += time.time() - start_time
                push_count += 1
            elif action == 'Pop':
                start_time = time.time()
                if mystack.top:
                    output_file.write(f"Item {mystack.pop()} popped\n")
                else:
                    output_file.write("Can't pop from an empty stack\n")
                pop_time += time.time() - start_time
                pop_count += 1
            elif action == 'getMax':
                start_time = time.time()
                max_value = mystack.get_max
                output_file.write(f"Max value {max_value if max_value else 'is not available'}\n")
                max_time += time.time() - start_time
                max_count += 1
    push_avg = calculate_average_time(push_time, push_count)
    pop_avg = calculate_average_time(pop_time, pop_count)
    max_avg = calculate_average_time(max_time, max_count)
    write_summary(output_file, push_count, pop_count, max_count, push_avg, pop_avg, max_avg, push_time, pop_time, max_time)
    output_file.close()
def read_queue_input_file():
    myqueue = MyQueue()
    enqueue_count, dequeue_count = 0, 0
    enqueue_time, dequeue_time = 0, 0
    with open("input/queue_input.txt") as f:
        output_file = open('output/queue_output.txt', 'w+')
        output_file.write("Queue: \n\nResults from MyQueue implementation:\n\n")
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            action, value = row[0], row[1] if len(row) > 1 else None
            if action == 'Enqueue':
                start_time = time.time()
                myqueue.enqueue(value)
                enqueue_time += time.time() - start_time
                enqueue_count += 1
            elif action == 'Dequeue':
                start_time = time.time()
                dequeued_value = myqueue.dequeue()
                output_string = f"Item {dequeued_value if dequeued_value else 'is not available'} dequeued\n"
                output_file.write(output_string)
                dequeue_time += time.time() - start_time
                dequeue_count += 1
    enqueue_avg = calculate_average_time(enqueue_time, enqueue_count)
    dequeue_avg = calculate_average_time(dequeue_time, dequeue_count)
    write_summary(output_file, enqueue_count, dequeue_count, None, enqueue_avg, dequeue_avg, None, enqueue_time, dequeue_time, None)
    output_file.close()
def calculate_average_time(total_time, count):
    return total_time / count if count != 0 else 0
def write_summary(output_file, op1_count, op2_count, op3_count, op1_avg, op2_avg, op3_avg, op1_time, op2_time, op3_time):
    total_count = op1_count + op2_count + (op3_count if op3_count else 0)
    total_time = op1_time + op2_time + (op3_time if op3_time else 0)
    output_file.write(f"\nTotal number of operations: {total_count}\n")
    output_file.write(f"Total time for all operations: {total_time * 1000:.4f} ms\n")
    if op1_count > 0:
        output_file.write(f"Average time for operation 1: {op1_avg * 1000:.3f} ms\n")
    if op2_count > 0:
        output_file.write(f"Average time for operation 2: {op2_avg * 1000:.3f} ms\n")
    if op3_count and op3_count > 0:
        output_file.write(f"Average time for operation 3: {op3_avg * 1000:.3f} ms\n")
if __name__ == '__main__':
    read_stack_input_file()
    read_queue_input_file()