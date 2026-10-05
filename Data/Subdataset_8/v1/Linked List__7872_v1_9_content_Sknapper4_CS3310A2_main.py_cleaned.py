from myQueue import MyQueue
from myStack import MyStack
import csv
import time
def read_stack_input_file():
    mystack = MyStack()
    push_count = 0
    pop_count = 0
    max_count = 0
    push_time = 0
    pop_time = 0
    max_time = 0
    output_file = open('output/stack_output.txt', 'w+')
    output_file.write("Stack: \n\nResults from MyStack implementation:\n\n")
    with open("input/stack_input.txt") as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            action_word = row[0]
            if row[1]:
                value = row[1]
            if action_word == 'Push':
                start = time.time()
                mystack.push(value)
                push_time += time.time() - start
                push_count += 1
            if action_word == 'Pop':
                start = time.time()
                if mystack.top:
                    total_time_string = 'Item' + str(mystack.pop()) + ' popped\n'
                    output_file.write(total_time_string)
                else:
                    output_file.write('Can\'t pop from an empty stack\n')
                pop_time += time.time() - start
                pop_count += 1
            if action_word == 'getMax':
                start = time.time()
                if mystack.get_max:
                    total_time_string = 'Max value' + str(mystack.get_max) + '\n'
                    output_file.write(total_time_string)
                else:
                    total_time_string = 'Max value is' + str(mystack.get_max) + 'as stack is empty\n'
                    output_file.write(total_time_string)
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
    total_time_string = f'\nTime for executing all the %d push, pop, and getMax operations in the sequence: %.4f ms\n' \
                        % (total_count, total_time * 1000)
    output_file.write(total_time_string)
    push_string = f'Average time for push operations: %.3f ms\n' % average_push
    output_file.write(push_string)
    pop_string = f'Average time for pop operations: %.3f ms\n' % average_pop
    output_file.write(pop_string)
    max_string = f'Average time for getMax operations: %.3f ms\n' % average_max
    output_file.write(max_string)
    output_file.close()
def read_queue_input_file():
    myqueue = MyQueue()
    enqueue_count = 0
    enqueue_time = 0
    dequeue_count = 0
    dequeue_time = 0
    output_file = open('output/queue_output.txt', 'w+')
    output_file.write('Queue: \n\nResults from MyQueue implementation:\n\n')
    with open("input/queue_input.txt") as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            action_word = row[0]
            if row[1]:
                value = row[1]
            if action_word == 'Enqueue':
                start = time.time()
                myqueue.enqueue(value)
                enqueue_count += 1
                enqueue_time += time.time() - start
            if action_word == 'Dequeue':
                start = time.time()
                dequeued_value = myqueue.dequeue()
                output_string = 'Item' + str(dequeued_value) + ' dequeued\n'
                output_file.write(output_string)
                dequeue_count += 1
                dequeue_time += time.time() - start
    if enqueue_count > 0:
        average_enqueue = find_average_time(enqueue_time, enqueue_count) * 1000
    if dequeue_count > 0:
        average_dequeue = find_average_time(dequeue_time, dequeue_count) * 1000
    total_count = enqueue_count + dequeue_count
    total_time = enqueue_time + dequeue_time
    total_time_string = f'\nTime for executing the sequence of a total of %d enqueue and dequeue operations: %.4f ms\n' \
                        % (total_count, total_time * 1000)
    output_file.write(total_time_string)
    enqueue_string = f'Average time for enqueue operation: %.3f ms\n' % average_enqueue
    output_file.write(enqueue_string)
    dequeue_string = f'Average time for dequeue operations: %.3f ms\n' % average_dequeue
    output_file.write(dequeue_string)
    output_file.close()
def find_average_time(total_time, count):
    return total_time / count
if __name__ == '__main__':
    read_stack_input_file()
    read_queue_input_file()