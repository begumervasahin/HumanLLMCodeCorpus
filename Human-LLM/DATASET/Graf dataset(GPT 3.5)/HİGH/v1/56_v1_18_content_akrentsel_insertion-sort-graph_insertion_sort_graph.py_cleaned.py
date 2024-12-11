import matplotlib.pyplot as plt
import matplotlib.animation as anim
import random
def fonk1(gen):
    y_vals, b1 = next(gen)
    b2 = len(y_vals) ** 2
    b3 = plt.figure()
    b4 = b3.add_subplot(1, 1, 1)
    def fonk2(i):
        y_vals, b1 = next(gen)
        b5 = [0] * len(y_vals)
        b5[b1] = y_vals[b1]
        b6 = range(len(y_vals))
        b4.clear()
        b4.bar(b6, y_vals, b7 = 1)
        b4.bar(b6, b5, b7 = 1, color="red")
        print('Iteration:', i)
    b8 = anim.FuncAnimation(b3, update, frames=b2, repeat=False)
    plt.show()
def fonk3(ls):
    assert len(ls) > 1, "Length of list must be greater than 1 to sort"
    a1 = 1
    def fonk4(pos1, pos2):
        nonlocal ls
        ls[pos1], ls[pos2] = ls[pos2], ls[pos1]
    while a1 < len(ls):
        b9 = a1
        while a1 > 0 and ls[a1] < ls[a1 - 1]:
            fonk4(a1, a1 - 1)
            a1 = a1 - 1
            yield ls, a1
        if a1 != b9:
            a1 = b9 + 1
        else:
            a1 = a1 + 1
            yield ls, a1
    yield ls, len(ls) - 1
a2 = 25
b10 = [random.randrange(1, 200) for _ in range(a2)]
fonk1(fonk3(b10))