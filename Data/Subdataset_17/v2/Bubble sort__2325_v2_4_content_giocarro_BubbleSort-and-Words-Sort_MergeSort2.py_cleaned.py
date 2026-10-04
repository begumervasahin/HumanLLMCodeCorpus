a = [0, 9, 1, 4, 6, 7, 2, 1, 8, 7, 7, 4, 3, 5, 6, 1, 7, 8, 0, 3]
length = len(a)
power = 0
temp_length = length
while temp_length % 2 == 0:
    temp_length
    power += 1
interval_size = 2 ** power
num_intervals = length
print('Number of intervals =', num_intervals)
print('Interval size =', interval_size)
print('List length =', length)
print(a)
start = 0
group = 1
for start in range(0, length, interval_size):
    for k in range(0, group * temp_length - 1):
        b = []
        print('b =', b, '\ng =', group)
        n = 0
        m = 0
        for i in range(0, group * temp_length - 1):
            for j in range(0, group * temp_length):
                if i >= n:
                    if i < j:
                        if a[i] <= a[j]:
                            b.append(a[i])
                            n = j
                            if j == temp_length - 1:
                                b.append(a[j])
                            else:
                                break
                        else:
                            b.append(a[j])
                            if j == temp_length - 1:
                                m += 1
                                b.append(a[i])
                                break
                else:
                    break
            if m > 0:
                break
        a = list(b)
        print('a =', a, '\nb =', b, '\nk =', k, '\ni =', i, '\nj =', j, '\nh =', start, '\ng*temp_length-1 =', group * temp_length - 1)
    group += 1
    start += temp_length