import csv
import time
from myQueue import MyQueue
from myStack import MyStack
def find_average_time(total_time, count):
    return total_time / count
def process_stack_operations(input_file, output_file):
    mystack = MyStack()
    push_count = pop_count = max_count = 0
    push_time = pop_time = max_time = 0
    with open(output_file, 'w+') as output:
        output.write("Stack: \n\nResults from MyStack implementation:\n\n")
        with open(input_file) as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                action_word = row[0]
                value = int(row[1]) if len(row) > 1 else None
                if action_word == 'Push':
                    start = time.time()
                    mystack.push(value)
                    push_time += time.time() - start
                    push_count += 1
                elif action_word == 'Pop':
                    start = time.time()
                    if mystack.top():
                        output.write(f'Item {mystack.pop()} popped\n')
                    else:
                        output.write('Cannot pop from an empty stack\n')
                    pop_time += time.time() - start
                    pop_count += 1
                elif action_word == 'getMax':
                    start = time.time()
                    max_value = mystack.get_max()
                    if max_value is not None:
                        output.write(f'Max value: {max_value}\n')
                    else:
                        output.write('Max value: None as stack is empty\n')
                    max_time += time.time() - start
                    max_count += 1
        if push_count > 0:
            average_push = find_average_time(push_time, push_count) * 1000
        if pop_count > 0:
            average_pop = find_average_time(pop_time, pop_count) * 1000
        if max_count > 0:
            average_max = find_average_time(max_time, max_count) * 1000
        total_count = push_count + pop_count + max_count
        total_time = push_time + pop_time + max_time
        output.write(f'\nTime for executing all the {total_count} push, pop, and getMax operations: {total_time * 1000:.4f} ms\n')
        if push_count > 0:
            output.write(f'Average time for push operations: {average_push:.3f} ms\n')
        if pop_count > 0:
            output.write(f'Average time for pop operations: {average_pop:.3f} ms\n')
        if max_count > 0:
            output.write(f'Average time for getMax operations: {average_max:.3f} ms\n')
def process_queue_operations(input_file, output_file):
    myqueue = MyQueue()
    enqueue_count = dequeue_count = 0
    enqueue_time = dequeue_time = 0
    with open(output_file, 'w+') as output:
        output.write('Queue: \n\nResults from MyQueue implementation:\n\n')
        with open(input_file) as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                action_word = row[0]
                value = int(row[1]) if len(row) > 1 else None
                if action_word == 'Enqueue':
                    start = time.time()
                    myqueue.enqueue(value)
                    enqueue_time += time.time() - start
                    enqueue_count += 1
                elif action_word == 'Dequeue':
                    start = time.time()
                    dequeued_value = myqueue.dequeue()
                    output.write(f'Item {dequeued_value} dequeued\n')
                    dequeue_time += time.time() - start
                    dequeue_count += 1
        if enqueue_count > 0:
            average_enqueue = find_average_time(enqueue_time, enqueue_count) * 1000
        if dequeue_count > 0:
            average_dequeue = find_average_time(dequeue_time, dequeue_count) * 1000
        total_count = enqueue_count + dequeue_count
        total_time = enqueue_time + dequeue_time
        output.write(f'\nTime for executing the sequence of {total_count} enqueue and dequeue operations: {total_time * 1000:.4f} ms\n')
        if enqueue_count > 0:
            output.write(f'Average time for enqueue operations: {average_enqueue:.3f} ms\n')
        if dequeue_count > 0:
            output.write(f'Average time for dequeue operations: {average_dequeue:.3f} ms\n')
if __name__ == '__main__':
    process_stack_operations('input/stack_input.txt', 'output/stack_output.txt')
    process_queue_operations('input/queue_input.txt', 'output/queue_output.txt')