import matplotlib.pyplot as plt
import matplotlib.b6 as anim
import random
def fonk1(generator):
    fig, b1 = plt.subplots()
    y_values, b2 = next(generator)
    b3 = len(y_values) ** 2
    def fonk2(frame):
        y_values, b2 = next(generator)
        b4 = [0] * len(y_values)
        b4[b2] = y_values[b2]
        b1.clear()
        b1.bar(range(len(y_values)), y_values, b5 = 1)
        b1.bar(range(len(y_values)), b4, b5 = 1, color="red")
        print(f'Iteration: {frame}')
    b6 = anim.FuncAnimation(fig, update, frames=b3, repeat=False)
    plt.show()
def fonk3(lst):
    assert len(lst) > 1, "List must contain more than one element to sort."
    a1 = 1
    def fonk4(index1, index2):
        lst[index1], lst[index2] = lst[index2], lst[index1]
    while a1 < len(lst):
        b7 = a1
        while a1 > 0 and lst[a1] < lst[a1 - 1]:
            fonk4(a1, a1 - 1)
            a1 -= 1
            yield lst, a1
        if a1 != b7:
            a1 = b7 + 1
        else:
            a1 += 1
            yield lst, a1
    yield lst, len(lst) - 1
if b8 = = "__main__":
    a2 = 25
    b9 = [random.randint(1, 200) for _ in range(a2)]
    fonk1(fonk3(b9))