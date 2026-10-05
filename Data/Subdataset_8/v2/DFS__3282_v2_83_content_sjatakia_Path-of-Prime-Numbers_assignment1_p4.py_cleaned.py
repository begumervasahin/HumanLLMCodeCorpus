import sys
def is_prime(number):
    number *= 1.0
    prime = True
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            prime = False
            break
    return prime
def not_visited(number, queue):
    return number not in queue
def get_possible_actions(number, primes):
    possible_primes = []
    str_number = str(number)
    for i in range(len(str_number)):
        for digit in range(10):
            new_number = str_number[:i] + str(digit) + str_number[i + 1:]
            if new_number[0] != '0' and new_number != str_number and is_prime(int(float(new_number))) \
                    and not_visited(new_number, primes):
                possible_primes.append(new_number)
    return possible_primes
def get_path(startP, endP):
    queue_start = [[str(startP)]]
    queue_end = [[str(endP)]]
    explore_start = set()
    explore_end = set()
    while queue_start and queue_end:
        path_start = queue_start.pop(0)
        node_start = path_start[-1]
        explore_start.add(node_start)
        if node_start == endP or node_start in explore_end:
            return path_start
        adjacent_start = get_possible_actions(node_start, explore_start)
        for a_start in adjacent_start:
            new_path_start = path_start + [a_start]
            queue_start.append(new_path_start)
        path_end = queue_end.pop(0)
        node_end = path_end[-1]
        explore_end.add(node_end)
        if node_end == startP or node_end in explore_start:
            return path_end
        adjacent_end = get_possible_actions(node_end, explore_end)
        for a_end in adjacent_end:
            new_path_end = path_end + [a_end]
            queue_end.append(new_path_end)
    return []
def main():
    for line in sys.stdin.readlines():
        primes = str(line).split()
        path = get_path(primes[0], primes[1])
        if not path or path[-1] != primes[1]:
            print("UNSOLVABLE")
        else:
            print(' '.join(path))
if __name__ == '__main__':
    main()