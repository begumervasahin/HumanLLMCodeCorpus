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
            action_word = row[0]
            value = row[1] if len(row) > 1 else None
            if action_word == 'Push':
                start = time.time()
                mystack.push(value)
                push_time += time.time() - start
                push_count += 1
            elif action_word == 'Pop':
                start = time.time()
                if mystack.top:
                    output_file.write(f"Item {mystack.pop()} popped\n")
                else:
                    output_file.write("Can't pop from an empty stack\n")
                pop_time += time.time() - start
                pop_count += 1
            elif action_word == 'getMax':
                start = time.time()
                if mystack.get_max:
                    output_file.write(f"Max value {mystack.get_max}\n")
                else:
                    output_file.write(f"Max value is {mystack.get_max} as stack is empty\n")
                max_time += time.time() - start
                max_count += 1
    push_avg = find_average_time(push_time, push_count) * 1000 if push_count > 0 else 0
    pop_avg = find_average_time(pop_time, pop_count) * 1000 if pop_count > 0 else 0
    max_avg = find_average_time(max_time, max_count) * 1000 if max_count > 0 else 0
    total_count = push_count + pop_count + max_count
    total_time = push_time + pop_time + max_time
    total_time_string = f"\nTime for executing all the {total_count} push, pop, and getMax operations in the sequence: {total_time * 1000:.4f} ms\n"
    output_file.write(total_time_string)
    push_string = f"Average time for push operations: {push_avg:.3f} ms\n"
    output_file.write(push_string)
    pop_string = f"Average time for pop operations: {pop_avg:.3f} ms\n"
    output_file.write(pop_string)
    max_string = f"Average time for getMax operations: {max_avg:.3f} ms\n"
    output_file.write(max_string)
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
            action_word = row[0]
            value = row[1] if len(row) > 1 else None
            if action_word == 'Enqueue':
                start = time.time()
                myqueue.enqueue(value)
                enqueue_count += 1
                enqueue_time += time.time() - start
            elif action_word == 'Dequeue':
                start = time.time()
                dequeued_value = myqueue.dequeue()
                output_string = f"Item {dequeued_value} dequeued\n"
                output_file.write(output_string)
                dequeue_count += 1
                dequeue_time += time.time() - start
    enqueue_avg = find_average_time(enqueue_time, enqueue_count) * 1000 if enqueue_count > 0 else 0
    dequeue_avg = find_average_time(dequeue_time, dequeue_count) * 1000 if dequeue_count > 0 else 0
    total_count = enqueue_count + dequeue_count
    total_time = enqueue_time + dequeue_time
    total_time_string = f"\nTime for executing the sequence of a total of {total_count} enqueue and dequeue operations: {total_time * 1000:.4f} ms\n"
    output_file.write(total_time_string)
    enqueue_string = f"Average time for enqueue operation: {enqueue_avg:.3f} ms\n"
    output_file.write(enqueue_string)
    dequeue_string = f"Average time for dequeue operations: {dequeue_avg:.3f} ms\n"
    output_file.write(dequeue_string)
    output_file.close()
def find_average_time(total_time, count):
    return total_time / count if count != 0 else 0
if __name__ == '__main__':
    read_stack_input_file()
    read_queue_input_file()