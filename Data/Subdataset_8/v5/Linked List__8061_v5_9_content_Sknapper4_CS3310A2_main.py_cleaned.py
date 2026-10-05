from myQueue import MyQueue
from myStack import MyStack
import csv
import time
def process_stack_input():
    stack = MyStack()
    push_count, pop_count, max_count = 0, 0, 0
    push_time, pop_time, max_time = 0, 0, 0
    with open("input/stack_input.txt") as file:
        with open('output/stack_output.txt', 'w+') as output_file:
            output_file.write("Stack:\n\nResults from MyStack implementation:\n\n")
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                action_word, value = row[0], row[1] if len(row) > 1 else None
                if action_word == 'Push':
                    start = time.time()
                    stack.push(value)
                    push_time += time.time() - start
                    push_count += 1
                elif action_word == 'Pop':
                    start = time.time()
                    if stack.top:
                        popped_item = stack.pop()
                        output_file.write(f'Item {popped_item} popped\n')
                    else:
                        output_file.write("Can't pop from an empty stack\n")
                    pop_time += time.time() - start
                    pop_count += 1
                elif action_word == 'getMax':
                    start = time.time()
                    max_value = stack.get_max()
                    if max_value is not None:
                        output_file.write(f'Max value: {max_value}\n')
                    else:
                        output_file.write("Max value is None as stack is empty\n")
                    max_time += time.time() - start
                    max_count += 1
    total_count = push_count + pop_count + max_count
    total_time = push_time + pop_time + max_time
    with open('output/stack_output.txt', 'a') as output_file:
        total_time_string = f'\nTime for executing all {total_count} push, pop, and getMax operations in the sequence: {total_time * 1000:.4f} ms\n'
        output_file.write(total_time_string)
        if push_count > 0:
            average_push = find_average_time(push_time, push_count) * 1000
            output_file.write(f'Average time for push operations: {average_push:.3f} ms\n')
        if pop_count > 0:
            average_pop = find_average_time(pop_time, pop_count) * 1000
            output_file.write(f'Average time for pop operations: {average_pop:.3f} ms\n')
        if max_count > 0:
            average_max = find_average_time(max_time, max_count) * 1000
            output_file.write(f'Average time for getMax operations: {average_max:.3f} ms\n')
def process_queue_input():
    queue = MyQueue()
    enqueue_count, dequeue_count = 0, 0
    enqueue_time, dequeue_time = 0, 0
    with open("input/queue_input.txt") as file:
        with open('output/queue_output.txt', 'w+') as output_file:
            output_file.write('Queue:\n\nResults from MyQueue implementation:\n\n')
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                action_word, value = row[0], row[1] if len(row) > 1 else None
                if action_word == 'Enqueue':
                    start = time.time()
                    queue.enqueue(value)
                    enqueue_count += 1
                    enqueue_time += time.time() - start
                elif action_word == 'Dequeue':
                    start = time.time()
                    dequeued_value = queue.dequeue()
                    output_file.write(f'Item {dequeued_value} dequeued\n')
                    dequeue_count += 1
                    dequeue_time += time.time() - start
    total_count = enqueue_count + dequeue_count
    total_time = enqueue_time + dequeue_time
    with open('output/queue_output.txt', 'a') as output_file:
        total_time_string = f'\nTime for executing the sequence of a total of {total_count} enqueue and dequeue operations: {total_time * 1000:.4f} ms\n'
        output_file.write(total_time_string)
        if enqueue_count > 0:
            average_enqueue = find_average_time(enqueue_time, enqueue_count) * 1000
            output_file.write(f'Average time for enqueue operation: {average_enqueue:.3f} ms\n')
        if dequeue_count > 0:
            average_dequeue = find_average_time(dequeue_time, dequeue_count) * 1000
            output_file.write(f'Average time for dequeue operations: {average_dequeue:.3f} ms\n')
def find_average_time(total_time, count):
    return total_time / count if count > 0 else 0
if __name__ == '__main__':
    process_stack_input()
    process_queue_input()