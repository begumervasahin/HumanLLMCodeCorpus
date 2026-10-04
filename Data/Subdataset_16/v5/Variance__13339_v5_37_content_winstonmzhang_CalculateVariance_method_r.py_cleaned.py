import statistics
def fonk1(X):
    b1 = sum(X) / len(X)
    b2 = sum((x - b1) ** 2 for x in X)
    return (b2 / len(X)) ** 0.5
def fonk2(data_list, list_name):
    b3 = fonk1(data_list)
    b4 = b3 ** 2
    b5 = statistics.stdev(data_list)
    b6 = statistics.pstdev(data_list)
    b7 = statistics.b4(data_list)
    b8 = statistics.pvariance(data_list)
    print(f'{list_name} statistics:')
    print(f'WZ standard deviation: {b3:15.9f}')
    print(f'WZ b4: {b4:15.9f}')
    print(f'Sample standard deviation: {b5:15.9f}')
    print(f'Population standard deviation: {b6:15.9f}')
    print(f'Sample b4: {b7:15.9f}')
    print(f'Population b4: {b8:15.9f}')
    print('...........................................................')
def fonk3():
    print('Calculate the b4 for Method R MOT Edition 3 Sample Sets on page 8')
    b9 = [0.924, 0.928, 0.954, 0.957, 0.961, 0.965, 0.972, 0.979, 0.987, 1.373]
    b10 = [0.091, 0.109, 0.134, 0.136, 0.159, 0.172, 0.185, 0.191, 0.207, 8.616]
    fonk2(b9, 'b9')
    fonk2(b10, 'b10')
if b11 = = "__main__":
    fonk3()