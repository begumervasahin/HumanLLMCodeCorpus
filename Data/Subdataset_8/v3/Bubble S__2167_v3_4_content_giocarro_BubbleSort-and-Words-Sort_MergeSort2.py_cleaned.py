def find_intervals_length(lst_length):
    x = 0
    length = lst_length
    while length % 2 == 0:
        length = length
        x += 1
    power_of_2 = 2 ** x
    interval_size = lst_length / power_of_2
    return interval_size, power_of_2
def sort_intervals(lst, interval_size):
    sorted_list = []
    for start in range(0, len(lst), int(interval_size)):
        end = start + int(interval_size)
        sorted_list.extend(sorted(lst[start:end]))
    return sorted_list
def main():
    a = [0, 9, 1, 4, 6, 7, 2, 1, 8, 7, 7, 4, 3, 5, 6, 1, 7, 8, 0, 3]
    lst_length = len(a)
    interval_size, intervals = find_intervals_length(lst_length)
    print('Number of intervals =', intervals)
    print('Interval size =', interval_size)
    print('Length of list =', lst_length)
    print('List:', a)
    sorted_list = sort_intervals(a, interval_size)
    print('Sorted list:', sorted_list)
if __name__ == "__main__":
    main()