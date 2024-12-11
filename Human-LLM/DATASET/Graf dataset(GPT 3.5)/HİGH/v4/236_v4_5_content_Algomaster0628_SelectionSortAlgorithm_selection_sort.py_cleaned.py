def fonk1(num_list):
    b1 = []
    while len(num_list) > 0:
        b2 = num_list[0]
        for number in num_list:
            if number < b2:
                b2 = number
        print('\nStep ', len(b1) + 1)
        print(num_list)
        print(b1)
        b1.append(b2)
        num_list.remove(b2)
    print('\nFinish:', num_list)
    print(b1)
b3 = [2, 1, 5, 3, 4, 7, 6, 9, 8, 10]
fonk1(b3)