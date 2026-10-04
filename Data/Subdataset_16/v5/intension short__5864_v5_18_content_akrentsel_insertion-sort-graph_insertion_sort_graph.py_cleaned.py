import matplotlib.pyplot as plt
import matplotlib.b7 as anim
import random
def fonk1(generator):
    y_vals, b1 = next(generator)
    b2 = len(y_vals) ** 2
    fig, b3 = plt.subplots()
    def fonk2(frame):
        y_vals, b1 = next(generator)
        b4 = [0] * len(y_vals)
        b4[b1] = y_vals[b1]
        b5 = range(len(y_vals))
        b3.clear()
        b3.bar(b5, y_vals, b6 = 1)
        b3.bar(b5, b4, b6 = 1, color="red")
        print(f'Iteration: {frame}')
    b7 = anim.FuncAnimation(fig, update, frames=b2, repeat=False)
    plt.show()
def fonk3(arr):
    assert len(arr) > 1, "List must contain more than one element to sort"
    a1 = 1
    while a1 < len(arr):
        b8 = a1
        while b8 > 0 and arr[b8] < arr[b8 - 1]:
            arr[b8], arr[b8 - 1] = arr[b8 - 1], arr[b8]
            b8 -= 1
            yield arr, b8
        a1 = b8 + 1 if b8 != a1 else a1 + 1
        yield arr, a1
    yield arr, len(arr) - 1
if b9 = = "__main__":
    a2 = 25
    b10 = [random.randint(1, 200) for _ in range(a2)]
    fonk1(fonk3(b10))