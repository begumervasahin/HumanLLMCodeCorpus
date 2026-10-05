import sys
def is_prime(number):
    number *= 1.0
    prime = True
    for divisor in range(2, int(number**0.5 + 1)):
        if number / divisor == int(number / divisor):
            prime = False
    return prime
def not_visited(number, queue):
    for item in queue:
        if item == number:
            return False
    return True
def get_possible_actions(number, primes):
    possible_primes = []
    str_number = str(number)
    for i in range(len(str_number)):
        for digit in range(10):
            new_number = str_number[:i] + str(digit) + str_number[i + 1:]
            if new_number[0] != '0' and new_number != str_number and not_visited(new_number, primes) \
                    and is_prime(int(float(new_number))):
                possible_primes.append(new_number)
    return possible_primes
def get_path(startP, endP):
    explore_start = []
    explore_end = []
    queue_start = []
    queue_end = []
    path_start = []
    path_end = []
    queue_start.append([str(startP)])
    queue_end.append([str(endP)])
    while len(queue_start) != 0 and len(queue_end) != 0:
        if len(queue_start) != 0:
            path_start = queue_start.pop(0)
            node_start = path_start[-1]
            explore_start.append(node_start)
            if node_start == endP or not not_visited(node_start, explore_end):
                return path_start
            adjacent_start = get_possible_actions(node_start, explore_start)
            for a_start in adjacent_start:
                new_path_start = list(path_start)
                new_path_start.append(a_start)
                queue_start.append(new_path_start)
        if len(queue_end) != 0:
            path_end = queue_end.pop(0)
            node_end = path_end[-1]
            explore_end.append(node_end)
            if node_end == startP or not not_visited(node_end, explore_start):
                return path_end
            adjacent_end = get_possible_actions(node_end, explore_end)
            for a_end in adjacent_end:
                new_path_end = list(path_end)
                new_path_end.append(a_end)
                queue_end.append(new_path_end)
    return []
def main():
    for line in sys.stdin.readlines():
        primes = str(line).split()
        path = get_path(primes[0], primes[1])
        if len(path) == 0 or path[-1] != primes[1]:
            print("UNSOLVABLE")
        else:
            print(' '.join(path))
if __name__ == '__main__':
    main()