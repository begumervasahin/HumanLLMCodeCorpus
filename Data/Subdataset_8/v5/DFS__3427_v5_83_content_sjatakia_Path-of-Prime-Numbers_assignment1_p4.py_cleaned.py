import sys
def is_prime(number):
    number *= 1.0
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True
def not_visited(number, visited):
    return number not in visited
def get_possible_actions(number, visited):
    possible_primes = []
    str_number = str(number)
    for i in range(len(str_number)):
        for digit in range(10):
            new_number = str_number[:i] + str(digit) + str_number[i + 1:]
            if new_number[0] != '0' and new_number != str_number \
                    and not_visited(new_number, visited) and is_prime(int(new_number)):
                possible_primes.append(new_number)
    return possible_primes
def get_path(start, end):
    visited_start = set()
    visited_end = set()
    queue_start = [[str(start)]]
    queue_end = [[str(end)]]
    while queue_start and queue_end:
        path_start = queue_start.pop(0)
        node_start = path_start[-1]
        visited_start.add(node_start)
        if node_start == end or node_start in visited_end:
            return path_start
        adjacent_start = get_possible_actions(node_start, visited_start)
        for adj_start in adjacent_start:
            new_path_start = path_start + [adj_start]
            queue_start.append(new_path_start)
        path_end = queue_end.pop(0)
        node_end = path_end[-1]
        visited_end.add(node_end)
        if node_end == start or node_end in visited_start:
            return path_end
        adjacent_end = get_possible_actions(node_end, visited_end)
        for adj_end in adjacent_end:
            new_path_end = path_end + [adj_end]
            queue_end.append(new_path_end)
    return []
def main():
    for line in sys.stdin.readlines():
        primes = str(line).split()
        paths = get_path(primes[0], primes[1])
        if not paths or paths[-1] != primes[1]:
            print("UNSOLVABLE")
        else:
            print(' '.join(paths))
if __name__ == '__main__':
    main()