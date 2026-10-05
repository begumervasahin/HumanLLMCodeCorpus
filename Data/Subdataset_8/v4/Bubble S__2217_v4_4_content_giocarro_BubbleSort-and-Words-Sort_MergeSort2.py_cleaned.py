a = [0, 9, 1, 4, 6, 7, 2, 1, 8, 7, 7, 4, 3, 5, 6, 1, 7, 8, 0, 3]
length = len(a)
total_intervals = length
count = 0
while total_intervals % 2 == 0:
    total_intervals
    count += 1
power_of_2 = 2 ** count
interval_size = length / power_of_2
print('Number of intervals =', power_of_2)
print('Interval size =', interval_size)
print('Length of the list =', length)
print('Original list:', a)
start = 0
end = 1
for _ in range(power_of_2):
    temp = []
    for _ in range(start, end * interval_size):
        for j in range(start, end * interval_size - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    for i in range(start, end * interval_size):
        temp.append(a[i])
    start = end * interval_size
    end += 1
    print('Sorted interval:', temp)
    print('Start index:', start)
    print('End index:', end)
    print('Updated list:', a)