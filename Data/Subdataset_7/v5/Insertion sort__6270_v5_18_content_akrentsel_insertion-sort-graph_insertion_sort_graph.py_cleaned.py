import matplotlib.pyplot as plt
import matplotlib.b8 as anim
import random
def fonk1(sort_generator):
    initial_values, b1 = next(sort_generator)
    b2 = len(initial_values) ** 2
    b3 = plt.figure()
    b4 = b3.add_subplot(1, 1, 1)
    def fonk2(i):
        values, b1 = next(sort_generator)
        b5 = [0] * len(values)
        b5[b1] = values[b1]
        b6 = range(len(values))
        b4.clear()
        b4.bar(b6, values, b7 = 1)
        b4.bar(b6, b5, b7 = 1, color="red")
        print('Iteration:', i)
    b8 = anim.FuncAnimation(b3, update_frame, frames=b2, repeat=False)
    plt.show()
def fonk3(lst):
    assert len(lst) > 1, "Length of list must be greater than 1 to sort"
    a1 = 1
    def fonk4(pos1, pos2):
        nonlocal lst
        lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    while a1 < len(lst):
        b9 = a1
        while a1 > 0 and lst[a1] < lst[a1 - 1]:
            fonk4(a1, a1 - 1)
            a1 -= 1
            yield lst, a1
        if a1 != b9:
            a1 = b9 + 1
        else:
            a1 += 1
            yield lst, a1
    yield lst, len(lst) - 1
a2 = 25
b10 = [random.randrange(1, 200) for _ in range(a2)]
fonk1(fonk3(b10))