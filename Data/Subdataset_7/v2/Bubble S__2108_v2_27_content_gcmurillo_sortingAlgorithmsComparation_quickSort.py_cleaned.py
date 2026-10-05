from time import time
import configuraciones
def fonk1(arr):
    fonk2(arr, 0, len(arr) - 1)
def fonk2(arr, low, high):
    if low < high:
        b1 = fonk3(arr, low, high)
        fonk2(arr, low, b1 - 1)
        fonk2(arr, b1 + 1, high)
def fonk3(arr, low, high):
    b2 = arr[low]
    b3 = low + 1
    b4 = high
    b5 = False
    while not b5:
        while b3 <= b4 and arr[b3] <= b2:
            b3 += 1
        while arr[b4] >= b2 and b4 >= b3:
            b4 -= 1
        if b4 < b3:
            b5 = True
        else:
            arr[b3], arr[b4] = arr[b4], arr[b3]
    arr[low], arr[b4] = arr[b4], arr[low]
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