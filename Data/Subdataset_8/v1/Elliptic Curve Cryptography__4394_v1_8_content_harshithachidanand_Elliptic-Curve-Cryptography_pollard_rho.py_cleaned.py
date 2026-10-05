val = (5 ** 30) % 2017
print("S1 ", val, "\n")
my_list = []
for i in range(1, 10):
    val2 = (val ** 2) % 2017
    if 1 <= val2 <= 672:
        print("S0 ", val2, "\n")
    elif 673 <= val2 <= 1345:
        print("S1 ", val2, "\n")
    elif 1346 <= val2 <= 2016:
        print("S2 ", val2, "\n")
    else:
        print("oops \n")
    my_list.append(val)
    my_list.append(val2)
    val = (1736 * val2) % 2017
    if 1 <= val <= 672:
        print("S0 ", val, "\n")
    elif 673 <= val <= 1345:
        print("S1 ", val, "\n")
    elif 1346 <= val <= 2016:
        print("S2 ", val, "\n")
    else:
        print("oops \n")
print(my_list)
mapped_values = {val: [i for i in range(len(my_list)) if my_list[i] == val] for val in my_list}
print(mapped_values)