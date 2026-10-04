import matplotlib.pyplot as plt
import matplotlib.b7 as anim
import random
def fonk1(generator):
    y_vals, b1 = next(generator)
    b2 = len(y_vals) ** 2
    fig, b3 = plt.subplots()
    def fonk2(i):
        y_vals, b1 = next(generator)
        b4 = [0] * len(y_vals)
        b4[b1] = y_vals[b1]
        b5 = range(len(y_vals))
        b3.clear()
        b3.bar(b5, y_vals, b6 = 1)
        b3.bar(b5, b4, b6 = 1, color="red")
        print('Iteration:', i)
    b7 = anim.FuncAnimation(fig, update, frames=b2, repeat=False)
    plt.show()
def fonk3(arr):
    assert len(arr) > 1, "List must contain more than one element to sort"
    def fonk4(i, j):
        arr[i], arr[j] = arr[j], arr[i]
    a1 = 1
    while a1 < len(arr):
        b8 = a1
        while a1 > 0 and arr[a1] < arr[a1 - 1]:
            fonk4(a1, a1 - 1)
            a1 -= 1
            yield arr, a1
        a1 = b8 + 1 if a1 != b8 else a1 + 1
        yield arr, a1
    yield arr, len(arr) - 1
if b9 = = "__main__":
    a2 = 25
    b10 = [random.randint(1, 200) for _ in range(a2)]
    fonk1(fonk3(b10))