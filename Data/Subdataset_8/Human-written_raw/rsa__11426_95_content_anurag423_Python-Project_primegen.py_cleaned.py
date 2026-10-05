def primegen():
    import numpy as np
    bits = int(input('How many bits? '))
    final = 2 ** bits
    ints_to_final = list(range(2,final+1))
    ints_to_final = np.array(ints_to_final)
    index = 0
    while index < len(ints_to_final):
        del_vect = []
        del_vect = np.array(del_vect)
        for i in range(0,len(ints_to_final)):
            if ints_to_final[i] == ints_to_final[index]:
                del_vect = np.append(del_vect, 0)
            else:
                if ints_to_final[i] % ints_to_final[index] == 0:
                    del_vect = np.append(del_vect, ints_to_final[i])
                else:
                    del_vect = np.append(del_vect, 0)
        ints_to_final = ints_to_final - del_vect
        ints_to_final = ints_to_final[ints_to_final != 0]
        index = index + 1
    random1 = int(np.random.choice(ints_to_final,1))
    print(f'(Hidden) P Value: {int(random1)}')
    random2 = int(np.random.choice(ints_to_final,1))
    print(f'(Hidden) Q Value: {int(random2)}')
    return random1,random2