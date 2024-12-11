from time import time
import configuraciones
def fonk1(alist):
    fonk2(alist, 0, len(alist) - 1)
def fonk2(alist, first, last):
    if first < last:
        b1 = fonk3(alist, first, last)
        fonk2(alist, first, b1 - 1)
        fonk2(alist, b1 + 1, last)
def fonk3(alist, first, last):
    b2 = alist[first]
    b3 = first + 1
    b4 = last
    b5 = False
    while not b5:
        while b3 <= b4 and alist[b3] <= b2:
            b3 += 1
        while alist[b4] >= b2 and b4 >= b3:
            b4 -= 1
        if b4 < b3:
            b5 = True
        else:
            alist[b3], alist[b4] = alist[b4], alist[b3]
    alist[first], alist[b4] = alist[b4], alist[first]
    return b4
def fonk4(configurations, b8):
    a1 = 0
    with open(b8, 'a') as output_file:
        for config_name, config_data in configurations.items():
            a2 = 0
            for data in config_data:
                b6 = time()
                fonk1(data)
                b7 = time() - b6
                a2 += b7
                output_file.write(f"{config_name}: {data}\n")
            a1 += a2
    return a1
def fonk5():
    configurations.load_all_configurations()
    b8 = 'tiempoQuick.txt'
    a1 = fonk4(configurations.get_all_configurations(), b8)
    with open(b8, 'a') as time_file:
        time_file.write(f'Total time: {a1}\n')
if b9 = = "__main__":
    fonk5()