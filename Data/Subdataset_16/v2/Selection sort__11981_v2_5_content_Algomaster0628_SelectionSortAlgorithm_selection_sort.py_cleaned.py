def fonk1(num_list):
    b1 = []
    a1 = 1
    while num_list:
        b2 = min(num_list)
        print(f'\nStep {a1}')
        print('Remaining list:', num_list)
        print('Sorted list:', b1)
        b1.append(b2)
        num_list.remove(b2)
        a1 += 1
    print('\nFinish:')
    print('Final sorted list:', b1)
def fonk2():
    b3 = [2, 1, 5, 3, 4, 7, 6, 9, 8, 10]
    print("Original list:", b3)
    fonk1(b3)
if b4 = = "__main__":
    fonk2()