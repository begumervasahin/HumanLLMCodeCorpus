def fonk1(num_list):
    b1 = []
    a1 = 1
    while len(num_list) > 0:
        b2 = num_list[0]
        for number in num_list:
            if number < b2:
                b2 = number
        print(f'\nStep {a1}')
        print(f'Current list: {num_list}')
        print(f'Sorted list: {b1}')
        b1.append(b2)
        num_list.remove(b2)
        a1 += 1
    print('\nFinal result:')
    print(f'Original list: {b4}')
    print(f'Sorted list: {b1}')
if b3 = = "__main__":
    b4 = [2, 1, 5, 3, 4, 7, 6, 9, 8, 10]
    fonk1(b4)